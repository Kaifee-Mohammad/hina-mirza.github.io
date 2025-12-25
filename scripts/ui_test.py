#!/usr/bin/env python3
"""
UI Testing Module for Jekyll Site
Tests the UI after every change to ensure everything renders correctly
"""
import requests
import time
import sys
from pathlib import Path
from bs4 import BeautifulSoup
import json
from datetime import datetime
from urllib.parse import urljoin

class UITester:
    def __init__(self, base_url='http://localhost:4000'):
        self.base_url = base_url
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'tests': [],
            'passed': 0,
            'failed': 0,
            'warnings': 0
        }

    def log(self, status, test_name, message, details=None):
        """Log test result"""
        result = {
            'status': status,
            'test': test_name,
            'message': message,
            'details': details
        }
        self.results['tests'].append(result)

        if status == 'PASS':
            self.results['passed'] += 1
            print(f"✓ {test_name}: {message}")
        elif status == 'FAIL':
            self.results['failed'] += 1
            print(f"✗ {test_name}: {message}")
            if details:
                print(f"  Details: {details}")
        elif status == 'WARN':
            self.results['warnings'] += 1
            print(f"⚠ {test_name}: {message}")

    def test_server_running(self):
        """Test if Jekyll server is running"""
        try:
            response = requests.get(self.base_url, timeout=5)
            if response.status_code == 200:
                self.log('PASS', 'Server Status', f'Server running at {self.base_url}')
                return True
            else:
                self.log('FAIL', 'Server Status', f'Server returned {response.status_code}')
                return False
        except requests.exceptions.RequestException as e:
            self.log('FAIL', 'Server Status', f'Cannot connect to {self.base_url}', str(e))
            return False

    def test_page_loads(self, path='/', page_name='Homepage'):
        """Test if a page loads successfully"""
        url = urljoin(self.base_url, path)
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                self.log('PASS', f'{page_name} Load', f'Page loads successfully')
                return response.text
            else:
                self.log('FAIL', f'{page_name} Load', f'Page returned {response.status_code}')
                return None
        except requests.exceptions.RequestException as e:
            self.log('FAIL', f'{page_name} Load', f'Cannot load page', str(e))
            return None

    def test_images_present(self, html, page_name='Page'):
        """Test if images are present and accessible"""
        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')
        images = soup.find_all('img')

        if not images:
            self.log('WARN', f'{page_name} Images', 'No images found on page')
            return

        broken_images = []
        for img in images:
            src = img.get('src', '')
            if not src:
                broken_images.append('Empty src attribute')
                continue

            # Test image URL
            img_url = urljoin(self.base_url, src)
            try:
                response = requests.head(img_url, timeout=5)
                if response.status_code != 200:
                    broken_images.append(f'{src} ({response.status_code})')
            except requests.exceptions.RequestException:
                broken_images.append(f'{src} (unreachable)')

        if broken_images:
            self.log('FAIL', f'{page_name} Images',
                    f'{len(broken_images)}/{len(images)} images broken',
                    broken_images[:5])  # Show first 5
        else:
            self.log('PASS', f'{page_name} Images',
                    f'All {len(images)} images accessible')

    def test_css_loaded(self, html, page_name='Page'):
        """Test if CSS is loaded"""
        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')
        css_links = soup.find_all('link', rel='stylesheet')

        if not css_links:
            self.log('WARN', f'{page_name} CSS', 'No CSS stylesheets found')
            return

        broken_css = []
        for link in css_links:
            href = link.get('href', '')
            if not href:
                continue

            css_url = urljoin(self.base_url, href)
            try:
                response = requests.head(css_url, timeout=5)
                if response.status_code != 200:
                    broken_css.append(f'{href} ({response.status_code})')
            except requests.exceptions.RequestException:
                broken_css.append(f'{href} (unreachable)')

        if broken_css:
            self.log('FAIL', f'{page_name} CSS',
                    f'{len(broken_css)}/{len(css_links)} stylesheets broken',
                    broken_css)
        else:
            self.log('PASS', f'{page_name} CSS',
                    f'All {len(css_links)} stylesheets loaded')

    def test_js_loaded(self, html, page_name='Page'):
        """Test if JavaScript is loaded"""
        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')
        js_scripts = soup.find_all('script', src=True)

        if not js_scripts:
            self.log('WARN', f'{page_name} JavaScript', 'No external JS files found')
            return

        broken_js = []
        for script in js_scripts:
            src = script.get('src', '')
            if not src:
                continue

            js_url = urljoin(self.base_url, src)
            try:
                response = requests.head(js_url, timeout=5)
                if response.status_code != 200:
                    broken_js.append(f'{src} ({response.status_code})')
            except requests.exceptions.RequestException:
                broken_js.append(f'{src} (unreachable)')

        if broken_js:
            self.log('FAIL', f'{page_name} JavaScript',
                    f'{len(broken_js)}/{len(js_scripts)} scripts broken',
                    broken_js)
        else:
            self.log('PASS', f'{page_name} JavaScript',
                    f'All {len(js_scripts)} scripts loaded')

    def test_links_valid(self, html, page_name='Page', sample_size=10):
        """Test if internal links are valid (sample)"""
        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', href=True)
        internal_links = [l for l in links if l['href'].startswith('/')]

        if not internal_links:
            self.log('WARN', f'{page_name} Links', 'No internal links found')
            return

        # Test a sample of links
        sample = internal_links[:sample_size]
        broken_links = []

        for link in sample:
            href = link['href']
            link_url = urljoin(self.base_url, href)
            try:
                response = requests.head(link_url, timeout=5, allow_redirects=True)
                if response.status_code >= 400:
                    broken_links.append(f'{href} ({response.status_code})')
            except requests.exceptions.RequestException:
                broken_links.append(f'{href} (unreachable)')

        if broken_links:
            self.log('FAIL', f'{page_name} Links',
                    f'{len(broken_links)}/{len(sample)} sample links broken',
                    broken_links)
        else:
            self.log('PASS', f'{page_name} Links',
                    f'Tested {len(sample)}/{len(internal_links)} internal links - all valid')

    def test_lightbox_elements(self, html):
        """Test if lightbox modal elements exist"""
        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')

        # Check for lightbox container
        lightbox = soup.find(id='lightbox')
        if not lightbox:
            self.log('FAIL', 'Lightbox Elements', 'Lightbox container not found')
            return

        # Check for required lightbox elements
        required = {
            'lightbox-close': 'Close button',
            'lightbox-image': 'Image element',
            'lightbox-title': 'Title element',
            'lightbox-description': 'Description element'
        }

        missing = []
        for elem_id, name in required.items():
            if not soup.find(id=elem_id):
                missing.append(f'{name} (#{elem_id})')

        if missing:
            self.log('FAIL', 'Lightbox Elements',
                    f'{len(missing)} elements missing', missing)
        else:
            self.log('PASS', 'Lightbox Elements', 'All lightbox elements present')

    def run_all_tests(self):
        """Run all UI tests"""
        print(f"\n{'='*60}")
        print(f"UI Test Suite - {self.results['timestamp']}")
        print(f"{'='*60}\n")

        # Test 1: Server running
        if not self.test_server_running():
            print("\n✗ Server not running. Please start Jekyll server first.")
            return self.results

        # Wait a moment for server to be ready
        time.sleep(1)

        # Test pages
        pages = [
            ('/', 'Homepage'),
            ('/portfolio/', 'Portfolio'),
            ('/prints/', 'Art Prints'),
            ('/about/', 'About'),
            ('/contact/', 'Contact')
        ]

        for path, name in pages:
            print(f"\n--- Testing {name} ---")
            html = self.test_page_loads(path, name)
            if html:
                self.test_images_present(html, name)
                self.test_css_loaded(html, name)
                self.test_js_loaded(html, name)
                if name == 'Homepage':
                    self.test_lightbox_elements(html)
                self.test_links_valid(html, name)

        # Print summary
        print(f"\n{'='*60}")
        print(f"Test Summary")
        print(f"{'='*60}")
        print(f"✓ Passed:  {self.results['passed']}")
        print(f"✗ Failed:  {self.results['failed']}")
        print(f"⚠ Warnings: {self.results['warnings']}")
        print(f"{'='*60}\n")

        return self.results

    def save_results(self, output_file='test_results.json'):
        """Save test results to JSON file"""
        base_dir = Path(__file__).parent.parent
        output_path = base_dir / output_file

        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"Results saved to: {output_path}")

def main():
    tester = UITester()
    results = tester.run_all_tests()
    tester.save_results()

    # Exit with error code if tests failed
    if results['failed'] > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()
