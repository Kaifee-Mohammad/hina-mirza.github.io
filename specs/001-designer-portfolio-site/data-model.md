# Data Model: Designer Portfolio Website

**Feature**: 001-designer-portfolio-site
**Date**: 2025-12-25
**Purpose**: Define WordPress content structure, taxonomies, and custom fields

## Overview

This document defines the data structures needed for the portfolio website using WordPress native capabilities and Blocksy theme features.

---

## WordPress Content Types

### 1. Portfolio Items (Custom Post Type)

**Purpose:** Individual artwork and design pieces for gallery showcase

**Post Type:** `portfolio` (or use WordPress Posts with category filter)

**Fields:**

| Field Name | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| title | Text | Yes | Artwork title/name | Max 200 characters |
| description | Rich Text | Yes | Artwork description, inspiration, technique | Max 2000 characters |
| featured_image | Image | Yes | Primary portfolio image | Min 1200x800px, optimized |
| gallery_images | Image Gallery | No | Additional views/detail shots | Max 10 images |
| category | Taxonomy | Yes | Fabric, Wallpaper, Paintings, Home Goods | Single selection |
| dimensions | Text | No | Physical dimensions (e.g., "24x36 inches") | Free text |
| materials | Text | No | Materials used (e.g., "Watercolor on paper") | Free text |
| year_created | Number | No | Year artwork was created | YYYY format |
| availability_status | Select | Yes | Available, Sold, Commission Only, Not For Sale | Single selection |
| price | Text | No | Display price (e.g., "$500" or "Contact for pricing") | Free text |
| display_order | Number | No | Manual sorting order | Integer |

**Taxonomies:**

```
portfolio_category (hierarchical):
├── Fabric
├── Wallpaper
├── Paintings
└── Home Goods

portfolio_tag (non-hierarchical):
└── Free-form tags (botanical, floral, protea, etc.)
```

**States:**
- Draft: Work in progress, not visible
- Published: Live on website
- Archived: No longer displayed but retained in database

---

### 2. Products (Custom Post Type or Standard Posts)

**Purpose:** Commercial items available for inquiry (not e-commerce)

**Post Type:** `product` (or use WordPress Posts with different category)

**Fields:**

| Field Name | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| title | Text | Yes | Product name | Max 200 characters |
| description | Rich Text | Yes | Product description, use cases, details | Max 2000 characters |
| featured_image | Image | Yes | Primary product image | Min 1200x800px |
| product_images | Image Gallery | No | Additional product photos | Max 10 images |
| category | Taxonomy | Yes | Fabric, Wallpaper, Home Goods | Single selection |
| price | Text | Yes | Display price or "Contact for pricing" | Free text |
| size_options | Text | No | Available sizes/dimensions | Free text |
| material_details | Text | No | Material composition, care instructions | Free text |
| availability | Select | Yes | Available, Out of Stock, Made to Order | Single selection |
| inquiry_button | Boolean | Yes | Show "Inquire About This Item" button | Default: true |
| related_portfolio | Relationship | No | Link to related portfolio artwork | Portfolio item ID |

**Taxonomies:**

```
product_category (hierarchical):
├── Fabric
│   ├── Cotton
│   ├── Silk
│   └── Linen
├── Wallpaper
│   ├── Removable
│   └── Traditional
└── Home Goods
    ├── Pillows
    ├── Art Prints
    └── Stationery
```

---

### 3. Pages (Standard WordPress Pages)

**Purpose:** Static informational pages

**Page Structure:**

| Page Name | Slug | Template | Purpose |
|-----------|------|----------|---------|
| Home | `/` | Homepage | Hero, portfolio highlights, Instagram feed |
| Portfolio | `/portfolio/` | Portfolio Archive | Full portfolio gallery with filtering |
| Shop | `/shop/` | Product Archive | Product listings with inquiry buttons |
| About | `/about/` | Standard Page | Artist bio, philosophy, contact CTA |
| Contact | `/contact/` | Standard Page | Contact form, email, social links |

