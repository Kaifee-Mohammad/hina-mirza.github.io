# Implementation Plan: Instagram Live Feed Page

**Branch**: `002-instagram-feed` | **Date**: 2025-12-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-instagram-feed/spec.md`

## Summary

Add a dedicated Instagram feed page to the Hina Mirza portfolio website that displays the 12 most recent Instagram posts in a responsive grid layout. The feature uses third-party Instagram embed widgets (Behold or Elfsight) to eliminate API token management while maintaining compliance with Instagram's Terms of Service. The page will be accessible via site navigation, follow the "Minimize Scrolling" principle with compact layouts, and allow CMS configuration of the Instagram username.

**Technical Approach**: Integrate a third-party embed widget service with Jekyll static site, add navigation link, create dedicated Instagram page, style to match existing portfolio design, and add CMS configuration options.

## Technical Context

**Language/Version**: Ruby 3.2.2, Jekyll 3.10.0 (static site generator)
**Primary Dependencies**:
- Jekyll (static site generation)
- Netlify CMS (content management)
- Third-party embed widget: Behold ($10/month recommended) or Elfsight (free/$5/month alternative)
- Existing SASS styling framework (_variables.scss, _components.scss, _pages.scss, _responsive.scss)

**Storage**: N/A (static HTML generation; Instagram content hosted by embed service)
**Testing**: Manual UI testing (scripts/ui_test.sh) + visual regression testing
**Target Platform**: Static HTML/CSS/JS hosted on Netlify, responsive 320px-1920px
**Project Type**: Jekyll static site (existing structure: _layouts, _includes, _sass, assets)
**Performance Goals**:
- Page load <2 seconds
- Instagram feed renders within 2 seconds
- Lazy loading for Instagram images
- Minimal JavaScript overhead

**Constraints**:
- Must follow "Minimize Scrolling" principle (6 posts visible desktop, 4 mobile)
- Visual consistency with peachy accent #d8c3be
- Compact spacing (8-16px vertical padding)
- No direct Instagram API integration (use embed widgets)
- Must work without JavaScript fallback message

**Scale/Scope**:
- Single Instagram feed page
- 12 posts displayed
- ~3-5 new files (instagram.md, _includes/instagram-feed.html, _sass/_instagram.scss, CMS config update)
- Integrates with existing navigation (4 nav items → 5)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ Constitution Compliance

**I. Minimize Scrolling (NON-NEGOTIABLE)**
- ✅ Grid layout shows 6 posts on desktop, 4 on mobile without scrolling (FR-007, SC-004)
- ✅ Compact layouts with minimal padding (following spacing guidelines 8-16px)
- ✅ Efficient use of horizontal space with responsive grid

**II. Visual Simplicity**
- ✅ Maintains peachy accent color #d8c3be (FR-006)
- ✅ Consistent typography (Libre Baskerville + Montserrat)
- ✅ Minimal UI elements, clean grid layout
- ✅ White space used intentionally for grid gaps

**III. Mobile-First Responsive**
- ✅ Responsive design 320px-1920px (FR-008, SC-002)
- ✅ Touch-friendly post interactions (P2 user story)
- ✅ Adapt grid columns based on viewport

**IV. Performance First**
- ✅ Lazy loading Instagram images (FR-010)
- ✅ <2 second page load target (SC-001)
- ✅ Minimal external dependencies (single embed widget script)
- ✅ Static site generation maintains fast base performance

**V. CMS Accessibility**
- ✅ Hina can configure Instagram username via Netlify CMS (FR-012, SC-006)
- ✅ Toggle display on/off without code changes (P3 user story)
- ✅ Simple workflow for configuration

**Development Workflow**
- ✅ Test at all breakpoints before committing
- ✅ Check for excessive scrolling
- ✅ Run UI test suite (scripts/ui_test.sh)
- ✅ Verify mobile responsiveness

### No Constitution Violations

All requirements align with established principles. No complexity justification needed.

## Project Structure

### Documentation (this feature)

```text
specs/002-instagram-feed/
├── spec.md              # Feature specification ✅ Complete
├── plan.md              # This file (implementation plan) ✅ In Progress
├── research.md          # Phase 0 research on embed widgets ✅ Complete
├── data-model.md        # Phase 1 data structures (minimal - config only)
├── quickstart.md        # Phase 1 setup guide for developers
├── contracts/           # Phase 1 CMS configuration schema
│   └── cms-config.yml   # Netlify CMS Instagram settings
└── checklists/
    └── requirements.md  # Spec quality checklist ✅ Complete
