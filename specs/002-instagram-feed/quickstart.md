# Quickstart: Instagram Live Feed Page

**Feature**: 002-instagram-feed
**Estimated Setup Time**: 30-45 minutes
**Skill Level**: Beginner (no coding required for basic setup)

## Overview

This guide will help you add an Instagram feed page to the Hina Mirza portfolio website. The page will display the 12 most recent Instagram posts in a responsive grid layout.

## Prerequisites

- [ ] Jekyll site deployed to Netlify (already set up)
- [ ] Netlify CMS configured and accessible
- [ ] Instagram account (public, not private)
- [ ] Access to commit to GitHub repository

## Quick Setup (5 Steps)

### Step 1: Choose Instagram Embed Service (5 minutes)

Pick one of these services to handle Instagram integration:

**Option A: Behold** (Recommended - $10/month)
- Best for static sites
- Sign up: https://behold.so
- Free tier: 1,200 views/month
- Paid Starter: $10/month (15,000 views, no branding)

**Option B: Elfsight** (Budget-friendly - Free or $5/month)
- Best free tier
- Sign up: https://elfsight.com/instagram-feed-instashow/
- Free: Basic features with branding
- Paid Basic: $5/month

**Option C: LightWidget** (Simplest - $15 one-time)
- One-time payment, no subscription
- Sign up: https://lightwidget.com
- Free: With branding
- Paid: $15 one-time (no branding)

### Step 2: Configure Your Widget (10 minutes)

**For Behold:**
1. Go to https://behold.so and create account
2. Click "Connect Instagram"
3. Authorize Instagram access (OAuth)
4. Click "Create Feed"
5. Choose "Grid" layout
6. Set number of posts: 12
7. Customize colors:
   - Background: #ffffff
   - Text: #333333
   - Accent: #d8c3be (peachy accent to match site)
8. Copy the **Widget ID** (looks like: `abc123xyz`)

**For Elfsight:**
1. Go to https://apps.elfsight.com
2. Sign up and connect Instagram
3. Create new Instagram Feed widget
4. Configure:
   - Layout: Grid
   - Posts: 12
   - Columns: Auto (responsive)
5. Customize appearance to match site
6. Copy the **Widget Code** (find the ID in the code: `elfsight-app-XXXXXXXX`)

**For LightWidget:**
1. Go to https://lightwidget.com
2. Create widget
3. Settings:
   - Username: your Instagram handle
   - Layout: Grid
   - Number of posts: 12
4. Customize styling
5. Copy the **Widget ID** from generated code

### Step 3: Create Configuration File (2 minutes)

Create `_data/instagram.yml` in your repository with:

```yaml
username: "hinamirza_art"          # Your Instagram handle (without @)
display_enabled: true               # Show the feed
posts_count: 12                     # Number of posts
widget_service: "behold"            # Service you chose: behold, elfsight, or lightwidget
widget_id: "YOUR_WIDGET_ID_HERE"   # Widget ID from Step 2
```

**Replace**:
- `YOUR_WIDGET_ID_HERE` with your actual widget ID
- `hinamirza_art` with your Instagram username
- `behold` with your chosen service if different

### Step 4: Add Instagram Page Files (10 minutes)

**4a. Create `instagram.md` in repository root:**

```markdown
---
layout: default
title: Instagram
permalink: /instagram/
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

**4b. Create `_includes/instagram-feed.html`:**

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

**4c. Add Instagram link to navigation** in `_includes/header.html`:

Find the navigation section and add Instagram link:

```html
<nav class="site-nav">
  <ul>
    <li><a href="{{ '/' | relative_url }}">Home</a></li>
    <li><a href="{{ '/portfolio/' | relative_url }}">Portfolio</a></li>
    <li><a href="{{ '/prints/' | relative_url }}">Art Prints</a></li>
    <li><a href="{{ '/instagram/' | relative_url }}">Instagram</a></li>  <!-- ADD THIS LINE -->
    <li><a href="{{ '/about/' | relative_url }}">About</a></li>
    <li><a href="{{ '/contact/' | relative_url }}">Contact</a></li>
  </ul>
</nav>
```

### Step 5: Test and Deploy (10 minutes)

**5a. Test locally:**

```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Open browser to http://localhost:4000/instagram/
```

**5b. Verify:**
- [ ] Instagram page loads at `/instagram/`
- [ ] Navigation menu shows Instagram link
- [ ] Widget displays posts (if configured correctly)
- [ ] Page looks good on mobile and desktop
- [ ] Clicking posts opens Instagram

**5c. Deploy:**

```bash
# Add all new files
git add _data/instagram.yml instagram.md _includes/instagram-feed.html _includes/header.html

# Commit
git commit -m "Add Instagram feed page

