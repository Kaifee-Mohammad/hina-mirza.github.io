# Data Model: Instagram Live Feed Page

**Feature**: 002-instagram-feed
**Date**: 2025-12-27

## Overview

This feature uses a minimal data model since Instagram post data is fetched and rendered by a third-party embed widget service. The only data stored locally is configuration information for the embed widget integration.

## Configuration Data Entity

**Location**: `_data/instagram.yml`
**Type**: YAML configuration file
**Managed By**: Netlify CMS (editable by Hina without code access)

### Instagram Configuration

| Field | Type | Required | Default | Description | Validation |
|-------|------|----------|---------|-------------|------------|
| `username` | string | Yes | - | Instagram handle (without @) | Non-empty, alphanumeric with underscores |
| `display_enabled` | boolean | Yes | `true` | Toggle feed visibility site-wide | true/false |
| `posts_count` | integer | Yes | `12` | Number of posts to display | Min: 6, Max: 24 |
| `widget_service` | enum | Yes | `behold` | Which embed service is configured | Options: behold, elfsight, lightwidget |
| `widget_id` | string | Yes | - | Unique embed ID from widget service | Non-empty string |

### Example Configuration

```yaml
username: "hinamirza_art"
display_enabled: true
posts_count: 12
widget_service: "behold"
widget_id: "abc123xyz"
```

## External Data (Read-Only)

**Instagram Post Data** - Managed by third-party embed widget service

The embed widget service (Behold/Elfsight/LightWidget) fetches and displays Instagram posts with the following attributes (read-only, not stored locally):

| Field | Type | Description |
|-------|------|-------------|
| `image_url` | string | URL to post thumbnail image |
| `caption` | string | Post caption text |
| `posted_at` | datetime | When the post was published on Instagram |
| `permalink` | string | URL to full post on Instagram |
| `media_type` | enum | Type of post (image, video, carousel) |

**Note**: This data is never stored in the Jekyll site. It's fetched client-side by the embed widget JavaScript.

## Data Flow

```text
┌─────────────────┐
│  Hina (via CMS) │
└────────┬────────┘
         │ Edits config
         ↓
┌─────────────────────┐
│  _data/instagram.yml│
└────────┬────────────┘
         │ Read by Jekyll
         ↓
┌─────────────────────────┐
│ Instagram Page Template │
└────────┬────────────────┘
         │ Includes widget embed code
         ↓
┌──────────────────────────┐
│  Browser loads page      │
│  + widget JavaScript     │
└────────┬─────────────────┘
         │ Fetches posts
         ↓
┌──────────────────────────┐
│ Widget Service API       │
│ (Behold/Elfsight)        │
└────────┬─────────────────┘
         │ Returns posts
         ↓
┌──────────────────────────┐
│ Widget renders grid      │
│ with Instagram posts     │
└──────────────────────────┘
```

## State Transitions

### Configuration State

```text
Initial State: No configuration exists
  │
  ├─→ [Admin creates config via CMS]
  │
  ↓
Active State: Configuration exists, display_enabled = true
  │
  ├─→ [Admin updates username] → Active State (new username)
  ├─→ [Admin disables feed] → Disabled State
  │
  ↓
Disabled State: Configuration exists, display_enabled = false
  │
  ├─→ [Admin enables feed] → Active State
  │
  ↓
Active State: Feed visible on site
```

## Validation Rules

### Instagram Username Validation

- **Format**: Alphanumeric characters and underscores only
- **Length**: 1-30 characters
- **No @ symbol**: Input should be "hinamirza_art" not "@hinamirza_art"
- **CMS Hint**: "Your Instagram handle (without @)"

### Widget ID Validation

- **Format**: Any non-empty string (format varies by service)
- **CMS Hint**: "Embed ID from your widget service dashboard"
- **Examples**:
  - Behold: "abc123xyz"
  - Elfsight: "550e8400-e29b-41d4-a716-446655440000"
  - LightWidget: "a1b2c3d4e5f6"

### Posts Count Validation

- **Minimum**: 6 posts (ensures grid has meaningful content)
- **Maximum**: 24 posts (prevents page from becoming too long, violating "Minimize Scrolling" principle)
- **Default**: 12 posts (optimal for desktop: 2 rows of 6)
- **CMS Widget**: Number input with min/max constraints

