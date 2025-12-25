# Research Findings: Designer Portfolio Website

**Date**: 2025-12-25
**Feature**: 001-designer-portfolio-site
**Purpose**: Technology selection and best practices for WordPress portfolio implementation

## Overview

This document consolidates research findings for all technical decisions required to build a fast, affordable, manageable WordPress portfolio website for designer Hina Mirza.

---

## 1. WordPress Theme Selection

### Decision: **Blocksy Free**

**Rationale:**
- Only theme offering native drag-and-drop portfolio customization WITHOUT requiring third-party page builder
- Uses WordPress native block editor (Gutenberg) - intuitive for non-technical designers
- Built-in patterns and blocks specifically for portfolio galleries
- Exceptional user rating: 4.95/5 stars (863 reviews)
- Modern block-based architecture ensures excellent PageSpeed scores
- 300,000+ active installations prove reliability
- Completely free with optional premium upgrades
- Future-proof: native WordPress block system ensures long-term compatibility

**Alternatives Considered:**

| Theme | Rating | Why Not Selected |
|-------|--------|-----------------|
| **Astra Free** | 4.9/5 (1M+ installs) | Requires separate page builder plugin (Elementor) - adds complexity |
| **GeneratePress** | 4.98/5 (500K installs) | Too minimal for non-technical users; best for developers |
| **Kadence** | 4.9/5 (400K installs) | Still requires page builder for full drag-and-drop functionality |
| **OceanWP** | 4.9/5 (500K installs) | Requires page builder; no advantage over Blocksy |

**Performance Expectations:**
- PageSpeed Desktop: 90-98 points
- PageSpeed Mobile: 85-92 points
- Load time: 1.2-1.8 seconds (homepage)
- Core Web Vitals: Excellent (LCP <2.5s, FID <100ms, CLS <0.1)

---

## 2. Page Builder Selection

### Decision: **WordPress Gutenberg (Block Editor) - Built into Blocksy**

**Rationale:**
- Native WordPress block editor - no additional plugin needed
- Zero performance overhead (no extra plugin weight)
- Blocksy enhances Gutenberg with portfolio-specific blocks
- Completely free with no limitations
- Future-proof as WordPress continues investing in blocks
- Intuitive for designers (block-based visual editing)
- Best Core Web Vitals performance of all options

**Alternatives Considered:**

| Builder | Why Not Selected |
|---------|-----------------|
| **Elementor Free** | Adds 10-15% load time; requires separate 50MB+ plugin; good option if Blocksy doesn't meet needs |
| **Beaver Builder Free** | Requires separate plugin; fewer features in free version; smaller community |
| **Brizy** | Context-sensitive UI is nice but adds plugin overhead; Gutenberg + Blocksy simpler |
| **SiteOrigin** | Grid-based system too technical; steeper learning curve than Gutenberg |

**Note:** If Hina finds Gutenberg/Blocksy limiting later, can switch to Astra + Elementor Free without losing content.

---

## 3. Instagram Feed Integration

### Decision: **Smash Balloon Social Photo Feed (Free)**

**Rationale:**
- 100 free credits/month handles 50-100 images easily
- Most reliable: 49.3M+ downloads, 4.9/5 stars
- Easiest setup: one-click Instagram connection, no developer account needed
- Built-in CDN included (no extra services required)
- Auto-updates feed automatically (cache-based)
- "Approved Instagram partner" - handles Meta API changes
- WebP/AVIF conversion included
- Minimal performance impact
- Excellent support community

**Alternatives Considered:**

| Plugin | Why Not Selected |
|--------|-----------------|
| **Feed Them Social** | 4.7/5 stars, requires Instagram Professional account setup; more complex token management |
| **Spotlight** | Smaller user base; limited documentation |
| **WPZOOM** | Too basic; limited customization |

**Implementation Notes:**
- @hinamirza.art.design MUST be Instagram Professional/Business account (required post-Dec 2024)
- Free tier displays user feed perfectly with grid layout
- Photos auto-update when new posts added to account
- No hashtag feeds in free version (acceptable for user feed only)

