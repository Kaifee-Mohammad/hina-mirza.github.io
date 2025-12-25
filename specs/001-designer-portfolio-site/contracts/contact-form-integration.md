# Contact Form Integration Contract

**Feature**: 001-designer-portfolio-site
**Integration**: Contact Form 7 to Email Delivery
**Date**: 2025-12-25

## Overview

This document specifies the integration between website contact forms and email delivery for inquiry-based sales and collaboration requests.

---

## Integration Architecture

```
Website Visitor
    ↓
Contact Form (Contact Form 7)
    ↓
WordPress Form Processing
    ↓
Email Delivery (SMTP / Hosting Mail)
    ↓
Hina's Email Inbox
    ↓
Database Storage (Optional - for backup)
```

---

## Form Types

### 1. General Contact Form

**Location:** /contact/ page
**Purpose:** General inquiries, collaborations, questions

**Fields:**

| Field | Type | Required | Validation | Placeholder |
|-------|------|----------|------------|-------------|
| name | Text | Yes | Max 100 chars | Your Name |
| email | Email | Yes | Valid email format | your@email.com |
| subject | Select | Yes | Predefined options | Select inquiry type |
| message | Textarea | Yes | Max 2000 chars | Your message |
| consent | Checkbox | Yes | Must be checked | I agree to privacy policy |

**Subject Options:**
- General Inquiry
- Collaboration Request
- Press/Media Inquiry
- Other

---

### 2. Product Inquiry Form

**Location:** Individual product pages
**Purpose:** Inquire about specific products for purchase

**Fields:**

| Field | Type | Required | Validation | Placeholder |
|-------|------|----------|------------|-------------|
| name | Text | Yes | Max 100 chars | Your Name |
| email | Email | Yes | Valid email format | your@email.com |
| phone | Tel | No | Phone format (optional) | (Optional) Phone |
| product_name | Hidden | Auto | Auto-filled | [Product Title] |
| product_url | Hidden | Auto | Auto-filled | [Product URL] |
| message | Textarea | Yes | Max 2000 chars | Tell us about your interest |
| consent | Checkbox | Yes | Must be checked | I agree to privacy policy |

**Auto-filled Fields:**
- Product name (from page title)
- Product URL (from current page)
- Timestamp (submission time)

---

## Email Delivery Contract

### Email Configuration

**From Address:** noreply@hinamirza.co (or hosting default)
**To Address:** hina@hinamirza.co (or designated email)
**Reply-To:** Visitor's email address

### General Contact Email Template

```
Subject: New Contact Form Submission: [Subject]

From: [Name]
Email: [Email]
Subject: [Selected Subject]

Message:
[Message Content]

---
Submitted: [Timestamp]
IP Address: [IP] (for spam prevention)
User Agent: [Browser/Device Info]
```

### Product Inquiry Email Template

```
Subject: Product Inquiry: [Product Name]

PRODUCT INQUIRY

Customer Information:
Name: [Name]
Email: [Email]
Phone: [Phone] (if provided)

Product Details:
Product: [Product Name]
URL: [Product URL]

Customer Message:
[Message Content]

---
Submitted: [Timestamp]
IP Address: [IP]
```

---

## Form Validation Rules

### Client-Side Validation (JavaScript)

```javascript
// Name validation
name: {
  required: true,
  minLength: 2,
  maxLength: 100,
  pattern: /^[a-zA-Z\s'-]+$/,
  errorMessage: "Please enter a valid name"
}

// Email validation
email: {
  required: true,
  pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  errorMessage: "Please enter a valid email address"
}

// Message validation
message: {
  required: true,
  minLength: 10,
  maxLength: 2000,
  errorMessage: "Message must be between 10 and 2000 characters"
}

// Consent validation
consent: {
  required: true,
  mustBeChecked: true,
  errorMessage: "You must agree to the privacy policy"
}
```

### Server-Side Validation (Contact Form 7)

```
[text* your-name maxlength:100 class:form-control placeholder "Your Name"]

[email* your-email class:form-control placeholder "your@email.com"]

[select* inquiry-type class:form-control
  "General Inquiry"
  "Product Inquiry"
  "Collaboration Request"
  "Press/Media Inquiry"
  "Other"]

[textarea* your-message maxlength:2000 class:form-control
  placeholder "Your message"]

[acceptance acceptance-privacy class:form-check-input]
I agree to the [link privacy policy]
[/acceptance]

[submit class:btn-primary "Send Message"]
```

---

## Spam Prevention

### Security Measures

