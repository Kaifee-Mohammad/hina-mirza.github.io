# Hina Mirza Portfolio Website

A beautiful, fast portfolio website for designer Hina Mirza, built with Jekyll and hosted on GitHub Pages.

## Features

- 🎨 Portfolio showcase with category filtering
- 🛍️ Product listings with inquiry forms
- 📱 Fully responsive design
- ⚡ Fast static site generation
- 🔒 Contact forms via Netlify
- 📧 Easy content management

## Local Development

### Prerequisites

- Ruby 2.7 or higher
- Bundler

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hina-mirza.github.io.git
cd hina-mirza.github.io
```

2. Install dependencies:
```bash
bundle install
```

3. Run the development server:
```bash
bundle exec jekyll serve
```

4. Open your browser to `http://localhost:4000`

## Content Management

### Adding Portfolio Items

Create a new file in `_portfolio/` directory:

```markdown
---
layout: portfolio-item
title: "Your Artwork Title"
category: "Fabric" # or Wallpaper, Paintings, Home Goods
image: "/assets/images/portfolio/your-image.jpg"
featured: true # Shows on homepage
dimensions: "24 x 36 inches"
materials: "Watercolor on paper"
year: 2024
availability: "Available"
---

Your artwork description goes here.
```

### Adding Products

Create a new file in `_products/` directory:

```markdown
---
layout: product-item
title: "Product Name"
category: "Wallpaper"
image: "/assets/images/products/product-image.jpg"
price: "$500" # or "Contact for pricing"
sizes: "Custom sizes available"
materials: "Premium materials"
availability: "Made to order"
---

Product description goes here.
```

### Adding Images

Place images in:
- Portfolio: `assets/images/portfolio/`
- Products: `assets/images/products/`

Recommended image sizes:
- Portfolio/Product cards: 800x600px minimum
- Featured images: 1200x800px minimum

## Deployment

### GitHub Pages (Free)

1. Push to GitHub:
```bash
git add .
git commit -m "Initial portfolio website"
git push origin main
```

2. Enable GitHub Pages:
   - Go to repository Settings
   - Navigate to Pages
   - Source: Deploy from branch `main`
   - Folder: `/ (root)`
   - Click Save

3. Your site will be live at: `https://yourusername.github.io`

### Custom Domain (hinamirza.co)

1. Create a file named `CNAME` in the repository root with content:
```
hinamirza.co
```

2. In your domain registrar (where you bought hinamirza.co), add DNS records:
   - Type: A Record
   - Host: @
   - Value: 185.199.108.153
   - Add 3 more A records with: 185.199.109.153, 185.199.110.153, 185.199.111.153

3. Add CNAME record:
   - Type: CNAME
   - Host: www
   - Value: yourusername.github.io

4. Wait 24-48 hours for DNS propagation

## Content Management System (Optional)

For a visual CMS where your wife can manage content without editing files:

### Option 1: Netlify CMS (Recommended)

1. Sign up for Netlify (free)
2. Connect your GitHub repository
3. Enable Netlify Identity
4. Access CMS at: `yourdomain.com/admin/`

### Option 2: Forestry.io

1. Sign up at forestry.io
2. Import your GitHub repository
3. Configure content models
4. Invite your wife as an editor

## Site Structure

```
├── _config.yml          # Site configuration
├── _layouts/            # Page templates
├── _includes/           # Reusable components
├── _portfolio/          # Portfolio items
├── _products/           # Product listings
├── _sass/               # Styles
├── assets/
│   ├── css/            # Compiled CSS
│   ├── js/             # JavaScript
│   └── images/         # Image files
├── index.html          # Homepage
├── portfolio.html      # Portfolio page
├── shop.html           # Shop page
├── about.md            # About page
└── contact.md          # Contact page
```

## Technologies

- **Jekyll**: Static site generator
- **GitHub Pages**: Free hosting
- **Netlify Forms**: Contact form handling
- **Custom CSS**: No framework bloat
- **Vanilla JavaScript**: Lightweight interactions

## Performance

- Static site = Fast loading
- Optimized images
- Minimal JavaScript
- Mobile-first responsive design

## Support

For issues or questions, please contact: hina@hinamirza.co

## License

© 2025 Hina Mirza. All rights reserved.
