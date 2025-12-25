# Quick Start Guide: Designer Portfolio Website

**Feature**: 001-designer-portfolio-site
**Date**: 2025-12-25
**Estimated Setup Time**: 4-6 hours

## Overview

This guide provides step-by-step instructions to set up the complete portfolio website from scratch, including hosting, WordPress installation, theme configuration, and content migration.

---

## Prerequisites

Before starting, ensure you have:

- [ ] Domain ownership access (hinamirza.co)
- [ ] Credit card for hosting signup (Bluehost or Hostinger)
- [ ] Instagram Professional account (@hinamirza.art.design)
- [ ] Email address for admin account
- [ ] Backup of existing website content (if migrating)
- [ ] 4-6 hours of uninterrupted time

---

## Phase 1: Hosting Setup (30 minutes)

### Option A: Bluehost Essentials (Recommended - $6.99/month flat rate)

1. **Sign Up for Hosting**
   - Go to: https://www.bluehost.com
   - Select "Essentials" plan ($6.99/month)
   - Domain: Choose "I have a domain" → Enter hinamirza.co
   - Create account with email and password
   - Enter payment information
   - Uncheck upsells (CodeGuard, SiteLock, etc.)
   - Complete purchase

2. **Access Control Panel**
   - Check email for "Welcome to Bluehost"
   - Click "Login to Bluehost"
   - Navigate to control panel (cPanel)

3. **Configure Domain**
   - If domain elsewhere: Get nameservers from Bluehost
     - Usually: ns1.bluehost.com, ns2.bluehost.com
   - Log in to domain registrar
   - Update DNS nameservers
   - Wait 24-48 hours for propagation

### Option B: Hostinger Business WordPress ($3.99/month, renews $9.99)

1. **Sign Up for Hosting**
   - Go to: https://www.hostinger.com
   - Select "Business WordPress" plan
   - Choose 48-month term for best pricing
   - Domain: "I'll use my existing domain"
   - Create account and complete payment

2. **Access hPanel**
   - Log in to Hostinger hPanel
   - Navigate to Websites section

3. **Configure Domain**
   - Add existing domain: hinamirza.co
   - Point domain nameservers to Hostinger
   - Nameservers will be provided in hPanel

---

## Phase 2: WordPress Installation (15 minutes)

### Bluehost Method

1. **One-Click WordPress Install**
   - In Bluehost dashboard, click "My Sites"
   - Click "Create Site"
   - Select "WordPress"
   - Site name: "Hina Mirza"
   - Tagline: "Botanical Artwork & Design"
   - Admin username: hinamirza (or preferred)
   - Admin password: [Create strong password]
   - Admin email: your@email.com
   - Click "Install"

2. **Access WordPress**
   - URL: hinamirza.co/wp-admin
   - Login with credentials created above
   - Save login credentials securely

### Hostinger Method

1. **WordPress Auto-Install**
   - From hPanel, click "Auto Installer"
   - Select "WordPress"
   - Choose domain: hinamirza.co
   - Admin details:
     - Username: hinamirza
     - Password: [Strong password]
     - Email: your@email.com
   - Click "Install"

2. **Access WordPress**
   - URL: hinamirza.co/wp-admin
   - Login with credentials

---

## Phase 3: SSL Certificate Setup (10 minutes)

### Enable HTTPS