**Home Page Sections:**
- Hero section with tagline "ELEGANT . SOFT . PAINTERLY"
- Portfolio highlights (6-8 featured items)
- Instagram feed (12 recent posts)
- About preview snippet
- Contact CTA

---

### 4. Inquiries (Contact Form Submissions)

**Purpose:** Capture visitor inquiries about products or collaborations

**Storage:** Contact Form 7 database or email delivery

**Fields:**

| Field Name | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| name | Text | Yes | Visitor name | Max 100 characters |
| email | Email | Yes | Visitor email | Valid email format |
| subject | Select | Yes | Inquiry type | General, Product Inquiry, Collaboration, Other |
| related_product | Text | No | Auto-filled if from product page | Product title |
| message | Textarea | Yes | Inquiry message | Max 2000 characters |
| consent | Checkbox | Yes | Privacy policy consent | Boolean |
| timestamp | Datetime | Auto | Submission timestamp | ISO 8601 |
| ip_address | Text | Auto | Visitor IP (spam prevention) | IPv4/IPv6 |

**Delivery Method:** Email to Hina's email address
**Retention:** Store in database for 90 days (GDPR compliance)

---

## Instagram Feed Integration

**Data Source:** Instagram account @hinamirza.art.design via Smash Balloon plugin

**Cached Data Structure:**

| Field | Type | Source | Refresh Rate |
|-------|------|--------|--------------|
| post_id | String | Instagram API | On cache refresh |
| image_url | URL | Instagram CDN | On cache refresh |
| caption | Text | Instagram API | On cache refresh |
| post_link | URL | Instagram API | On cache refresh |
| timestamp | Datetime | Instagram API | On cache refresh |
| likes_count | Number | Instagram API (if available) | On cache refresh |

**Cache Settings:**
- Refresh interval: 6-12 hours
- Display count: 12 posts
- Layout: Grid (3 columns desktop, 2 mobile)
- Fallback: Display cached posts if API unavailable

---

## User Roles & Permissions

**Admin (Hina):**
- Full access to all content
- Create/edit/delete portfolio items
- Create/edit/delete products
- Edit pages
- Manage plugins and settings
- View form submissions

**Permissions Configured:**
- No additional users needed (single admin)
- No public user registration
- No comment system (disabled)

---

## Content Relationships

```
Portfolio Item ──(1:1)──> Featured Image
              └──(1:N)──> Gallery Images
              └──(M:N)──> Portfolio Categories
              └──(M:N)──> Tags

Product ──(1:1)──> Featured Image
        └──(1:N)──> Product Images
        └──(M:N)──> Product Categories
        └──(1:1)──> Related Portfolio Item (optional)

Inquiry ──(1:1)──> Related Product (optional)
```

---

## Data Validation Rules

### Image Upload Requirements
- **Minimum dimensions:** 1200x800px
- **Maximum file size:** 10MB (before optimization)
- **Accepted formats:** JPG, PNG, WebP
- **Automatic processing:** ShortPixel optimization (Glossy JPEG mode)
- **Output:** <500KB optimized file

### Text Field Limits
- **Titles:** 200 characters (SEO optimal)
- **Descriptions:** 2000 characters
- **Short descriptions:** 300 characters
- **Meta descriptions:** 160 characters (SEO)

### Required Fields Enforcement
- Cannot publish without featured image
- Cannot publish without title
- Cannot publish without category selection
- Inquiry forms require name, email, message

---

## Content Migration Mapping

### From Existing Site to New Site

**Current Astra + WooCommerce Structure:**

| Current | New Structure | Migration Method |
|---------|--------------|------------------|
| WooCommerce Products | Custom Post Type: Products | Export/import with category mapping |
| Gallery Posts | Custom Post Type: Portfolio | Export/import, regenerate thumbnails |
| Pages | Standard Pages | Direct export/import, rebuild layouts |
| Media Library | Media Library | FTP download/upload, run ShortPixel |
| Product Categories | Product Categories taxonomy | Import with hierarchy |

**Custom Field Migration:**
- WooCommerce price → Custom field: price (text)
- WooCommerce SKU → Not needed (no e-commerce)
- WooCommerce inventory → Custom field: availability
- Product images → Gallery images custom field