| Method | Implementation | Effectiveness |
|--------|---------------|---------------|
| reCAPTCHA v3 | Invisible, scores visitors | High |
| Honeypot Field | Hidden field (bots fill it) | Medium |
| IP Logging | Track submission IPs | Medium |
| Rate Limiting | Max 5 submissions/hour/IP | High |
| Email Confirmation | Require valid email | High |
| Akismet | WordPress anti-spam service | Very High |

### Recommended Setup
- **Primary:** Contact Form 7 + reCAPTCHA v3
- **Secondary:** Akismet for additional spam filtering
- **Tertiary:** Honeypot field (built into CF7)

### reCAPTCHA Configuration

```php
// Site Key (public)
site_key: [Google reCAPTCHA site key]

// Secret Key (private)
secret_key: [Google reCAPTCHA secret key]

// Threshold
score_threshold: 0.5 (0-1, lower = stricter)

// Action
action: contact_form_submit
```

---

## Email Delivery Methods

### Option 1: Hosting Default (SMTP)

**Pros:**
- No additional setup
- Free (included in hosting)
- Works out of the box

**Cons:**
- Less reliable (can be flagged as spam)
- No delivery tracking
- Shared server reputation

**Setup:** None required (default Contact Form 7 behavior)

---

### Option 2: WP Mail SMTP Plugin (Recommended)

**Provider Options:**
- **SendGrid:** 100 emails/day free
- **Mailgun:** 5,000 emails/month free (first 3 months)
- **Gmail SMTP:** Free but limited (500/day)
- **Amazon SES:** $0.10 per 1,000 emails

**Recommended:** SendGrid (100/day = 3,000/month free)

**Setup Steps:**
1. Install "WP Mail SMTP" plugin
2. Sign up for SendGrid free account
3. Generate API key
4. Configure plugin with API key
5. Set From email: noreply@hinamirza.co
6. Test email delivery

**Benefits:**
- High deliverability (99%+)
- Email tracking/analytics
- SPF/DKIM configured automatically
- Professional email reputation

---

## Response Times & Notifications

### Delivery SLA

| Metric | Target | Monitoring |
|--------|--------|------------|
| Form submission → Email delivery | < 5 minutes | Email notifications |
| Email inbox arrival | < 5 minutes | Test weekly |
| Admin notification | < 5 minutes | Dashboard alert |

### Admin Notifications

**Success Message (Visitor):**
```
Thank you for your message!

We've received your inquiry and will respond within 24-48 hours.

If you don't hear from us, please check your spam folder or email
directly at hina@hinamirza.co.

- Hina Mirza Studio
```

**Confirmation Email (Visitor - Optional):**
```
Subject: Thank you for contacting Hina Mirza

Hello [Name],

Thank you for reaching out! We've received your message:

[Brief message echo]

We'll respond within 24-48 hours.

Best regards,
Hina Mirza
hinamirza.co
```

---

## Database Storage (Optional)

### Storage Plugin: Contact Form 7 Database Addon (CFDB7)

**Purpose:** Backup form submissions in WordPress database

**Data Structure:**

```sql
CREATE TABLE wp_db7_forms (
  form_id INT PRIMARY KEY AUTO_INCREMENT,
  form_post_id INT,
  form_value TEXT,
  form_date DATETIME,
  form_ip VARCHAR(45),
  form_user_agent TEXT
);
```

**Retention Policy:**
- Store all submissions for 90 days
- Auto-delete after 90 days (GDPR compliance)
- Admin can export to CSV anytime

**Privacy Considerations:**
- Store only necessary data
- Encrypt sensitive information
- Provide deletion mechanism
- Include in privacy policy

---

## Error Handling

### Error Scenarios

| Error | Cause | User Message | Admin Action |
|-------|-------|--------------|--------------|
| Email delivery failed | SMTP error | "Sorry, there was a problem sending your message. Please email directly." | Check email logs |
| Invalid email format | Bad input | "Please enter a valid email address" | None (client-side) |
| Spam detected | reCAPTCHA low score | "Your submission appears suspicious. Please try again." | Review Akismet logs |
| Rate limit exceeded | Too many submissions | "Too many submissions. Please wait before trying again." | Check for abuse |
| Database storage failed | DB error | Form still submits (silent failure) | Check database logs |

### Fallback Contact Methods

**If form fails completely:**
```html
<div class="contact-fallback">
  <p>Having trouble with the form? Email us directly:</p>
  <a href="mailto:hina@hinamirza.co">hina@hinamirza.co</a>
</div>
```

---

## Testing Checklist