- Create Instagram page at /instagram/
- Add Instagram embed widget integration
- Update navigation with Instagram link
- Configure widget via _data/instagram.yml

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to GitHub
git push origin 002-instagram-feed
```

Netlify will automatically rebuild and deploy your site in 1-2 minutes.

## Configure CMS (Optional but Recommended)

To allow Hina to manage Instagram settings without editing code:

**Add to `admin/config.yml`:**

```yaml
collections:
  - name: "settings"
    label: "Site Settings"
    files:
      - label: "Instagram Feed"
        name: "instagram"
        file: "_data/instagram.yml"
        fields:
          - {label: "Instagram Username", name: "username", widget: "string", required: true}
          - {label: "Display Feed", name: "display_enabled", widget: "boolean", default: true}
          - {label: "Number of Posts", name: "posts_count", widget: "number", default: 12, min: 6, max: 24}
          - {label: "Widget Service", name: "widget_service", widget: "select", options: ["behold", "elfsight", "lightwidget"], default: "behold"}
          - {label: "Widget ID", name: "widget_id", widget: "string", required: true}
```

Now Hina can edit Instagram settings at `/admin/` → Site Settings → Instagram Feed.

## Troubleshooting

### Widget doesn't display

**Check:**
1. Is `widget_id` correct in `_data/instagram.yml`?
2. Is `widget_service` spelled correctly? (behold, elfsight, or lightwidget)
3. Did you save the widget in the service dashboard?
4. Check browser console for JavaScript errors (F12 → Console)

**Fix:**
- Double-check widget ID matches what's in service dashboard
- Verify service name is lowercase
- Make sure widget is "published" in service dashboard

### Navigation link doesn't appear

**Check:**
1. Did you add the Instagram link to `_includes/header.html`?
2. Did you rebuild the site after adding it?

**Fix:**
- Check header.html has the Instagram `<li>` line
- Run `bundle exec jekyll serve` locally to verify
- Commit and push changes to trigger Netlify rebuild

### Posts show incorrect Instagram account

**Check:**
1. Is `username` field in `_data/instagram.yml` correct?
2. Did you connect the correct Instagram account to widget service?

**Fix:**
- Update `username` in `_data/instagram.yml`
- In widget service dashboard, reconnect to correct Instagram account
- May need to delete and recreate widget

### "Instagram feed is currently unavailable"

**Reason:** `display_enabled` is set to `false` in `_data/instagram.yml`

**Fix:**
- Change `display_enabled: false` to `display_enabled: true`
- Commit and push

### Page looks broken on mobile

**Check:**
- Are you using the correct SASS classes from the plan?
- Did you add responsive styles?

**Fix:**
- Refer to plan.md Design Specifications section
- Copy Instagram page styles to `_sass/_pages.scss`
- Test at multiple breakpoints

### Widget shows different number of posts than configured

**Note:** The `posts_count` field in `_data/instagram.yml` is currently informational. The actual number of posts is controlled in the widget service dashboard.

**Fix:**
- Log into widget service dashboard (Behold/Elfsight/LightWidget)
- Edit widget settings
- Change "Number of posts" to 12
- Save and wait for widget to refresh (5-60 minutes)

## Next Steps

After basic setup is complete:

1. **Add styling** - See plan.md for complete SCSS styles
2. **Add UI tests** - See plan.md for test suite additions
3. **Optimize performance** - Add lazy loading if needed
4. **Customize widget** - Match peachy accent color #d8c3be exactly
5. **Monitor usage** - Check widget service dashboard for view counts

## Cost Summary

**Monthly Costs:**

| Service | Free Tier | Recommended Paid | Best For |
|---------|-----------|------------------|----------|
| Behold | 1,200 views/mo | $10/mo (15k views) | Static sites, clean design |
| Elfsight | Limited features | $5/mo | Tight budgets |
| LightWidget | With branding | $15 one-time | No subscriptions |

**Recommendation**: Start with free tier to test, upgrade to Behold Starter ($10/mo) when ready for professional launch.

## Support

**Widget Service Issues:**
- Behold: https://behold.so/support
- Elfsight: https://apps.elfsight.com/support
- LightWidget: https://lightwidget.com/support

**Jekyll/Netlify Issues:**
- Jekyll Docs: https://jekyllrb.com/docs/
- Netlify Support: https://docs.netlify.com/

**Hina Mirza Site Specific:**
- Refer to plan.md in `specs/002-instagram-feed/`
- Check repository documentation

## Estimated Time Breakdown

- Widget service signup: 5 min
- Widget configuration: 10 min
- Create config file: 2 min
- Add page files: 10 min
- Test locally: 5 min
- Deploy: 3 min
- **Total: 35 minutes**

(Add 15 minutes if adding CMS configuration)

## Success Checklist

After completing setup, verify:

- [ ] Can access `/instagram/` page
- [ ] Navigation shows Instagram link on all pages
- [ ] Widget displays 12 Instagram posts
- [ ] Posts are clickable and open Instagram
- [ ] Page looks good on mobile (test on phone)
- [ ] NoScript message appears when JS disabled
- [ ] CMS can edit Instagram settings (if configured)

## You're Done! 🎉

The Instagram feed is now live. Hina can manage settings through the CMS (if configured) or by editing `_data/instagram.yml` directly.

**Next Command**: `/speckit.tasks` to generate detailed implementation task list
