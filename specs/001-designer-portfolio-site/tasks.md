# Tasks: Designer Portfolio Website Redesign

**Input**: Design documents from `/specs/001-designer-portfolio-site/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: This is a WordPress configuration project (no custom code), so tests are manual UAT/browser testing, not automated unit tests.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different configurations, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- WordPress admin paths noted where applicable

## Path Conventions

This is a WordPress installation project. Paths refer to:
- WordPress Admin: `/wp-admin/` (web interface)
- Theme files: `wp-content/themes/blocksy/`
- Plugin configs: WordPress admin settings pages
- Content: Created via WordPress admin (Posts, Pages, Media)

---

## Phase 1: Setup & Hosting (Infrastructure)

**Purpose**: Establish hosting environment and WordPress foundation

- [ ] T001 Sign up for hosting account (Bluehost Essentials $6.99/mo or Hostinger Business WordPress $3.99/mo)
- [ ] T002 Configure domain DNS settings to point hinamirza.co to new hosting nameservers
- [ ] T003 Install WordPress 6.4+ via hosting control panel one-click installer
- [ ] T004 Enable SSL certificate (Let's Encrypt) via hosting control panel
- [ ] T005 Install and activate Really Simple SSL plugin to force HTTPS sitewide
- [ ] T006 [P] Set WordPress permalink structure to "Post name" in Settings → Permalinks
- [ ] T007 [P] Configure WordPress timezone and site details in Settings → General
- [ ] T008 [P] Disable comments sitewide in Settings → Discussion
- [ ] T009 Create secure admin account with strong password (replace default if needed)

**Checkpoint**: WordPress accessible at https://hinamirza.co/wp-admin/

---

## Phase 2: Foundational (Theme & Essential Plugins)

**Purpose**: Install core theme and plugins that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T010 Install and activate Blocksy Free theme from Appearance → Themes → Add New
- [ ] T011 Configure Blocksy theme via Appearance → Customize (site identity, logo upload, colors: #d8c3be accent, #3a3a3a text, #ffffff background)
- [ ] T012 Set typography in Blocksy customizer (Libre Baskerville headings, Montserrat body)
- [ ] T013 [P] Install and activate Smash Balloon Social Photo Feed plugin for Instagram integration
- [ ] T014 [P] Install and activate ShortPixel Image Optimizer plugin for image optimization
- [ ] T015 [P] Install and activate Contact Form 7 plugin for contact forms
- [ ] T016 [P] Install and activate Contact Form CFDB7 plugin for form submission backup
- [ ] T017 [P] Install and activate WP Mail SMTP plugin for email delivery
- [ ] T018 [P] Install and activate Yoast SEO Free plugin for SEO optimization
- [ ] T019 [P] Install and activate Wordfence Security plugin (optional but recommended)
- [ ] T020 Delete unnecessary default plugins (Hello Dolly, etc.)
- [ ] T021 Run Yoast SEO configuration wizard in SEO → General
- [ ] T022 Run Wordfence initial security scan in Wordfence → Scan

**Checkpoint**: Foundation ready - all plugins activated, theme configured, ready for content

---

## Phase 3: User Story 1 - Website Content Management (Priority: P1) 🎯 MVP

**Goal**: Enable Hina to independently add, edit, and publish portfolio content using visual editor

**Independent Test**: Hina logs into WordPress admin, creates a new post with Portfolio category, uploads images via Gutenberg blocks, publishes it, and verifies it appears on the site without developer help. All image optimization happens automatically.

### Implementation for User Story 1

- [ ] T023 [P] [US1] Configure ShortPixel plugin: sign up for free account (100 credits/month) in ShortPixel → Settings
- [ ] T024 [P] [US1] Set ShortPixel compression to "Glossy" mode for artwork preservation in ShortPixel → Settings
- [ ] T025 [P] [US1] Enable WebP image format conversion in ShortPixel → Settings → Advanced
- [ ] T026 [P] [US1] Create Portfolio category in Posts → Categories (slug: portfolio)
- [ ] T027 [P] [US1] Create Products category in Posts → Categories (slug: products)
- [ ] T028 [P] [US1] Create taxonomy subcategories under Portfolio: Fabric, Wallpaper, Paintings, Home Goods
- [ ] T029 [US1] Create test portfolio post using Gutenberg blocks: add title, gallery block with images, description
- [ ] T030 [US1] Assign test post to Portfolio → Fabric category and publish
- [ ] T031 [US1] Verify ShortPixel automatically optimizes uploaded images (check Media Library for optimization status)
- [ ] T032 [US1] Test editing published post: update text, add image, republish - verify changes appear immediately
- [ ] T033 [US1] Bulk optimize any existing images via Media → Bulk ShortPixel
- [ ] T034 [US1] Configure WordPress media settings: thumbnail size 300x300, medium 768x768, large 1200x1200

**Checkpoint**: Hina can independently create, edit, and publish portfolio items with automatic image optimization. Test by creating 2-3 sample portfolio posts.

---

## Phase 4: User Story 2 - Portfolio Showcase (Priority: P1) 🎯 MVP

**Goal**: Create beautiful portfolio gallery page with category filtering and mobile responsiveness

**Independent Test**: Visit homepage and portfolio page, verify artwork displays in attractive grid (3 col desktop, 2 col mobile), images load fast, category filters work, lightbox opens on click, mobile touch navigation smooth.

### Implementation for User Story 2

- [ ] T035 [US2] Create Portfolio page: Pages → Add New, title "Portfolio"
- [ ] T036 [US2] Add Query Loop block to Portfolio page, configure to show posts from Portfolio category
- [ ] T037 [US2] Configure Query Loop layout: grid view, 3 columns desktop, 2 columns mobile, featured image prominent
- [ ] T038 [US2] Add Blocksy filter controls above Query Loop for category filtering (Fabric, Wallpaper, Paintings, Home Goods)
- [ ] T039 [US2] Enable Blocksy lightbox feature for portfolio images in Customizer → General → Lightbox
- [ ] T040 [US2] Configure lazy loading for images in Blocksy → Performance
- [ ] T041 [US2] Create Homepage: Pages → Add New, title "Home"
- [ ] T042 [US2] Add Cover block to Homepage for hero section with tagline "ELEGANT . SOFT . PAINTERLY"
- [ ] T043 [US2] Add Query Loop to Homepage showing 6-8 featured portfolio items (most recent from Portfolio category)
- [ ] T044 [US2] Set Homepage as static front page in Settings → Reading → Homepage: "Home"
- [ ] T045 [US2] Create and assign Primary navigation menu in Appearance → Menus (Home, Portfolio, Shop, About, Contact)
- [ ] T046 [US2] Test portfolio page on desktop: verify 3-column grid, images load <3 seconds, category filter works
- [ ] T047 [US2] Test portfolio page on mobile: verify 2-column responsive layout, touch navigation, lightbox

**Checkpoint**: Portfolio gallery displays beautifully with filtering, mobile responsive, fast loading. Visitors can browse artwork easily.

---

## Phase 5: User Story 3 - Instagram Integration (Priority: P2)

**Goal**: Display latest Instagram posts from @hinamirza.art.design automatically on website

**Independent Test**: Visit homepage or Instagram section, verify 12 recent Instagram posts display in grid, links open Instagram in new tab, feed auto-updates within 6 hours without manual intervention.

### Implementation for User Story 3

- [ ] T048 [US3] Connect Instagram account: Instagram Feed → Settings → Connect Instagram Account
- [ ] T049 [US3] Log in to Instagram with @hinamirza.art.design credentials (must be Professional account)
- [ ] T050 [US3] Grant Smash Balloon read-only permissions and verify connection successful
- [ ] T051 [US3] Configure feed display in Instagram Feed → Settings: 12 posts, grid layout, 3 columns desktop, 2 mobile
- [ ] T052 [US3] Set cache refresh interval to 6 hours in Instagram Feed → Settings → Advanced
- [ ] T053 [US3] Enable "Show follow button" and disable "Show header" in Instagram Feed → Settings → General
- [ ] T054 [US3] Copy Instagram feed shortcode: [instagram-feed]
- [ ] T055 [US3] Add Instagram feed to Homepage: insert Shortcode block below portfolio highlights, paste [instagram-feed]
- [ ] T056 [US3] Add heading "Latest from Instagram" above feed using Heading block
- [ ] T057 [US3] Test Instagram feed on homepage: verify 12 posts display, grid layout, images load properly
- [ ] T058 [US3] Test Instagram post click: verify opens original Instagram post in new tab
- [ ] T059 [US3] Verify feed caching working: check Instagram Feed → Settings → Feeds → View cached data

**Checkpoint**: Instagram feed displays 12 recent posts automatically, no manual updates needed, graceful fallback if API fails.

---

## Phase 6: User Story 4 - Product/Artwork Sales (Priority: P2)

**Goal**: Enable inquiry-based sales with product listings and contact forms for purchase inquiries

**Independent Test**: Browse products page, click product, see pricing and "Inquire About This Item" button, submit inquiry form with auto-filled product details, verify Hina receives email with product reference and customer contact info.

### Implementation for User Story 4

- [ ] T060 [US4] Sign up for SendGrid free account (100 emails/day) at https://sendgrid.com
- [ ] T061 [US4] Generate SendGrid API key: SendGrid Dashboard → Settings → API Keys → Create API Key
- [ ] T062 [US4] Configure WP Mail SMTP: Settings → WP Mail SMTP, select SendGrid mailer, enter API key
- [ ] T063 [US4] Set From Email to noreply@hinamirza.co and From Name to "Hina Mirza" in WP Mail SMTP settings
- [ ] T064 [US4] Send test email via WP Mail SMTP → Tools → Email Test to verify email delivery working
- [ ] T065 [US4] Create general contact form in Contact → Add New: fields for name, email, subject dropdown, message, privacy consent checkbox
- [ ] T066 [US4] Configure general contact form email settings: To: hina@hinamirza.co, Subject: "New Contact: [inquiry-type]"
- [ ] T067 [US4] Create product inquiry form in Contact → Add New: name, email, optional phone, hidden product name field, message, consent
- [ ] T068 [US4] Configure product inquiry form email template to include product name and URL in email body
- [ ] T069 [US4] Set up reCAPTCHA v3 for spam prevention: get keys from Google reCAPTCHA, add to Contact Form 7 Integration settings
- [ ] T070 [US4] Create Shop/Products page: Pages → Add New, title "Shop"
- [ ] T071 [US4] Add Query Loop to Shop page showing posts from Products category with featured images, titles, excerpts
- [ ] T072 [US4] Create sample product post: add title, images, description, price (text field), size options, materials
- [ ] T073 [US4] Add "Inquire About This Item" button block to product post template, link to product inquiry form shortcode
- [ ] T074 [US4] Test product inquiry flow end-to-end: click product, fill form, submit, verify email arrives at hina@hinamirza.co
- [ ] T075 [US4] Verify product inquiry email includes product name, URL, and customer message
- [ ] T076 [US4] Configure Contact Form CFDB7 retention policy: auto-delete submissions after 90 days in CFDB7 → Settings

**Checkpoint**: Visitors can inquire about products, forms deliver to email reliably, product details auto-fill, spam prevention active, GDPR compliant.

---

## Phase 7: User Story 5 - About & Brand Story (Priority: P3)

**Goal**: Create About page with artist bio, brand story, and contact information

**Independent Test**: Navigate to About page, verify professionally written bio, artist photo, design philosophy, contact form/email visible, compelling brand narrative present.

### Implementation for User Story 5

- [ ] T077 [US5] Create About page: Pages → Add New, title "About"
- [ ] T078 [US5] Add Cover block with artist photo for hero section on About page
- [ ] T079 [US5] Write/add artist biography using Paragraph blocks: background, artistic journey, design philosophy
- [ ] T080 [US5] Add tagline "If you'd like to collaborate, please get in touch. I'm all ears!" using Heading block
- [ ] T081 [US5] Insert contact form shortcode at bottom of About page using Shortcode block
- [ ] T082 [US5] Add social media links (Instagram, Facebook) using Buttons block
- [ ] T083 [US5] Create Contact page: Pages → Add New, title "Contact"
- [ ] T084 [US5] Add contact form shortcode to Contact page
- [ ] T085 [US5] Add email address hina@hinamirza.co as fallback on Contact page using Paragraph block
- [ ] T086 [US5] Add Instagram and social links to Contact page
- [ ] T087 [US5] Update Primary navigation menu to include About and Contact pages
- [ ] T088 [US5] Test About page: verify bio readable, photo displays, contact form works, social links open correctly

**Checkpoint**: About and Contact pages complete with compelling narrative, professional presentation, multiple contact methods available.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Performance optimization, SEO, security, and final polish

- [ ] T089 [P] Configure Yoast SEO meta titles and descriptions for all pages: Homepage, Portfolio, Shop, About, Contact
- [ ] T090 [P] Set featured images for all pages for social media sharing (og:image)
- [ ] T091 [P] Create Privacy Policy page: Pages → Add New, add GDPR-compliant privacy policy text covering form data collection
- [ ] T092 [P] Add Privacy Policy link to footer menu via Appearance → Menus
- [ ] T093 [P] Configure Wordfence firewall: enable learning mode initially, monitor for false positives
- [ ] T094 [P] Enable Wordfence login security: limit login attempts, block brute force attacks
- [ ] T095 [P] Set up automatic WordPress backups via hosting control panel (daily backups, 30-day retention)
- [ ] T096 Run Google PageSpeed Insights test: target Mobile 80+, Desktop 90+, address any critical issues
- [ ] T097 Test site on Chrome desktop: verify all pages load, all links work, forms submit
- [ ] T098 Test site on Safari desktop: verify compatibility
- [ ] T099 Test site on Firefox desktop: verify compatibility
- [ ] T100 Test site on Chrome mobile (Android): verify responsive layout, touch navigation
- [ ] T101 Test site on Safari mobile (iOS): verify responsive layout, touch navigation
- [ ] T102 Test slow 3G connection: verify lazy loading works, images sized appropriately
- [ ] T103 Verify SSL certificate active: all pages load with https://, no mixed content warnings
- [ ] T104 [P] Submit XML sitemap to Google Search Console (generated by Yoast SEO)
- [ ] T105 [P] Configure WordPress admin email notifications for form submissions, comments (if enabled), updates
- [ ] T106 [P] Create admin documentation: save quickstart.md guide to Google Docs for Hina's reference
- [ ] T107 Train Hina on content management: walkthrough creating portfolio post, product listing, editing pages
- [ ] T108 Verify all 5 user stories working: run independent tests from each user story phase
- [ ] T109 Clear all WordPress caches and test final performance: verify <3s load time target met

**Checkpoint**: Site production-ready, performant, secure, SEO-optimized, mobile-responsive, all user stories validated.

---

## Optional: Content Migration (If Applicable)

**Purpose**: Migrate content from existing hinamirza.co WordPress site

**Skip if starting fresh**

- [ ] T110 Export old site content: Tools → Export on old site, download WordPress XML file
- [ ] T111 Download media library from old site via FTP or All-in-One WP Migration plugin
- [ ] T112 Import content to new site: Tools → Import, install WordPress Importer, upload XML file
- [ ] T113 Upload old media files to new site wp-content/uploads/ directory via FTP
- [ ] T114 Regenerate thumbnails using Regenerate Thumbnails plugin (if image sizes changed)
- [ ] T115 Recategorize imported posts: assign Portfolio vs Products categories as appropriate
- [ ] T116 Rebuild page layouts using Gutenberg blocks (old Elementor layouts won't transfer)
- [ ] T117 Update internal links to point to new domain/structure using Better Search Replace plugin
- [ ] T118 Run ShortPixel bulk optimization on all imported images
- [ ] T119 Test migrated content: verify all posts display, images load, categories correct
- [ ] T120 301 redirect old URLs to new URLs if structure changed (via Yoast SEO or Redirection plugin)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup & Hosting)**: No dependencies - can start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 completion - BLOCKS all user stories
- **Phase 3 (US1 - Content Management)**: Depends on Phase 2 - Can run independently
- **Phase 4 (US2 - Portfolio Showcase)**: Depends on Phase 2 and Phase 3 (needs content to display) - Can run after US1
- **Phase 5 (US3 - Instagram)**: Depends on Phase 2 - Can run independently after Phase 2, parallel with US1/US2
- **Phase 6 (US4 - Product Sales)**: Depends on Phase 2 - Can run independently after Phase 2, parallel with other stories
- **Phase 7 (US5 - About Page)**: Depends on Phase 2 - Can run independently after Phase 2, parallel with other stories
- **Phase 8 (Polish)**: Depends on desired user stories being complete
- **Content Migration (Optional)**: Can run anytime after Phase 2, before or after user stories

### User Story Dependencies

- **US1 (Content Management)**: Foundational only - No dependencies on other stories
- **US2 (Portfolio Showcase)**: Depends on US1 (needs portfolio content to display)
- **US3 (Instagram)**: Foundational only - Independent, can run parallel with US1/US2/US4/US5
- **US4 (Product Sales)**: Foundational only - Independent, can run parallel with US1/US2/US3/US5
- **US5 (About Page)**: Foundational only - Independent, can run parallel with all other stories

### Within Each User Story

- Tasks within a phase generally flow sequentially
- Tasks marked [P] can run in parallel (different plugins, different pages)
- WordPress configuration tasks are quick (5-30 min each), parallelization less critical
- Content creation tasks (posts, pages) can be parallelized

### Parallel Opportunities

- **Phase 1 Setup**: Tasks T006-T009 can run in parallel after T005
- **Phase 2 Foundational**: Tasks T013-T019 (plugin installations) can run in parallel
- **Phase 3 US1**: Tasks T023-T028 can run in parallel (different configurations)
- **Phase 4 US2**: Page creation tasks can be parallelized with menu creation
- **Phase 5 US3**: Instagram setup is sequential (must connect before configuring)
- **Phase 6 US4**: T060-T063 (email setup) parallel with T065-T068 (form creation)
- **Phase 7 US5**: Page creation tasks can be fully parallelized
- **Phase 8 Polish**: Tasks T089-T095 can run in parallel (different configurations)

After Phase 2 completion, these user stories can run in parallel:
- US1 (Content Management)
- US3 (Instagram Integration)
- US4 (Product Sales)
- US5 (About Page)

US2 (Portfolio Showcase) should start after US1 has some content created.

---

## Parallel Example: Phase 2 Foundational

```bash
# Launch all plugin installations together:
Task T013: "Install Smash Balloon Social Photo Feed"
Task T014: "Install ShortPixel Image Optimizer"
Task T015: "Install Contact Form 7"
Task T016: "Install Contact Form CFDB7"
Task T017: "Install WP Mail SMTP"
Task T018: "Install Yoast SEO Free"
Task T019: "Install Wordfence Security"