### Functional Tests
- [ ] Form displays correctly on all pages
- [ ] All fields validate (client-side)
- [ ] Required fields enforced
- [ ] Email format validated
- [ ] reCAPTCHA badge appears
- [ ] Submission shows success message
- [ ] Email arrives in inbox within 5 minutes
- [ ] Reply-to address is visitor's email
- [ ] Product inquiry auto-fills product info
- [ ] Consent checkbox required

### Spam Prevention Tests
- [ ] Honeypot field hidden from users
- [ ] reCAPTCHA prevents bot submissions
- [ ] Rate limiting works (5+ submissions blocked)
- [ ] Akismet filters spam (if enabled)

### Email Delivery Tests
- [ ] Emails arrive in inbox (not spam)
- [ ] From address correct
- [ ] Reply-to visitor's email
- [ ] Subject line correct
- [ ] Message formatting preserved
- [ ] Timestamp accurate
- [ ] Auto-filled fields populate

### Mobile Tests
- [ ] Form responsive on mobile
- [ ] All fields accessible on touch devices
- [ ] Keyboard dismisses properly
- [ ] Submit button large enough for touch

---

## Performance Requirements

### Form Loading
- **Render time:** <500ms
- **JavaScript size:** <50KB (including reCAPTCHA)
- **No blocking:** Async loading

### Submission Processing
- **Processing time:** <2 seconds
- **User feedback:** Instant (loading spinner)
- **Email delivery:** <5 minutes
- **Database insert:** <1 second

---

## Privacy & GDPR Compliance

### Privacy Policy Requirements

**Must include:**
- What data is collected (name, email, message, IP)
- Why data is collected (respond to inquiries)
- How data is stored (database, email)
- How long data is retained (90 days)
- Who has access (site admin only)
- User rights (deletion request)
- Contact for privacy requests

### Consent Checkbox Language

```
[x] I agree to the privacy policy and terms of service

By submitting this form, you consent to us storing and processing
your personal information to respond to your inquiry. We will not
share your information with third parties. See our privacy policy
for details.
```

### Data Deletion Requests

**Process:**
1. Receive deletion request via email
2. Delete from database (CFDB7 admin panel)
3. Delete from email archives
4. Confirm deletion within 30 days
5. Document request (for compliance)

---

## Monitoring & Maintenance

### Monthly Checks
- [ ] Test form submission end-to-end
- [ ] Check spam filter (Akismet dashboard)
- [ ] Review submission count
- [ ] Verify email deliverability
- [ ] Check reCAPTCHA score distribution
- [ ] Export and delete old submissions (90+ days)

### Quarterly Reviews
- [ ] Review spam prevention effectiveness
- [ ] Update email templates if needed
- [ ] Check SendGrid usage (within free tier?)
- [ ] Review privacy policy accuracy
- [ ] Test all form variations

---

## Cost Summary

| Component | Provider | Cost |
|-----------|----------|------|
| Contact Form 7 | WordPress.org | Free |
| WP Mail SMTP | WordPress.org | Free |
| SendGrid SMTP | SendGrid | Free (100/day) |
| reCAPTCHA v3 | Google | Free |
| Akismet | Automattic | $5/month (optional) |
| CFDB7 Plugin | WordPress.org | Free |
| **Total** | | **$0-5/month** |

**Recommendation:** Start with free tier (no Akismet). Add Akismet only if spam becomes issue.

---

## Implementation Steps

### Setup Sequence
1. Install Contact Form 7 plugin
2. Install CFDB7 (form backup) plugin
3. Install WP Mail SMTP plugin
4. Sign up for SendGrid free account
5. Configure WP Mail SMTP with SendGrid API
6. Create general contact form
7. Create product inquiry form template
8. Add forms to pages (shortcode/block)
9. Set up reCAPTCHA v3 (Google)
10. Configure spam prevention (Akismet optional)
11. Test all forms thoroughly
12. Set up retention policy (90 days)
13. Create privacy policy page
14. Train admin on form management

**Estimated Time:** 2-3 hours total setup

---

## Success Criteria

### Launch Requirements
- [x] Contact forms on all required pages
- [x] Emails deliver within 5 minutes
- [x] Spam prevention active (>95% blocked)
- [x] Mobile responsive
- [x] GDPR compliant
- [x] Privacy policy in place
- [x] Admin can view submissions

### Ongoing Metrics
- **Deliverability:** 99%+ emails reach inbox
- **Spam rate:** <5% false positives
- **Response time:** Admin responds within 24-48 hours
- **Uptime:** 99.9%+ form availability

---

This contract ensures reliable, secure, and GDPR-compliant contact form integration with professional email delivery.