```

### Source Code (repository root)

This is a Jekyll static site with the following existing structure:

```text
hina-mirza.github.io/
├── _config.yml                    # Jekyll configuration
├── _includes/                     # Reusable HTML components
│   ├── header.html               # Site navigation (UPDATE: add Instagram link)
│   ├── footer.html               # Site footer
│   └── instagram-feed.html       # NEW: Instagram embed widget wrapper
├── _layouts/                      # Page templates
│   └── default.html              # Base layout (existing, no changes)
├── _sass/                         # SASS stylesheets
│   ├── _variables.scss           # Color/spacing variables (existing)
│   ├── _base.scss                # Base styles (existing)
│   ├── _layout.scss              # Layout components (existing)
│   ├── _components.scss          # UI components (existing)
│   ├── _pages.scss               # Page-specific styles (UPDATE: add Instagram)
│   └── _responsive.scss          # Media queries (UPDATE: Instagram responsive)
├── assets/
│   ├── css/
│   │   └── main.scss             # Main stylesheet entry point
│   ├── js/
│   │   └── main.js               # Existing JavaScript (no changes for basic embed)
│   └── images/                    # Static images (no changes)
├── admin/
│   ├── config.yml                # Netlify CMS config (UPDATE: add Instagram settings)
│   └── index.html                # CMS interface (existing)
├── _data/                         # NEW (if needed)
│   └── instagram.yml             # Instagram configuration data file
├── instagram.md                   # NEW: Instagram feed page
├── index.html                     # Homepage (UPDATE: add Instagram CTA optional)
├── contact.md                     # Existing page (no changes)
├── about.md                       # Existing page (no changes)
├── portfolio.html                 # Existing page (no changes)
├── prints.html                    # Existing page (no changes)
└── scripts/
    ├── ui_test.sh                # UI test suite (UPDATE: add Instagram page tests)
    └── ui_test.py                # Python test runner (UPDATE: add Instagram tests)
```

**Structure Decision**: Jekyll static site with modular SCSS architecture. New Instagram page follows existing pattern: markdown file (instagram.md) + include (_includes/instagram-feed.html) + page-specific styles (_sass/_pages.scss addition). This maintains consistency with portfolio.html and prints.html implementations.

## Phase 0: Research (✅ Complete)

### Research Findings

**Decision**: Use **Behold** ($10/month Starter plan) as primary recommendation, with **Elfsight** (free/$5/month) as fallback option.

**Rationale**:
- Behold is specifically optimized for JAMstack/static sites like Jekyll
- Eliminates need for Instagram API token management
- Compliant with Instagram Terms of Service (uses official APIs under the hood)
- Free tier available for testing (1,200 views/month)
- $10/month Starter plan provides 15,000 views/month, hourly updates, no branding
- Simple JavaScript embed code integration
- Excellent customization options for grid layout
- Netlify-compatible (no special configuration needed)

**Alternatives Considered**:
1. **Elfsight** ($0-$5/month) - Best free tier, lowest paid option, excellent for budget-conscious users
2. **LightWidget** ($15 one-time) - Simplest setup, one-time payment vs subscription
3. **DIY Build-Time Generation** - Best performance but requires Instagram Business account, complex setup, ongoing maintenance
4. **Instagram Native Embeds** - Rejected: only supports single posts, not grid layout

**Implementation Approach**:
1. Sign up for Behold (or Elfsight as alternative)
2. Connect Instagram account via OAuth (one-time setup)
3. Configure widget: grid layout, 12 posts, custom styling to match site
4. Copy embed code (JavaScript snippet)
5. Create Jekyll include file with embed code
6. Style grid to follow constitution principles
7. Add to new Instagram page

**Key Insight**: Instagram's Basic Display API was deprecated December 2025, so all solutions require some form of authentication. Third-party services handle this complexity, making them the practical choice for static sites.

**Full research documentation**: [research.md](./research.md)

## Phase 1: Design & Data Model

### Data Model

Since this feature uses an external embed widget service, the data model is minimal. Instagram post data is fetched and rendered by the third-party service.

**Local Configuration Data** (stored in _data/instagram.yml):

```yaml
# Instagram feed configuration
username: "hinamirza_art"       # Instagram handle
display_enabled: true            # Toggle feed visibility
posts_count: 12                  # Number of posts to display
widget_service: "behold"         # Service name: behold, elfsight, lightwidget
widget_id: "YOUR_WIDGET_ID"      # Embed widget ID from service
```

**CMS-Managed Fields** (via Netlify CMS):

- **Instagram Username** (string, required) - Instagram handle to display
- **Display Feed** (boolean, default: true) - Toggle feed visibility site-wide
- **Widget Service** (select: behold|elfsight|lightwidget) - Which service is configured
- **Widget Embed ID** (string, required) - Unique ID from embed service

**Instagram Post Entity** (managed by external service, displayed via widget):
- Image URL
- Caption excerpt
- Post date
- Permalink to Instagram

This minimal data model avoids duplicating Instagram's data and leverages the embed service as the source of truth.

### Design Specifications

**Page Layout** (instagram.md):

```markdown
---
layout: default
title: Instagram
permalink: /instagram/
show_instagram: true
---