1. **Install SSL Certificate**
   - Bluehost: Navigate to Security > SSL/TLS Status
   - Hostinger: Navigate to SSL section
   - Click "Install Free SSL" (Let's Encrypt)
   - Wait 5-10 minutes for activation

2. **Force HTTPS**
   - Install plugin: "Really Simple SSL"
   - Activate plugin
   - Click "Activate SSL" button
   - Test site: https://hinamirza.co

---

## Phase 4: Theme Installation (20 minutes)

### Install Blocksy Theme

1. **Install Theme**
   - WordPress Admin → Appearance → Themes
   - Click "Add New"
   - Search "Blocksy"
   - Click "Install" on Blocksy theme
   - Click "Activate"

2. **Import Starter Template (Optional)**
   - Blocksy → Starter Sites
   - Browse portfolio templates
   - Select template matching portfolio style
   - Click "Import" (imports demo content)
   - Choose "Import" (takes 5-10 minutes)

3. **Basic Theme Configuration**
   - Go to: Appearance → Customize
   - **Site Identity:**
     - Upload logo (if available)
     - Site title: "Hina Mirza"
     - Tagline: "Elegant, Soft, Painterly Botanical Artwork"
   - **Colors:**
     - Primary color: #d8c3be (peachy accent)
     - Text color: #3a3a3a (dark gray)
     - Background: #ffffff (white)
   - **Typography:**
     - Headings: Libre Baskerville or similar serif
     - Body: Montserrat or similar sans-serif
   - Click "Publish"

---

## Phase 5: Essential Plugins Installation (30 minutes)

### Install Required Plugins

Navigate to: Plugins → Add New

1. **Smash Balloon Social Photo Feed** (Instagram)
   - Search: "Instagram Feed"
   - Install "Smash Balloon Social Photo Feed"
   - Activate

2. **ShortPixel Image Optimizer** (Image Optimization)
   - Search: "ShortPixel"
   - Install and activate
   - Sign up for free account (100 credits/month)
   - Enter API key when prompted

3. **Contact Form 7** (Contact Forms)
   - Search: "Contact Form 7"
   - Install and activate

4. **Contact Form CFDB7** (Form Backup)
   - Search: "CFDB7"
   - Install and activate

5. **WP Mail SMTP** (Email Delivery)
   - Search: "WP Mail SMTP"
   - Install and activate

6. **Yoast SEO** or **Rank Math** (SEO)
   - Search: "Yoast SEO"
   - Install and activate
   - Run configuration wizard

7. **Wordfence Security** (Security - Optional)
   - Search: "Wordfence"
   - Install and activate
   - Run setup wizard

### Remove Unnecessary Plugins
- Delete default plugins (Hello Dolly, etc.)
- Keep: Akismet Anti-spam (optional)

---

## Phase 6: Instagram Feed Configuration (20 minutes)

1. **Connect Instagram Account**
   - Instagram Feed → Settings
   - Click "Connect Instagram Account"
   - Log in with @hinamirza.art.design
   - Grant permissions (read-only)
   - Verify connection successful

2. **Configure Feed Display**
   - Number of posts: 12
   - Layout: Grid
   - Columns: 3 (desktop), 2 (mobile)
   - Image resolution: Auto
   - Show header: No
   - Show follow button: Yes
   - Cache: 6 hours

3. **Test Feed**
   - Copy shortcode: `[instagram-feed]`
   - Create test page
   - Paste shortcode
   - Preview page
   - Verify images display correctly

---

## Phase 7: Contact Form Setup (30 minutes)

### 1. Set Up Email Delivery (SendGrid)

1. **Create SendGrid Account**
   - Go to: https://sendgrid.com
   - Sign up for free account (100 emails/day)
   - Verify email address
   - Complete account verification

2. **Generate API Key**
   - SendGrid Dashboard → Settings → API Keys
   - Click "Create API Key"
   - Name: "Hina Mirza Website"
   - Permissions: Full Access
   - Copy API key (save securely)

3. **Configure WP Mail SMTP**
   - WP Mail SMTP → Settings
   - Mailer: SendGrid
   - API Key: [Paste API key]
   - From Email: noreply@hinamirza.co
   - From Name: "Hina Mirza"
   - Click "Save Settings"
   - Send test email

### 2. Create Contact Forms

**General Contact Form:**
- Contact → Add New
- Form name: "General Contact"
- Paste form code:

```
<label> Your Name (required)
    [text* your-name class:form-control] </label>

<label> Your Email (required)
    [email* your-email class:form-control] </label>

<label> Subject
    [select inquiry-type "General Inquiry" "Collaboration Request" "Press/Media" "Other"] </label>

<label> Your Message
    [textarea* your-message class:form-control] </label>

[acceptance acceptance-privacy]
I agree to the privacy policy
[/acceptance]

[submit "Send"]
```

- Mail tab:
  - To: your@email.com
  - From: [your-name] <[your-email]>
  - Subject: New Contact: [inquiry-type]
  - Body: Keep default template
- Save form
- Copy shortcode

**Product Inquiry Form:**
- Contact → Add New
- Form name: "Product Inquiry"
- Similar to above, add hidden fields for product name/URL
- Save and copy shortcode

---

## Phase 8: Page Creation (1-2 hours)

### Create Essential Pages

1. **Home Page**
   - Pages → Add New
   - Title: "Home"
   - Use Blocksy blocks to create:
     - Hero section (cover block) with tagline
     - Portfolio highlights (query loop block)
     - Instagram feed (shortcode block)
     - About preview (paragraph block)
     - Contact CTA (button block)
   - Settings → Reading → Set as "Homepage"

2. **Portfolio Page**
   - Pages → Add New
   - Title: "Portfolio"
   - Add Query Loop block
   - Configure: Show posts from "Portfolio" category
   - Add filter controls (Blocksy filter blocks)
   - Enable grid layout (3 columns)

3. **Shop/Products Page**
   - Pages → Add New
   - Title: "Shop"
   - Similar to Portfolio, query "Products" category
   - Ensure inquiry buttons display

4. **About Page**
   - Pages → Add New
   - Title: "About"
   - Add bio text, artist photo
   - Add "If you'd like to collaborate, get in touch!"
   - Add contact form shortcode

5. **Contact Page**
   - Pages → Add New
   - Title: "Contact"
   - Add contact form shortcode
   - Add email: hina@hinamirza.co
   - Add social media links

### Create Menus

1. **Primary Menu**
   - Appearance → Menus
   - Create new menu: "Primary"
   - Add pages: Home, Portfolio, Shop, About, Contact
   - Set location: "Primary Menu"
   - Save

2. **Footer Menu (Optional)**
   - Create menu: "Footer"
   - Add: Privacy Policy, Terms
   - Assign to footer location

---

## Phase 9: Content Migration (2-3 hours if applicable)

### If Migrating from Existing WordPress Site

1. **Export Old Content**
   - Old site: Tools → Export
   - Select "All content"
   - Download XML file

2. **Import Content**
   - New site: Tools → Import
   - Install "WordPress Importer"
   - Upload XML file
   - Assign authors
   - Download and import attachments
   - Click "Submit"

3. **Migrate Images**
   - Old site: FTP download wp-content/uploads/
   - New site: FTP upload to wp-content/uploads/
   - Or use "All-in-One WP Migration" plugin

4. **Rebuild Page Layouts**
   - Old layouts (Elementor) won't transfer to Blocksy
   - Recreate pages using Gutenberg blocks
   - Reference screenshots from old site

5. **Recategorize Content**
   - Convert WooCommerce products → Portfolio/Products posts
   - Assign proper categories
   - Update custom fields

---

## Phase 10: Image Optimization (30 minutes)

1. **Configure ShortPixel**
   - ShortPixel → Settings
   - Compression: Glossy (best for artwork)
   - WebP: Enable
   - Create WebP versions: Yes
   - Optimize thumbnails: Yes
   - Backup originals: Yes (optional)

2. **Bulk Optimize Existing Images**
   - Media → Bulk ShortPixel
   - Click "Start Optimizing"
   - Wait for completion (can take 30-60 minutes)

3. **Test Optimization**
   - Check image sizes reduced
   - Verify quality maintained
   - Confirm WebP serving

---

## Phase 11: Final Configuration (30 minutes)

### WordPress Settings

1. **General Settings**
   - Site Title: "Hina Mirza"
   - Tagline: "Botanical Artwork & Design"
   - WordPress Address: https://hinamirza.co
   - Site Address: https://hinamirza.co
   - Timezone: Your timezone

2. **Reading Settings**
   - Homepage: Static page → "Home"
   - Posts page: "Blog" (if using)
   - Search engine visibility: Unchecked (allow indexing)

3. **Permalink Settings**
   - Structure: "Post name" (%postname%)
   - Click "Save Changes"

4. **Discussion Settings**
   - Disable comments (uncheck "Allow comments")

### Security & Performance

1. **User Roles**
   - Remove default "admin" user if exists
   - Use strong password
   - Enable two-factor authentication (optional)

2. **Wordfence Setup**
   - Run initial scan
   - Configure firewall (learning mode first)
   - Enable login security

3. **Backups**
   - Verify hosting backups enabled
   - Set up UpdraftPlus (optional plugin)
   - Schedule weekly backups

---

## Phase 12: Testing & Launch (1 hour)

### Pre-Launch Checklist

**Functionality Tests:**
- [ ] All pages load correctly
- [ ] Menu navigation works
- [ ] Instagram feed displays 12 posts
- [ ] Contact forms submit successfully
- [ ] Form emails arrive in inbox
- [ ] Product inquiry forms auto-fill product info
- [ ] Images load quickly and look sharp
- [ ] Mobile responsive on all pages

**Performance Tests:**
- [ ] Run PageSpeed Insights: https://pagespeed.web.dev/
  - Target: Mobile 80+, Desktop 90+
- [ ] Test on slow 3G connection
- [ ] Verify lazy loading works
- [ ] Check image optimization

**SEO Tests:**
- [ ] Meta titles set for all pages
- [ ] Meta descriptions set
- [ ] XML sitemap generated (Yoast)
- [ ] Robots.txt allows indexing
- [ ] Social media og:images set

**Security Tests:**
- [ ] SSL certificate active (https://)
- [ ] WordPress version updated
- [ ] All plugins updated
- [ ] Strong admin password
- [ ] Wordfence scan shows no issues

**Cross-Browser/Device Tests:**
- [ ] Chrome desktop
- [ ] Safari desktop
- [ ] Firefox desktop
- [ ] Chrome mobile (Android)
- [ ] Safari mobile (iOS)
- [ ] Tablet view

### Launch Steps

1. **Final Content Review**
   - Proofread all pages
   - Check for placeholder text
   - Verify all links work
   - Test all forms

2. **Go Live**
   - If on temporary URL: Point domain DNS
   - Update WordPress URLs if needed
   - Clear all caches
   - Test live site

3. **Post-Launch Monitoring**
   - Check email notifications working
   - Monitor error logs (first 24 hours)
   - Verify analytics tracking
   - Test Instagram feed updates

---

## Maintenance Schedule

### Daily (First Week)
- [ ] Check contact form submissions
- [ ] Monitor site uptime
- [ ] Review error logs

### Weekly
- [ ] Test contact form submission
- [ ] Check Instagram feed updates
- [ ] Review spam filter effectiveness
- [ ] Backup database manually

### Monthly
- [ ] Update WordPress core
- [ ] Update all plugins
- [ ] Update theme
- [ ] Review analytics
- [ ] Optimize database
- [ ] Check broken links
- [ ] Review security scan

### Quarterly
- [ ] Review hosting performance
- [ ] Audit SEO rankings
- [ ] Update content
- [ ] Review privacy policy accuracy
- [ ] Export full backup

---

## Troubleshooting Common Issues

### Site Not Loading
- Check DNS propagation: https://dnschecker.org/
- Verify hosting account active
- Clear browser cache
- Check .htaccess file permissions

### Instagram Feed Not Showing
- Verify account still Professional
- Reconnect Instagram account
- Clear WordPress cache
- Check plugin updated

### Contact Forms Not Sending
- Test WP Mail SMTP settings
- Check spam folder
- Verify SendGrid API key
- Review email logs

### Slow Performance
- Run PageSpeed Insights
- Optimize more images
- Enable caching plugin
- Check plugin bloat
- Contact hosting support

### Images Not Optimizing
- Verify ShortPixel API key
- Check credit balance (100/month)
- Manually optimize via Media Library
- Try re-uploading images

---

## Support Resources

### Documentation
- **WordPress:** https://wordpress.org/support/
- **Blocksy:** https://creativethemes.com/blocksy/docs/
- **Contact Form 7:** https://contactform7.com/docs/
- **ShortPixel:** https://shortpixel.com/knowledge-base

### Community Support
- **WordPress Forums:** https://wordpress.org/support/forums/
- **Blocksy Facebook Group:** Search "Blocksy Users"
- **YouTube Tutorials:** Search "[plugin name] tutorial"

### Hosting Support
- **Bluehost:** 24/7 phone/chat support
- **Hostinger:** 24/7 chat support

### Emergency Contacts
- Hosting support (for downtime)
- Domain registrar (for DNS issues)
- SendGrid support (for email delivery)

---

## Cost Summary

### One-Time Costs
| Item | Cost |
|------|------|
| Theme & plugins | $0 |
| Setup labor | DIY ($0) |
| Domain transfer | $0 (already owned) |
| **Total** | **$0** |

### Monthly Recurring
| Item | Cost |
|------|------|
| Hosting (Bluehost/Hostinger) | $3.99-$6.99 |
| SendGrid email | $0 (free tier) |
| ShortPixel optimization | $0 (free tier) |
| All plugins | $0 |
| **Total** | **$3.99-$6.99/month** |

### Annual Costs
| Item | Cost |
|------|------|
| Hosting | $48-$84/year |
| Domain renewal | ~$15/year |
| **Total** | **$63-$99/year** |

---

## Next Steps After Launch

1. **Week 1:** Monitor closely, fix any issues
2. **Week 2:** Start adding portfolio content
3. **Month 1:** Complete content migration
4. **Month 2:** SEO optimization and marketing
5. **Month 3:** Review analytics, optimize for conversions

**Congratulations! Your portfolio website is now live.** 🎉

For implementation tasks, run: `/speckit.tasks`