---

## SEO & Meta Data

**Per Content Type:**

| Field | Usage | Max Length |
|-------|-------|-----------|
| meta_title | Browser title, search results | 60 characters |
| meta_description | Search result snippet | 160 characters |
| og_image | Social media sharing | Featured image |
| og_title | Social media card | 60 characters |
| og_description | Social media card | 160 characters |

**Managed By:** Yoast SEO or Rank Math plugin
**Configuration:** Template-based with manual override capability

---

## Performance Considerations

### Database Optimization
- **Revisions:** Limit to 5 per post (reduce database bloat)
- **Auto-drafts:** Delete after 7 days
- **Trash:** Auto-delete after 30 days
- **Transients:** Clear expired weekly

### Image Storage
- **Original uploads:** Stored in wp-content/uploads/YYYY/MM/
- **Optimized versions:** Replace originals via ShortPixel
- **Thumbnails:** Generate standard WordPress sizes + custom
- **Lazy loading:** Enabled for all images below fold

### Caching Strategy
- **Page caching:** Server-level (via hosting) or plugin
- **Object caching:** Not needed for <1000 visitors/month
- **Instagram feed:** 6-12 hour cache
- **Asset caching:** Browser cache headers (1 year for static assets)

---

## Content Workflow

### Adding New Portfolio Item
1. Admin logs into WordPress
2. Navigate to Portfolio > Add New
3. Enter title and description
4. Upload featured image (auto-optimized by ShortPixel)
5. Add gallery images if applicable
6. Select category
7. Fill dimensions, materials, availability
8. Set price or "Contact for pricing"
9. Publish → Appears on portfolio page immediately

**Time estimate:** 5-10 minutes per item

### Adding New Product
1. Admin logs into WordPress
2. Navigate to Products > Add New
3. Enter product name and description
4. Upload product images
5. Select category and subcategory
6. Enter price, size options, materials
7. Set availability status
8. Inquiry button auto-enabled
9. Publish → Appears on shop page immediately

**Time estimate:** 10-15 minutes per product

---

## Backup & Recovery

### Automated Backups
- **Frequency:** Daily (included in hosting)
- **Retention:** 30 days
- **Includes:** Database, media files, theme/plugin files
- **Storage:** Off-site (hosting provider)

### Manual Export
- **WordPress content:** Tools > Export (XML)
- **Database:** phpMyAdmin export
- **Media library:** FTP/SFTP download
- **Frequency:** Monthly recommended

---

## Security Considerations

### Data Protection
- **Contact form data:** Encrypted in transit (HTTPS)
- **Database:** Protected by hosting firewall
- **File uploads:** Scanned by Wordfence
- **Admin login:** SSL required, strong password enforced

### Privacy Compliance
- **Form consent:** Required checkbox for GDPR
- **Cookie notice:** Add cookie consent banner
- **Privacy policy:** Page with data handling explanation
- **Data retention:** 90 days for form submissions

---

## Future Scalability

### Growth Accommodations
- **Content structure** supports unlimited portfolio items
- **Taxonomies** can be expanded (new categories, tags)
- **Custom fields** can be added without migration
- **E-commerce** can be added later (WooCommerce plugin)

### Migration Path
- Current structure compatible with WooCommerce
- Can upgrade to custom post type plugins if needed
- Can switch themes without data loss (standard WordPress)
- Can export to any WordPress site

---

## Implementation Notes

### Blocksy Theme Integration
- Portfolio custom post type via CPT UI plugin or code
- Use Blocksy Query Loop blocks for portfolio display
- Filter controls via Blocksy filter widgets
- Gallery lightbox via Blocksy lightbox feature

### Alternative: Use Standard Posts
- **Option:** Use WordPress Posts instead of custom post types
- **Categories:** Create "Portfolio" and "Products" parent categories
- **Pros:** Simpler, no additional plugins
- **Cons:** Less flexible, mixed content types

**Recommendation:** Start with standard Posts + Categories for simplicity. Add custom post types only if needed.

---

This data model provides a complete structure for content management while maintaining simplicity for a non-technical user.