<div class="instagram-page">
  <header class="page-header compact">
    <h1>Latest on Instagram</h1>
    <p class="subtitle">Follow along for works in progress, behind-the-scenes, and inspiration</p>
  </header>

  <div class="instagram-content">
    {% if site.data.instagram.display_enabled %}
      {% include instagram-feed.html %}
    {% else %}
      <p class="feed-disabled">Instagram feed is currently unavailable.</p>
    {% endif %}
  </div>
</div>
```

**Instagram Feed Include** (_includes/instagram-feed.html):

```html
<div class="instagram-feed-wrapper">
  {% if site.data.instagram.widget_service == 'behold' %}
    <!-- Behold embed -->
    <div id="behold-feed" data-feed-id="{{ site.data.instagram.widget_id }}"></div>
    <script src="https://behold.so/{{ site.data.instagram.widget_id }}/embed.js" async defer></script>

  {% elsif site.data.instagram.widget_service == 'elfsight' %}
    <!-- Elfsight embed -->
    <div class="elfsight-app-{{ site.data.instagram.widget_id }}"></div>
    <script src="https://apps.elfsight.com/p/platform.js" async defer></script>

  {% elsif site.data.instagram.widget_service == 'lightwidget' %}
    <!-- LightWidget embed -->
    <iframe src="https://cdn.lightwidget.com/widgets/{{ site.data.instagram.widget_id }}.html"
            scrolling="no"
            allowtransparency="true"
            class="lightwidget-widget"
            style="width:100%;border:0;overflow:hidden;"></iframe>
  {% endif %}

  <noscript>
    <p class="no-js-message">
      Please enable JavaScript to view the Instagram feed, or
      <a href="https://instagram.com/{{ site.data.instagram.username }}" target="_blank" rel="noopener">
        visit @{{ site.data.instagram.username }} on Instagram
      </a>
    </p>
  </noscript>
</div>
```

**Styling Specifications** (_sass/_pages.scss addition):

```scss
// Instagram Page
.instagram-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 $spacing-md $spacing-md;

  .page-header.compact {
    padding: $spacing-sm 0;
    text-align: center;
    margin-bottom: $spacing-md;

    h1 {
      font-size: 2rem;
      margin-bottom: $spacing-xs;
    }

    .subtitle {
      font-size: 0.95rem;
      color: $text-secondary;
      margin: 0;
    }
  }

  .instagram-content {
    width: 100%;
  }

  .feed-disabled,
  .no-js-message {
    text-align: center;
    padding: $spacing-lg;
    background: $light-gray;
    border-radius: 4px;
    font-size: 0.95rem;
    color: $text-secondary;

    a {
      color: $primary-color;
      text-decoration: underline;
    }
  }
}