---

## 4. Image Optimization Plugin

### Decision: **ShortPixel Image Optimizer (Free Tier)**

**Rationale:**
- 100 free credits/month sufficient for 50-100 portfolio images
- "Glossy JPEG" mode specifically designed for artwork preservation
- Maintains portfolio-worthy visual quality (better than generic lossless)
- Built-in CDN included (no Cloudflare needed)
- Free WebP/AVIF conversion
- Auto-optimizes new uploads
- Bulk optimization for existing images
- Non-technical friendly setup
- Estimated 40-50% file size reduction while maintaining quality
- Minimal site impact

**Alternatives Considered:**

| Plugin | Why Not Selected |
|--------|-----------------|
| **EWWW Image Optimizer** | Unlimited free, but local processing uses server resources; good backup option |
| **Imagify** | Only 20MB/month free (~200 images) - too limiting; $4.99/month for 500MB acceptable if needed |
| **Smush Free** | Lossless only, no WebP in free tier; less effective for portfolio images |

**Expected Results:**
- Portfolio images: 40-60% size reduction
- Individual image sizes: <500KB (from original 1-3MB)
- Quality preservation: Excellent for artwork showcase
- Load time improvement: ~30-40% faster image loading

---

## 5. Hosting Provider

### Decision: **Bluehost Essentials Plan ($6.99/month) or Hostinger Business WordPress ($3.99/month initial)**

**Rationale - Bluehost Essentials ($6.99/month):**
- WordPress.org official recommendation
- No renewal shock (flat $6.99/month pricing)
- 99.99% uptime SLA with compensation
- 24/7 support including phone
- Free SSL certificate
- Free CDN included
- One-click WordPress install
- Proven reliability for portfolios
- Stays within $10/month budget permanently

**Alternative - Hostinger Business WordPress:**
- Cheaper initial: $3.99/month (renews ~$9.99/month)
- 200GB NVMe storage (more than needed)
- LiteSpeed servers with caching (faster)
- WordPress staging environment
- Daily backups included
- Git integration + SSH access
- Unmetered bandwidth
- Fits budget if renewal acceptable

**Alternatives Considered:**

| Provider | Initial | Renewal | Why Not Primary Choice |
|----------|---------|---------|----------------------|
| **SiteGround** | $3.75 | $13.99+ | Renewal exceeds $10/month budget |
| **DreamHost** | $2.59 | $3.99+ | Good value but less WordPress-focused than Bluehost |
| **A2 Hosting** | $2.99 | $8.99 | Less well-known; cPanel good but Bluehost preferred |

**Final Recommendation:**
- **Budget-conscious**: Hostinger Business WordPress ($3.99 → $9.99)
- **Long-term stability**: Bluehost Essentials ($6.99 flat rate)
- **Best support**: SiteGround (if $13.99 renewal acceptable)

---

## 6. Additional Essential Plugins

### Contact Forms
**Decision:** Contact Form 7 (Free)
- Most popular (5M+ installs)
- Simple, lightweight
- Email delivery reliable
- Adequate for inquiry-based sales

**Alternatives:** WPForms Lite, Forminator

### SEO Optimization
**Decision:** Yoast SEO Free or Rank Math Free
- Both excellent free options
- Yoast: More established (5M+ installs)
- Rank Math: More features in free tier
- Either acceptable - suggest Yoast for simplicity

### Caching (Optional)
**Decision:** WP Super Cache or W3 Total Cache
- Only if hosting doesn't provide caching
- Bluehost/Hostinger include caching
- Use if site feels slow after launch

### Security
**Decision:** Wordfence Security (Free)
- Firewall and malware scanner
- Free tier sufficient for portfolio
- 4M+ active installations

---

## 7. Domain Migration Strategy

### Current Situation
- Domain: hinamirza.co
- Currently points to existing WordPress site
- Uses Astra theme + Elementor + WooCommerce

