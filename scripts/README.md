# Testing Scripts

This directory contains automated testing scripts for the Jekyll website.

## UI Test Script

The `ui_test.sh` script automatically tests the website UI after changes are made.

### What it tests:

1. **Server Status** - Verifies Jekyll server is running
2. **Page Loading** - Tests all main pages (Homepage, Portfolio, Art Prints, About, Contact)
3. **Images** - Verifies all placeholder images are accessible
4. **CSS** - Checks that stylesheets load correctly
5. **JavaScript** - Ensures main.js is accessible
6. **Lightbox** - Confirms lightbox modal elements exist

### Usage:

```bash
# Make sure Jekyll server is running first
bundle exec jekyll serve

# In another terminal, run the test
./scripts/ui_test.sh
```

### Example Output:

```
============================================================
UI Test Suite - Thu Dec 25 22:00:55 GMT 2025
============================================================

Testing server status...
✓ Server Status: Server running at http://localhost:4000

Testing Homepage...
✓ Homepage Load: Page loads successfully
✓ Homepage Images: 3 images found in HTML
✓ Homepage SVG Images: 2 SVG images found
✓ Homepage CSS: 2 stylesheets found
✓ Lightbox Elements: Lightbox container found

...

============================================================
Test Summary
============================================================
✓ Passed:  17
✗ Failed:  0
⚠ Warnings: 0
============================================================

All tests passed successfully!
```

### Exit Codes:

- `0` - All tests passed
- `1` - One or more tests failed

### Integration:

You can add this to a git pre-commit hook or CI/CD pipeline:

```bash
# Run tests before committing
./scripts/ui_test.sh && git commit -m "Your message"
```

## Image Conversion Scripts

### convert_svg_to_png.py

Python script to convert SVG placeholder images to PNG format if needed.

**Requirements:**
- Python 3
- One of: cairosvg, rsvg-convert, or ImageMagick

**Usage:**
```bash
python3 scripts/convert_svg_to_png.py
```

### ui_test.py

Advanced Python-based UI testing module with detailed reporting.

**Requirements:**
- Python 3
- `pip3 install --user requests beautifulsoup4`

**Usage:**
```bash
python3 scripts/ui_test.py
```

This generates a detailed JSON report saved to `test_results.json`.

## Automated Testing Workflow

Recommended workflow after making changes:

1. Make your changes to the site
2. Save files (Jekyll will auto-rebuild)
3. Run `./scripts/ui_test.sh` to verify everything works
4. If tests pass, commit your changes
5. If tests fail, review the output and fix issues

## Tips:

- The UI test should complete in under 10 seconds
- Run tests frequently during development
- All tests should pass before pushing to production
- Add new tests as you add new features