// Instagram Feed Widget Wrapper
.instagram-feed-wrapper {
  width: 100%;

  // Grid layout styling (applied to widget container)
  #behold-feed,
  .elfsight-app,
  .lightwidget-widget {
    width: 100%;
    min-height: 400px; // Prevent layout shift while loading
  }

  // Override widget styles to match site design
  :global {
    // Customize widget appearance to match peachy theme
    .behold-grid-item,
    .elfsight-widget-instagram-feed,
    .lightwidget-grid-item {
      border-radius: 4px;
      transition: transform 0.3s ease;

      &:hover {
        transform: scale(1.02);
      }
    }
  }
}

// Mobile responsive
@media (max-width: $tablet) {
  .instagram-page {
    .page-header.compact h1 {
      font-size: 1.75rem;
    }
  }
}

@media (max-width: $mobile) {
  .instagram-page {
    padding: 0 $spacing-sm $spacing-sm;

    .page-header.compact h1 {
      font-size: 1.5rem;
    }
  }
}
```

**Navigation Update** (_includes/header.html):

Add Instagram link to navigation menu:

```html
<nav class="site-nav">
  <ul>
    <li><a href="{{ '/' | relative_url }}">Home</a></li>
    <li><a href="{{ '/portfolio/' | relative_url }}">Portfolio</a></li>
    <li><a href="{{ '/prints/' | relative_url }}">Art Prints</a></li>
    <li><a href="{{ '/instagram/' | relative_url }}">Instagram</a></li>  <!-- NEW -->
    <li><a href="{{ '/about/' | relative_url }}">About</a></li>
    <li><a href="{{ '/contact/' | relative_url }}">Contact</a></li>
  </ul>
</nav>
```

### CMS Configuration

**Netlify CMS Update** (admin/config.yml):

```yaml
# Add Instagram settings collection
collections:
  - name: "settings"
    label: "Site Settings"
    files:
      - label: "Instagram Feed"
        name: "instagram"
        file: "_data/instagram.yml"
        fields:
          - {label: "Instagram Username", name: "username", widget: "string", required: true, hint: "Your Instagram handle (without @)"}
          - {label: "Display Feed", name: "display_enabled", widget: "boolean", default: true, hint: "Show/hide Instagram feed on the site"}
          - {label: "Number of Posts", name: "posts_count", widget: "number", default: 12, min: 6, max: 24, hint: "How many posts to display (6-24)"}
          - {label: "Widget Service", name: "widget_service", widget: "select", options: ["behold", "elfsight", "lightwidget"], default: "behold", hint: "Which embed service you configured"}
          - {label: "Widget ID", name: "widget_id", widget: "string", required: true, hint: "Embed ID from your widget service dashboard"}
```

## Testing Strategy

**UI Tests to Add** (scripts/ui_test.sh):

```bash
# Test 18: Instagram page exists and loads
test_instagram_page_loads() {
  check_page "/instagram/" "Instagram page"
}

# Test 19: Instagram navigation link present
test_instagram_nav_link() {
  check_element "nav a[href*='instagram']" "Instagram nav link"
}

# Test 20: Instagram feed container exists
test_instagram_feed_container() {
  check_page_element "/instagram/" ".instagram-feed-wrapper" "Instagram feed container"
}

# Test 21: NoScript fallback message
test_instagram_noscript() {
  check_page_element "/instagram/" "noscript" "Instagram noscript fallback"
}

# Test 22: Page header compact styling
test_instagram_header_compact() {
  check_page_element "/instagram/" ".page-header.compact" "Compact page header"
}

# Test 23: Mobile responsive (320px)
test_instagram_mobile() {
  check_responsive "/instagram/" 320 "Instagram mobile view"
}

# Test 24: Tablet responsive (768px)
test_instagram_tablet() {
  check_responsive "/instagram/" 768 "Instagram tablet view"
}

