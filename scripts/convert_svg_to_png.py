#!/usr/bin/env python3
"""
Convert SVG placeholder images to PNG format for browser compatibility
"""
import os
import subprocess
from pathlib import Path

def convert_svg_to_png(svg_path, png_path, width=800):
    """Convert SVG to PNG using built-in tools"""
    try:
        # Try using cairosvg if available
        import cairosvg
        cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width)
        print(f"✓ Converted (cairosvg): {svg_path} -> {png_path}")
        return True
    except ImportError:
        pass

    try:
        # Try using rsvg-convert (librsvg)
        result = subprocess.run(
            ['rsvg-convert', '-w', str(width), '-o', png_path, svg_path],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✓ Converted (rsvg): {svg_path} -> {png_path}")
            return True
    except FileNotFoundError:
        pass

    try:
        # Try using ImageMagick convert
        result = subprocess.run(
            ['convert', '-background', 'none', '-density', '150',
             '-resize', f'{width}x', svg_path, png_path],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✓ Converted (ImageMagick): {svg_path} -> {png_path}")
            return True
    except FileNotFoundError:
        pass

    print(f"✗ Could not convert {svg_path} - no converter available")
    return False

def main():
    base_dir = Path(__file__).parent.parent

    # Define directories
    dirs = [
        base_dir / 'assets' / 'images' / 'portfolio',
        base_dir / 'assets' / 'images' / 'prints'
    ]

    converted = 0
    failed = 0

    for directory in dirs:
        if not directory.exists():
            continue

        # Find all .jpg files that are actually SVG
        for file_path in directory.glob('*.jpg'):
            # Check if it's actually an SVG
            with open(file_path, 'r') as f:
                content = f.read(100)
                if '<svg' in content:
                    # It's an SVG, convert to PNG
                    png_path = file_path.with_suffix('.png')
                    if convert_svg_to_png(str(file_path), str(png_path)):
                        converted += 1
                    else:
                        failed += 1

    print(f"\nConversion complete: {converted} successful, {failed} failed")

    if failed > 0 and converted == 0:
        print("\nNo converters available. Installing cairosvg...")
        subprocess.run(['pip3', 'install', 'cairosvg'], check=False)
        print("Please run this script again.")

if __name__ == '__main__':
    main()
