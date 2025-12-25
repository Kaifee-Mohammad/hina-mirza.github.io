# Instagram Feed Integration Contract

**Feature**: 001-designer-portfolio-site
**Integration**: Instagram to WordPress via Smash Balloon Social Photo Feed plugin
**Date**: 2025-12-25

## Overview

This document specifies the integration contract between Instagram (@hinamirza.art.design) and the WordPress portfolio website for automatic feed display.

---

## Integration Architecture

```
Instagram Account (@hinamirza.art.design)
    ↓
Instagram Graph API (Meta)
    ↓
Smash Balloon Plugin (Authentication & Caching)
    ↓
WordPress Database (Cached Feed Data)
    ↓
Blocksy Theme (Display Layer)
    ↓
Website Visitors
```

---

## API Authentication

### Instagram Account Requirements
- **Account Type:** Instagram Professional (Business or Creator)
- **Username:** @hinamirza.art.design
- **Access Level:** Read-only (public posts)
- **Permissions:** Basic profile info, media (photos/videos)

### Authentication Flow
1. Admin installs Smash Balloon plugin
2. Admin clicks "Connect Instagram Account"
3. Redirected to Instagram OAuth login
4. Grant permissions (read-only)
5. Smash Balloon stores access token (encrypted)
6. Token auto-refreshes (handled by plugin)

### Token Management
- **Initial token:** 60-day expiration
- **Refresh:** Automatic by Smash Balloon
- **Storage:** WordPress database (encrypted)
- **Revocation:** Through Instagram settings or plugin disconnect

---

## Data Contract

### Request Parameters

```json
{
  "endpoint": "https://graph.instagram.com/me/media",
  "method": "GET",
  "authentication": "Bearer {access_token}",
  "parameters": {
    "fields": "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp",
    "limit": 12
  }
}
```

### Response Format

```json
{
  "data": [
    {
      "id": "instagram_media_id",
      "caption": "Artwork description and hashtags",
      "media_type": "IMAGE",
      "media_url": "https://scontent.cdninstagram.com/...",
      "permalink": "https://www.instagram.com/p/...",
      "thumbnail_url": "https://scontent.cdninstagram.com/...",
      "timestamp": "2025-12-25T10:30:00+0000"
    }
  ],
  "paging": {
    "cursors": {
      "before": "cursor_string",
      "after": "cursor_string"
    }
  }
}
```

### Cached Data Structure (WordPress)

```php
// Stored in wp_options or custom table
array(
    'instagram_posts' => array(
        array(
            'post_id' => 'string',
            'image_url' => 'string (CDN URL)',
            'caption' => 'string (max 2200 chars)',
            'post_link' => 'string (Instagram URL)',
            'timestamp' => 'datetime (ISO 8601)',
            'media_type' => 'IMAGE|VIDEO|CAROUSEL',
            'likes' => 'integer (if available)',
            'comments' => 'integer (if available)'
        )
    ),
    'last_updated' => 'datetime',
    'cache_expiry' => 'datetime (current + 6 hours)'
)
```

---

## Display Specifications

### Feed Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| Display count | 12 posts | Show 12 most recent |
| Layout | Grid | 3 columns desktop, 2 mobile |
| Image size | 300x300px | Square crop |
| Loading | Lazy load | Below-fold optimization |
| Lightbox | Enabled | Click to enlarge |
| Caption | Truncated | Max 150 characters shown |
| Link behavior | New tab | Opens Instagram post |

### Responsive Breakpoints

```css
/* Desktop: 3 columns */
@media (min-width: 992px) {
  .instagram-grid { grid-template-columns: repeat(3, 1fr); }
}

/* Tablet: 2 columns */
@media (min-width: 768px) and (max-width: 991px) {
  .instagram-grid { grid-template-columns: repeat(2, 1fr); }
}

/* Mobile: 2 columns (smaller images) */
@media (max-width: 767px) {
  .instagram-grid { grid-template-columns: repeat(2, 1fr); }
}
```

---

## Caching Strategy

### Cache Configuration
- **Initial load:** API call to fetch latest posts
- **Cache duration:** 6 hours (configurable: 1-24 hours)
- **Cache storage:** WordPress transients or database
- **Cache key:** `instagram_feed_hinamirza`

### Cache Refresh Logic

```
IF cache expired OR manual refresh:
    CALL Instagram API
    IF API success:
        UPDATE cache with new data
        SET expiry = current_time + 6 hours
    ELSE IF API failure:
        KEEP existing cache
        LOG error
        SET retry = current_time + 1 hour
    ENDIF
ENDIF

RETURN cached data
```

### Fallback Behavior
- If API unavailable: Display last cached posts
- If cache empty: Display placeholder message
- If account disconnected: Show "Connect Instagram" button (admin only)

---

## Error Handling

### Error Scenarios

| Error | Cause | User Impact | Admin Action |
|-------|-------|-------------|--------------|
| 401 Unauthorized | Token expired | Feed shows old cache | Reconnect Instagram account |
| 403 Forbidden | Account privacy changed | Feed hidden | Change account to Professional |
| 429 Rate Limited | Too many API calls | Feed shows cache | Wait for rate limit reset |
| 500 API Error | Instagram server issue | Feed shows cache | Wait for Instagram fix |
| Network Timeout | Connection issue | Feed shows cache | Check hosting/firewall |

### Error Messages (Admin Only)

```
// Admin dashboard notice
"Instagram Feed: Unable to refresh feed. Using cached posts.
Error: [error_message].
Last successful update: [timestamp]"
```