# Test 25: Desktop responsive (1920px)
test_instagram_desktop() {
  check_responsive "/instagram/" 1920 "Instagram desktop view"
}
```

**Manual Testing Checklist**:
- [ ] Instagram page loads at /instagram/
- [ ] Navigation includes Instagram link
- [ ] Widget displays 12 posts in grid
- [ ] Posts are clickable and open Instagram in new tab
- [ ] Grid is responsive (6 columns desktop → 3 tablet → 2 mobile)
- [ ] Page follows "Minimize Scrolling" principle (6 posts visible desktop)
- [ ] Visual consistency with portfolio page
- [ ] CMS settings work (username change reflects on site)
- [ ] NoScript fallback message displays when JS disabled
- [ ] Performance: page loads <2 seconds
- [ ] All 25 UI tests pass

## Implementation Phases

### Phase 2: Tasks Generation (Next Step)

After this planning phase, run `/speckit.tasks` to generate dependency-ordered task list based on:

**Priority 1 (P1) - Core Functionality**:
1. Set up embed widget service account (Behold/Elfsight)
2. Create _data/instagram.yml configuration file
3. Create instagram.md page
4. Create _includes/instagram-feed.html include
5. Add Instagram styles to _sass/_pages.scss
6. Update navigation in _includes/header.html
7. Test basic page load and widget display

**Priority 2 (P2) - Navigation & Responsive**:
8. Add responsive styles to _sass/_responsive.scss
9. Update CMS configuration (admin/config.yml)
10. Add UI tests to scripts/ui_test.sh
11. Test all breakpoints (320px, 768px, 1920px)
12. Verify minimal scrolling compliance

**Priority 3 (P3) - CMS & Polish**:
13. Test CMS Instagram settings functionality
14. Add homepage Instagram CTA (optional)
15. Performance optimization (lazy loading verification)
16. Final visual regression testing
17. Documentation updates (README, CMS guide)

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Third-party widget service downtime | High - feed unavailable | Implement NoScript fallback with Instagram link, consider DIY build-time generation as backup |
| Widget doesn't match site design | Medium - visual inconsistency | Use Behold's extensive customization options, apply CSS overrides if needed |
| Instagram API policy changes | High - widget stops working | Stay informed on Instagram Platform Policy updates, service provider handles API changes |
| Widget slows page load | Medium - performance impact | Lazy load widget below fold, use async script loading, monitor Core Web Vitals |
| Free tier view limits exceeded | Low - free tier caps at 1,200 views/month | Upgrade to $10/month Starter plan (15,000 views) or use Elfsight free tier |
| CMS configuration errors | Low - user mistakes | Clear field hints in CMS, validation rules, setup documentation |

## Next Steps

1. ✅ **Phase 0 Complete**: Research embed widget solutions
2. ✅ **Phase 1 Complete**: Design data model, page layouts, and contracts
3. **Phase 2**: Run `/speckit.tasks` to generate detailed implementation tasks
4. **Phase 3**: Execute tasks in priority order (P1 → P2 → P3)
5. **Phase 4**: Test, validate against constitution, deploy to Netlify

## Success Metrics

Implementation will be considered successful when:

- ✅ Instagram page loads at /instagram/ with 12 posts in grid layout
- ✅ Page accessible from navigation menu on all pages
- ✅ Responsive design works 320px-1920px (all tests pass)
- ✅ Minimal scrolling: 6 posts visible desktop, 4 mobile
- ✅ Page load time <2 seconds
- ✅ Widget renders within 2 seconds
- ✅ Visual consistency with portfolio page (peachy accent, typography)
- ✅ CMS settings functional (username change updates site within 2 minutes)
- ✅ All 25 UI tests pass
- ✅ NoScript fallback works correctly
- ✅ Constitution compliance verified

---

**Plan Status**: ✅ Phase 1 Complete - Ready for Task Generation
**Next Command**: `/speckit.tasks`
**Branch**: `002-instagram-feed`
**Estimated Implementation Time**: 4-6 hours (assuming embed widget account already set up)