### Migration Approach

**Step 1: Content Backup**
- Export WordPress content (Tools > Export)
- Download media library via FTP or plugin
- Screenshot all pages for reference
- Export theme customizer settings if possible

**Step 2: New Site Setup**
- Set up new hosting (Bluehost or Hostinger)
- Install WordPress with Blocksy theme
- Install essential plugins
- Build new portfolio structure

**Step 3: Content Migration**
- Import WordPress XML export
- Upload images to new media library
- Recreate pages using Blocksy blocks
- Set up Instagram feed
- Configure contact forms
- Set up inquiry buttons for products

**Step 4: DNS Changeover**
- Update DNS nameservers to point to new host
- Wait 24-48 hours for propagation
- Test thoroughly before removing old site

**Estimated Timeline:** 2-3 days (DNS propagation is longest part)

---

## 8. Content Structure & Organization

### Custom Post Types Needed
1. **Portfolio Items** - Individual artwork pieces
2. **Products** - Commercial items available for inquiry

### Taxonomies (Categories)
- Fabric
- Wallpaper
- Paintings
- Home Goods

### Custom Fields Required
- Pricing (text field)
- Dimensions (text field)
- Materials (text field)
- Availability status (dropdown: Available, Sold, Commission)
- Inquiry button (automatic on all products)

### Pages Required
1. Home - Hero + portfolio highlights + Instagram feed
2. Portfolio - Full artwork gallery with filtering
3. Shop/Products - Product listings with inquiry buttons
4. About - Artist bio and brand story
5. Contact - Contact form

**Implementation:** Can be achieved with Blocksy + standard WordPress features, no custom post types plugin needed initially.

---

## 9. Performance Optimization Strategy

### Initial Setup
- Install Blocksy theme (lightweight foundation)
- ShortPixel optimization for all images
- Instagram feed caching enabled
- Browser caching via hosting

### Ongoing Optimization
- Optimize images before upload (Photoshop/Canva export for web)
- Use ShortPixel auto-optimization
- Lazy load images (built into Blocksy)
- Minimal plugin footprint (remove unused)
- Regular WordPress/plugin updates

### Performance Targets
- Homepage load: <3 seconds
- Portfolio page: <3 seconds
- Google PageSpeed Mobile: 80+
- Google PageSpeed Desktop: 90+
- Core Web Vitals: All green

**Expected Results:** Achievable with selected technology stack without additional optimization.

---

## 10. Budget Summary

### One-Time Setup Costs
| Item | Cost |
|------|------|
| Blocksy Theme | $0 (free) |
| Domain (if new) | $0 (existing: hinamirza.co) |
| Premium plugins | $0 (all free tier sufficient) |
| Migration/setup | $0 (DIY with documentation) |
| **Total Setup** | **$0** |

### Monthly Recurring Costs
| Item | Cost |
|------|------|
| Hosting (Bluehost Essentials) | $6.99/month |
| OR Hosting (Hostinger Business) | $3.99/month ($9.99 renewal) |
| ShortPixel (100 credits) | $0/month |
| Instagram Feed | $0/month |
| Image optimization | $0/month |
| All plugins | $0/month |
| **Total Monthly** | **$3.99-$6.99/month** |

### Annual Costs
| Item | Cost |
|------|------|
| Domain renewal | ~$15/year |
| Hosting (Bluehost) | $83.88/year |
| OR Hosting (Hostinger renewal) | ~$120/year |
| **Total Annual** | **$98.88-$135/year** |

**Conclusion:** Stays well within budget (<$10/month target).

---

## 11. Non-Technical User Considerations

### Ease of Content Management
- **Portfolio updates:** Blocksy block editor = drag-and-drop artwork images
- **Product listings:** Create new post, add images, write description, publish
- **Page edits:** Visual block editor, no code required
- **Instagram feed:** Automatic updates, no manual management
- **Image optimization:** Automatic on upload, no user action needed

