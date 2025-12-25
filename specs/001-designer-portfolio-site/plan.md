# Implementation Plan: Designer Portfolio Website Redesign

**Branch**: `001-designer-portfolio-site` | **Date**: 2025-12-25 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-designer-portfolio-site/spec.md`

## Summary

Build a fast, affordable WordPress-based portfolio website for designer Hina Mirza that she can manage independently. The site will showcase her botanical artwork portfolio, integrate Instagram feed, provide inquiry-based sales (no e-commerce), and maintain performance targets under 3 seconds load time on a budget under $10/month hosting.

**Primary Requirements**:
- WordPress CMS with visual page builder for non-technical content management
- Responsive portfolio gallery with category filtering
- Instagram integration (@hinamirza.art.design)
- Inquiry-based product listings (no shopping cart/checkout)
- Fast loading (<3s), mobile-optimized, SEO-friendly

**Technical Approach**: Lightweight WordPress setup with optimized theme, image optimization, and minimal plugins to maximize performance while minimizing costs.

## Technical Context

**Language/Version**: PHP 8.1+ (WordPress 6.4+)
**Primary Dependencies**:
- WordPress 6.4+ (CMS core)
- Lightweight theme (research needed: Astra Free, GeneratePress, Kadence)
- Visual page builder plugin (research needed: Elementor Free vs Gutenberg blocks)
- Instagram feed plugin (research needed: Smash Balloon vs alternatives)
- Image optimization plugin (research needed: ShortPixel, Imagify, EWWW)
- Contact form plugin (Contact Form 7, WPForms Lite, or Forminator)
- SEO plugin (Yoast SEO Free or Rank Math Free)

**Storage**: MySQL/MariaDB database (provided by hosting), filesystem for media library
**Testing**: Manual UAT for content management workflows, browser testing (Chrome, Safari, Firefox, mobile devices), PageSpeed Insights for performance validation
**Target Platform**: Shared hosting (LAMP stack), WordPress-compatible, cPanel or equivalent
**Project Type**: Web application (WordPress installation)
**Performance Goals**:
- Homepage load <3 seconds on broadband
- Google PageSpeed score 80+ mobile, 90+ desktop
- Optimized images <500KB each
- Lazy loading for below-fold content

**Constraints**:
- Budget: <$10/month hosting, <$100 one-time theme cost (prefer free)
- No custom code/plugin development (configuration only)
- Must be manageable by non-technical user
- No e-commerce/payment processing
- Must maintain existing domain (hinamirza.co)

**Scale/Scope**:
- Initial: ~50-100 portfolio items, ~20-30 product listings
- Traffic: <1000 visitors/month initially
- Inquiries: <50/month
- Single admin user (Hina)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Note**: No project-specific constitution file found. Using WordPress and web development best practices:

✓ **Simplicity**: Use WordPress core features and established plugins rather than custom development
✓ **Performance**: Image optimization, caching, lazy loading, minimal plugin footprint
✓ **Maintainability**: Well-supported themes/plugins with regular updates, no orphaned dependencies
✓ **Security**: HTTPS, regular WordPress updates, minimal plugin surface area, reputable sources only
✓ **User-Centered**: Visual editor for non-technical management, intuitive admin interface
✓ **Cost-Effective**: Free/open-source components, affordable hosting, no ongoing developer costs

**No violations to justify.**

## Project Structure

### Documentation (this feature)

```text
specs/001-designer-portfolio-site/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
├── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
├── checklists/          # Quality validation checklists
│   └── requirements.md  # Specification quality checklist
└── research/            # Background research and content inventory
    └── content-inventory.md
```

### Source Code (repository root)

This is a WordPress installation project, not a custom codebase. The structure will be:

```text
# WordPress Installation Structure (on hosting server)
wordpress/
├── wp-content/
│   ├── themes/
│   │   └── [selected-theme]/     # Lightweight portfolio theme
│   ├── plugins/
│   │   ├── elementor/             # Visual page builder (if selected)
│   │   ├── instagram-feed/        # Instagram integration
│   │   ├── contact-form-7/        # Contact forms
│   │   ├── shortpixel/            # Image optimization
│   │   └── yoast-seo/             # SEO optimization
│   └── uploads/                   # Media library (images)
├── wp-config.php                  # Configuration
└── [WordPress core files]

# GitHub Repository (configuration tracking)
hina-mirza.github.io/
├── specs/                         # This planning documentation
├── config/                        # Exported configuration files
│   ├── theme-settings.json        # Theme customizer export
│   ├── plugins-list.txt           # Installed plugins list
│   └── content-backup/            # WordPress XML exports
└── assets/                        # Design assets for migration
    ├── logos/
    ├── images/
    └── content/
```

**Structure Decision**: This is a WordPress installation project, not custom application development. The GitHub repository will track configuration, documentation, and backups, but the actual WordPress installation lives on the hosting server. Configuration-as-code approach where possible using exports and documentation.

## Complexity Tracking

**No complexity violations** - This project follows WordPress standard practices using established themes and plugins. No custom development, frameworks, or architectural patterns that require justification.

## Phase 0: Research (Next)

**Objectives**: Resolve all technical unknowns and select specific technologies

**Research Tasks**:
1. WordPress theme selection (Astra Free vs GeneratePress vs Kadence vs others)
2. Page builder selection (Elementor Free vs Gutenberg blocks vs alternatives)
3. Instagram feed plugin comparison (Smash Balloon vs Spotlight vs Feed Them Social)
4. Image optimization plugin evaluation (ShortPixel vs Imagify vs EWWW)
5. Hosting provider comparison (budget <$10/month, WordPress-optimized)
6. Domain migration process for hinamirza.co
7. Content migration strategy from existing WordPress site

**Output**: `research.md` with technology selections and rationale

## Phase 1: Design & Contracts (After Research)

**Objectives**: Define data structures, page layouts, and integration contracts

**Deliverables**:
1. **data-model.md**: WordPress content types and taxonomy structure
   - Custom Post Types (Portfolio Items, Products)
   - Taxonomies (Categories: Fabric, Wallpaper, Paintings, Home Goods)
   - Custom Fields (pricing, dimensions, availability, materials)
   - User roles and permissions

2. **contracts/**: Integration specifications
   - Instagram API/embed integration contract
   - Contact form to email contract
   - Image optimization pipeline
   - Analytics integration (Google Analytics or alternative)

3. **quickstart.md**: Setup and deployment guide
   - Hosting account setup
   - WordPress installation steps
   - Theme and plugin installation sequence
   - Initial configuration checklist
   - Content migration procedures
   - DNS configuration for hinamirza.co

**Output**: Complete technical specifications ready for implementation

## Phase 2: Task Generation (Separate Command)

**Not included in this plan** - Run `/speckit.tasks` after plan approval to generate actionable implementation tasks.

## Next Steps

1. Review and approve this implementation plan
2. Execute Phase 0 research to select specific technologies
3. Complete Phase 1 design with data models and contracts
4. Generate tasks with `/speckit.tasks` command
5. Begin implementation

**Estimated Timeline**: 2-4 weeks from approval to launch
**Budget**: $0-60 one-time setup (optional premium theme), $5-10/month hosting