# All can be installed simultaneously in separate browser tabs
```

## Parallel Example: After Phase 2 (Independent Stories)

```bash
# Team Member A: Complete US1 (Content Management)
Task T023-T034

# Team Member B: Complete US3 (Instagram Integration)
Task T048-T059

# Team Member C: Complete US4 (Product Sales)
Task T060-T076

# Team Member D: Complete US5 (About Page)
Task T077-T088

# All run independently, no conflicts
```

---

## Implementation Strategy

### MVP First (US1 + US2 Only)

1. Complete Phase 1: Setup & Hosting (Tasks T001-T009)
2. Complete Phase 2: Foundational (Tasks T010-T022) - CRITICAL
3. Complete Phase 3: US1 Content Management (Tasks T023-T034)
4. Complete Phase 4: US2 Portfolio Showcase (Tasks T035-T047)
5. **STOP and VALIDATE**: Test that Hina can add portfolio content and it displays beautifully
6. Run Phase 8 Polish tasks T089-T109 for MVP launch

**MVP Timeline**: 4-6 hours of focused work

### Full Feature Set (All User Stories)

1. Complete Phase 1 + Phase 2 → Foundation ready
2. Add US1 + US2 → Test independently → **MVP Launch!**
3. Add US3 (Instagram) → Test independently → Deploy update
4. Add US4 (Product Sales) → Test independently → Deploy update
5. Add US5 (About Page) → Test independently → Deploy update
6. Run Phase 8 Polish for final production hardening

**Full Timeline**: 8-12 hours total work over 2-3 days (including DNS propagation)

### Parallel Team Strategy

With 2-3 people:

1. Person A: Phase 1 + Phase 2 setup (solo, 2 hours)
2. Once Phase 2 done, split user stories:
   - **Person A**: US1 + US2 (Content + Portfolio) - MVP core
   - **Person B**: US3 + US4 (Instagram + Product Sales)
   - **Person C**: US5 (About Page) + Phase 8 Polish tasks
3. Merge and test all stories together
4. Person C runs final Phase 8 validation

**Parallel Timeline**: 3-4 hours with 3 people

---

## Notes

- [P] tasks = different configurations/pages, no conflicts
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- WordPress admin tasks are quick (5-30 min each typically)
- Most time spent in Phase 2 (plugin setup), Phase 3 (content), Phase 4 (design)
- Commit/backup after each phase completion
- Stop at any checkpoint to validate story independently
- DNS propagation (T002) takes 24-48 hours - plan accordingly
- Email setup (Phase 6) requires external account signup (SendGrid)
- Instagram integration (Phase 5) requires Professional Instagram account

---

## Testing Checklist (Manual UAT)

### Pre-Launch Validation

**User Story 1 (Content Management):**
- [ ] Hina can log into WordPress admin
- [ ] Can create new portfolio post with images
- [ ] Images auto-optimize via ShortPixel
- [ ] Can edit and republish existing posts
- [ ] Changes appear immediately on public site

**User Story 2 (Portfolio Showcase):**
- [ ] Portfolio page displays 3-column grid (desktop)
- [ ] Portfolio page displays 2-column grid (mobile)
- [ ] Category filters work (Fabric, Wallpaper, etc.)
- [ ] Lightbox opens on image click
- [ ] Page loads in under 3 seconds
- [ ] Mobile touch navigation smooth

**User Story 3 (Instagram Integration):**
- [ ] 12 Instagram posts display on homepage
- [ ] Grid layout: 3 cols desktop, 2 cols mobile
- [ ] Clicking post opens Instagram in new tab
- [ ] Feed updates automatically (check after 6 hours)
- [ ] Graceful fallback if API unavailable

**User Story 4 (Product Sales):**
- [ ] Shop page displays product listings
- [ ] Product detail shows price, images, inquiry button
- [ ] Clicking inquiry button opens form with product auto-filled
- [ ] Form submits successfully
- [ ] Email arrives at hina@hinamirza.co within 5 minutes
- [ ] Email includes product name and customer details
- [ ] Spam prevention active (reCAPTCHA)

**User Story 5 (About Page):**
- [ ] About page displays bio and photo
- [ ] Contact form works on About page
- [ ] Social links open correctly
- [ ] Contact page accessible
- [ ] Email fallback visible

**Performance:**
- [ ] PageSpeed Mobile: 80+ score
- [ ] PageSpeed Desktop: 90+ score
- [ ] Homepage loads <3 seconds
- [ ] All images <500KB
- [ ] Lazy loading works

**Security & SEO:**
- [ ] SSL active (https://)
- [ ] All plugins updated
- [ ] Wordfence scan clean
- [ ] Meta titles/descriptions set
- [ ] XML sitemap submitted

**Cross-Browser:**
- [ ] Works on Chrome (desktop + mobile)
- [ ] Works on Safari (desktop + iOS)
- [ ] Works on Firefox desktop
- [ ] Responsive on tablet

---

## Task Count Summary

- **Total Tasks**: 120 tasks (109 main + 11 optional migration)
- **Phase 1 (Setup)**: 9 tasks
- **Phase 2 (Foundational)**: 13 tasks
- **Phase 3 (US1)**: 12 tasks
- **Phase 4 (US2)**: 13 tasks
- **Phase 5 (US3)**: 12 tasks
- **Phase 6 (US4)**: 17 tasks
- **Phase 7 (US5)**: 12 tasks
- **Phase 8 (Polish)**: 21 tasks
- **Optional (Migration)**: 11 tasks

**Parallel Opportunities**: 35+ tasks marked [P]

**MVP Scope (US1 + US2)**: 47 tasks (Phases 1-4 + selected Polish tasks)

**Suggested MVP**: US1 (Content Management) + US2 (Portfolio Showcase) = Core portfolio functionality

---

## Success Criteria

✅ **Launch Requirements Met When:**
- All Phase 1-2 tasks complete
- At minimum US1 + US2 complete and validated
- Performance targets achieved (<3s load, 80+ PageSpeed)
- Security hardened (SSL, Wordfence, strong password)
- Hina can independently manage content

🚀 **Ready to Deploy When:**
- All desired user stories (3-7) complete
- All Phase 8 polish tasks complete
- Cross-browser testing passed
- DNS propagated (24-48 hours after T002)
- Backup system configured

📊 **Ongoing Success Metrics:**
- Hina can add portfolio items in <10 min without help
- Site maintains 99.9% uptime
- Form inquiries deliver reliably
- Instagram feed updates automatically
- Performance stays within targets

---

**Ready to Begin!** Start with Phase 1, Task T001. Follow quickstart.md for detailed step-by-step guidance.