### Display Enabled Validation

- **Type**: Boolean
- **Values**: `true` | `false`
- **CMS Widget**: Toggle switch
- **Default**: `true`

## Relationships

This feature has no complex relationships. The single configuration entity is standalone.

**Configuration → Widget Service**: One-to-one relationship
- One configuration points to one widget service account
- If service changes (e.g., Behold → Elfsight), admin updates `widget_service` and `widget_id` fields

**Configuration → Instagram Account**: One-to-one relationship
- One configuration displays posts from one Instagram username
- Username can be changed without affecting other configuration

## Edge Cases

### Missing Configuration

**Scenario**: `_data/instagram.yml` doesn't exist

**Behavior**: Instagram page shows error message:
```
"Instagram feed is currently unavailable."
```

**Resolution**: Admin creates configuration via CMS

### Invalid Widget ID

**Scenario**: `widget_id` is incorrect or widget deleted from service

**Behavior**: Widget service shows error or empty state

**Resolution**: Admin checks widget service dashboard, updates `widget_id`

### Instagram Account Deleted/Private

**Scenario**: Instagram username no longer exists or account made private

**Behavior**: Widget service displays appropriate error message (handled by service)

**Resolution**: Admin updates `username` to valid account

### Display Disabled

**Scenario**: `display_enabled` set to `false`

**Behavior**: Instagram page shows:
```
"Instagram feed is currently unavailable."
```

**Resolution**: Admin re-enables via CMS toggle

## Performance Considerations

### Data Size

- **Configuration**: ~200 bytes (tiny YAML file)
- **Impact on Build**: Negligible (read once during Jekyll build)
- **Impact on Page Load**: None (configuration rendered as HTML attributes)

### Caching

- **Configuration**: Cached as part of static HTML after Jekyll build
- **Instagram Posts**: Cached by widget service (typically 15 min - 1 hour)
- **No server-side cache**: needed (pure static site)

## Security Considerations

### Sensitive Data

- **Widget ID**: Not sensitive (public embed code)
- **Instagram Username**: Public information
- **No API tokens**: stored (handled by widget service)
- **No user credentials**: required

### CMS Access Control

- **Who can edit**: Only authenticated CMS users (Hina)
- **Authentication**: Handled by Netlify Identity
- **Change tracking**: Git commits record all configuration changes

## Migration Strategy

### Initial Setup

1. Create `_data/instagram.yml` with template values
2. Admin logs into CMS → Site Settings → Instagram Feed
3. Admin enters Instagram username
4. Admin signs up for widget service (Behold/Elfsight)
5. Admin configures widget in service dashboard
6. Admin copies widget ID into CMS
7. Save → Netlify rebuilds site → Feed appears

### Changing Widget Services

**Example**: Migrating from Behold to Elfsight

1. Sign up for Elfsight, configure widget
2. Admin logs into CMS
3. Changes `widget_service` from "behold" to "elfsight"
4. Updates `widget_id` with new Elfsight ID
5. Save → Site rebuilds with new widget

**No data migration needed**: Instagram posts always fetched fresh from service

## Testing Data

### Test Configuration (Development)

```yaml
username: "hinamirza_art"
display_enabled: true
posts_count: 12
widget_service: "behold"
widget_id: "test-widget-123"  # Test widget ID
```

### Test Configuration (Production)

```yaml
username: "hinamirza_art"
display_enabled: true
posts_count: 12
widget_service: "behold"
widget_id: "ACTUAL_PRODUCTION_ID"  # Real widget ID from Behold
```

## Summary

**Data Complexity**: Minimal
- **Entities**: 1 (Instagram Configuration)
- **Relationships**: 0 (standalone configuration)
- **Validation Rules**: 4 (username, widget_id, posts_count, display_enabled)
- **State Transitions**: 2 (Active ↔ Disabled)

**Design Philosophy**: Delegate Instagram post management to specialized third-party service, maintain only essential configuration locally. This keeps the Jekyll site simple, fast, and easy to maintain while providing a robust Instagram feed feature.