### Learning Curve
- **Blocksy:** 1-2 hours to understand blocks
- **WordPress admin:** Familiar if already uses WordPress
- **Portfolio management:** 10 minutes per new item once learned
- **No technical knowledge required**

### Support Resources
- Blocksy documentation (excellent)
- WordPress.org forums (massive community)
- Smash Balloon support (responsive)
- YouTube tutorials abundant
- Facebook groups active

---

## 12. Migration from Existing Site

### Current Tech Stack Analysis
- **Current:** Astra + Elementor + WooCommerce
- **New:** Blocksy + Gutenberg + No e-commerce

### Content That Transfers Easily
- Posts and pages (WordPress export)
- Images (media library)
- Text content
- Product descriptions

### Content Requiring Rebuild
- Page layouts (Elementor → Gutenberg blocks)
- WooCommerce products → Simple portfolio posts
- Shopping cart → Inquiry buttons

### Estimated Migration Time
- Content export/backup: 1 hour
- New site setup: 2-3 hours
- Content recreation: 5-10 hours
- Testing and refinement: 2-3 hours
- **Total:** 10-16 hours of work

---

## 13. Risk Mitigation

### Potential Issues & Solutions

**Issue:** Instagram API changes breaking feed
- **Solution:** Smash Balloon handles API changes automatically as "approved partner"
- **Backup:** Can use static Instagram link or embed if feed fails

**Issue:** Hosting performance inadequate
- **Solution:** Both recommended hosts have 30-day money-back; can switch
- **Upgrade path:** Increase hosting tier if traffic grows

**Issue:** Image optimization credits run out
- **Solution:** 100 credits/month sufficient; upgrade to $9.99/month unlimited if needed
- **Alternative:** Switch to EWWW unlimited free

**Issue:** User finds Gutenberg too limiting
- **Solution:** Can switch to Astra + Elementor Free without data loss
- **Export:** Gutenberg content exports cleanly

**Issue:** Domain DNS propagation issues
- **Solution:** Keep old site running during transition; 24-48hr propagation normal

---

## 14. Future Expansion Options

### Phase 2 Enhancements (Optional)
- **E-commerce:** Add WooCommerce if she wants shopping cart later ($0)
- **Email marketing:** Mailchimp free tier (2,000 subscribers)
- **Booking system:** Calendly integration for consultations
- **Blog:** WordPress native (already included)
- **Multilingual:** WPML or Polylang plugin ($0-$199)

### Scalability Path
- Current setup handles 10,000 visitors/month easily
- If traffic grows: Upgrade hosting tier ($15-30/month)
- If needing advanced features: Blocksy Pro ($99 one-time)
- All upgrades optional, not required for launch

---

## 15. Final Technology Stack Summary

| Component | Selected Technology | Cost |
|-----------|-------------------|------|
| **CMS** | WordPress 6.4+ | Free |
| **Theme** | Blocksy Free | Free |
| **Page Builder** | Gutenberg (native) | Free |
| **Hosting** | Bluehost Essentials or Hostinger Business | $3.99-$6.99/mo |
| **Image Optimization** | ShortPixel Free | Free |
| **Instagram Feed** | Smash Balloon Free | Free |
| **Contact Forms** | Contact Form 7 | Free |
| **SEO** | Yoast SEO Free | Free |
| **Security** | Wordfence Free | Free |
| **Domain** | Existing (hinamirza.co) | ~$15/year renewal |

**Total Monthly Cost:** $3.99-$6.99
**Total Annual Cost:** $98.88-$135
**Setup Cost:** $0

---

## Conclusion

All technical decisions have been made based on:
1. **Budget constraints:** <$10/month ✓
2. **Performance targets:** <3s load, 80+ PageSpeed ✓
3. **Ease of use:** Non-technical friendly ✓
4. **No e-commerce:** Inquiry-based only ✓
5. **Reliability:** Established, well-supported technologies ✓
6. **Future-proof:** Modern, maintained solutions ✓

**Next Phase:** Design & Contracts (data models, page layouts, integration specifications)
