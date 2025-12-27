# Hina Mirza Portfolio Website Constitution

## Core Principles

### I. Minimize Scrolling (NON-NEGOTIABLE)
**Always strive to minimize vertical scrolling on all pages.**
- Maximize visible content within the viewport
- Use compact layouts and efficient spacing
- Avoid unnecessary padding or whitespace
- Content should fit within one screen when possible
- Use horizontal space efficiently before adding vertical content
- Test all pages to ensure minimal scrolling required
- Mobile: Content must be accessible without excessive scrolling

### II. Visual Simplicity
**Clean, elegant design that showcases artwork.**
- Minimal UI elements that don't distract from art
- Consistent color palette (peachy #d8c3be accent)
- Professional typography (Libre Baskerville + Montserrat)
- White space used intentionally, not excessively

### III. Mobile-First Responsive
**Site must work beautifully on all devices.**
- Design for mobile first, scale up
- Touch-friendly interface elements
- Images optimize for device size
- Compact layouts adapt smoothly

### IV. Performance First
**Fast loading is essential.**
- Optimize all images before uploading
- Minimize external dependencies
- Static site generation for speed
- Lazy load images when appropriate

### V. CMS Accessibility
**Hina must be able to manage all content without code.**
- WordPress-like interface (Netlify CMS)
- Drag-drop image uploads
- Visual editors for all content
- Clear, simple workflows

## Design Standards

### Layout Hierarchy
1. Navigation: Minimal, always visible
2. Content: Maximum viewport usage
3. Footer: Compact, essential info only

### Spacing Guidelines
- Vertical padding: Use sparingly (xs: 8px, sm: 16px max for most sections)
- Horizontal margins: Utilize full width where appropriate
- Gallery gaps: Minimal (8-16px) to show more items
- Hero sections: Compact, not full-screen

### Image Standards
- Thumbnails: Optimized size for quick loading
- Gallery: Responsive grid (250px → 200px → 150px)
- Lightbox: High quality on demand
- Format: SVG for placeholders, JPG/PNG for photos

## Development Workflow

### Before Committing
- [ ] Test locally at all breakpoints
- [ ] Check for excessive scrolling
- [ ] Run UI test suite (scripts/ui_test.sh)
- [ ] Verify mobile responsiveness
- [ ] Optimize any new images

### Testing Requirements
- All 17 UI tests must pass
- Visual check on mobile device
- Lightbox functionality verified
- Form submissions tested

## Governance

This constitution guides all design and development decisions.
Any changes that introduce excessive scrolling must be justified and approved.

**Version**: 1.0.0 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27