### User-Facing Fallback

```html
<!-- If feed fails completely -->
<div class="instagram-fallback">
  <p>Follow us on Instagram:
    <a href="https://instagram.com/hinamirza.art.design" target="_blank">
      @hinamirza.art.design
    </a>
  </p>
</div>
```

---

## Performance Requirements

### Response Times
- **Initial page load:** Feed HTML rendered immediately (cached)
- **Image loading:** Lazy load (only when scrolled into view)
- **API refresh:** Background process (doesn't block page load)
- **Cache lookup:** <100ms (database query)

### Bandwidth Optimization
- **Thumbnail size:** 300x300px (Instagram CDN optimized)
- **Image format:** WebP preferred, JPG fallback
- **CDN delivery:** Instagram CDN (no local storage)
- **Lazy loading:** Native browser lazy load attribute

---

## Security Considerations

### Data Protection
- **Access token:** Stored encrypted in WordPress database
- **API calls:** HTTPS only
- **No sensitive data:** Only public posts displayed
- **CORS:** Not applicable (server-side integration)

### Privacy Compliance
- **No tracking:** Instagram posts displayed without tracking scripts
- **User consent:** Not required (public Instagram content)
- **GDPR:** Compliant (no personal data collected from visitors)

---

## Setup Instructions

### Installation Steps
1. Install "Smash Balloon Social Photo Feed" plugin
2. Activate plugin
3. Navigate to Instagram Feed > Settings
4. Click "Connect an Instagram Account"
5. Log in with @hinamirza.art.design credentials
6. Authorize Smash Balloon app (read-only)
7. Configure display settings:
   - Number of posts: 12
   - Layout: Grid
   - Columns: 3 (desktop), 2 (mobile)
   - Image resolution: Auto
   - Cache duration: 6 hours
8. Insert feed using shortcode or block:
   - Shortcode: `[instagram-feed]`
   - Block: "Instagram Feed" (Gutenberg)
9. Preview and publish

### Configuration Options

```php
// Shortcode with parameters
[instagram-feed
  num=12
  cols=3
  showheader=false
  showbutton=true
  buttontext="View on Instagram"
]
```

---

## Monitoring & Maintenance

### Health Checks
- **Weekly:** Verify feed displays correctly
- **Monthly:** Check cache refresh working
- **Quarterly:** Review API usage (within free tier)
- **Yearly:** Verify token still valid

### Troubleshooting Steps
1. Check Instagram account still Professional
2. Verify Smash Balloon plugin updated
3. Clear WordPress cache
4. Test API connection (plugin settings)
5. Reconnect Instagram account if needed
6. Check error logs (WordPress debug.log)

---

## API Rate Limits

### Instagram Graph API Limits
- **Per app:** 200 calls/hour (Smash Balloon shared)
- **Per user:** Not specified (but typically generous)
- **Free tier:** Adequate for portfolio site

### Our Usage Estimate
- **Cache refresh:** Every 6 hours = 4 calls/day
- **Monthly:** ~120 API calls
- **Well within limits** (even with Smash Balloon's shared app)

---

## Testing Checklist

### Functional Tests
- [ ] Feed displays on homepage
- [ ] Shows 12 most recent posts
- [ ] Grid layout works (3 cols desktop, 2 mobile)
- [ ] Images load properly (lazy loading)
- [ ] Lightbox opens on click
- [ ] Links open Instagram post in new tab
- [ ] Captions truncate correctly
- [ ] "View on Instagram" button works

### Performance Tests
- [ ] Feed loads within 2 seconds
- [ ] Images lazy load (below fold)
- [ ] No impact on PageSpeed score
- [ ] Cache working (check database)
- [ ] API not called on every page load

### Error Handling Tests
- [ ] Disconnect Instagram → Shows fallback
- [ ] Cache expired → Refreshes automatically
- [ ] API error → Shows cached posts
- [ ] Network timeout → Graceful degradation

---

## Upgrade Path

### From Free to Pro (If Needed)
**Current:** Smash Balloon Free (100 credits/month)
**Upgrade:** $49/year for Pro features

**Pro Features (Optional):**
- Hashtag feeds (display posts by hashtag)
- Lightbox with video playback
- Like/comment counts visible
- Advanced moderation filters
- Premium support

**Decision Point:** Upgrade only if hashtag feeds or advanced filtering needed. Free tier sufficient for basic user feed display.

---

## Alternative Solutions (If Issues Arise)

### Backup Option 1: Instagram Embed
- Use Instagram's native embed code
- Manual paste for each post
- No automation but reliable

### Backup Option 2: Manual Instagram Section
- Add static Instagram link/button
- Update periodically with screenshots
- No API dependency

### Backup Option 3: Different Plugin
- Try "Spotlight Instagram Feeds" or "Feed Them Social"
- Similar features, different API handling
- Requires reconnection

---

## Success Criteria

### Launch Requirements
- [x] Instagram feed displays 12 recent posts
- [x] Grid layout responsive across devices
- [x] Auto-updates every 6 hours
- [x] No performance impact (<0.5s added load time)
- [x] Graceful fallback if API unavailable
- [x] Admin can reconnect account easily

### Ongoing Metrics
- **Uptime:** 99%+ feed availability
- **Freshness:** Posts appear within 6 hours
- **Performance:** No PageSpeed degradation
- **Maintenance:** <15 minutes/month admin time

---

This integration contract ensures reliable, performant Instagram feed integration with clear fallback mechanisms and maintenance procedures.
