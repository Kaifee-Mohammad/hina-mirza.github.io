---
layout: default
title: Contact
permalink: /contact/
---
<div class="contact-page">
  <header class="page-header compact">
    <h1>Get in Touch</h1>
  </header>

  <div class="contact-content">
    <div class="contact-form">
      <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="contact">
        <p style="display: none;">
          <label>Don't fill this out: <input name="bot-field"></label>
        </p>

        <div class="form-row">
          <div class="form-group">
            <label for="name">Name *</label>
            <input type="text" id="name" name="name" required>
          </div>

          <div class="form-group">
            <label for="email">Email *</label>
            <input type="email" id="email" name="email" required>
          </div>
        </div>

        <div class="form-group">
          <label for="subject">Subject *</label>
          <select id="subject" name="subject" required>
            <option value="">Select...</option>
            <option value="general">General Inquiry</option>
            <option value="collaboration">Collaboration</option>
            <option value="product">Product Inquiry</option>
            <option value="other">Other</option>
          </select>
        </div>

        <div class="form-group">
          <label for="message">Message *</label>
          <textarea id="message" name="message" rows="4" required></textarea>
        </div>

        <div class="form-actions">
          <label class="consent-label">
            <input type="checkbox" name="consent" required>
            I agree to the <a href="{{ '/privacy/' | relative_url }}" target="_blank">privacy policy</a>
          </label>
          <button type="submit" class="button primary">Send Message</button>
        </div>
      </form>
    </div>

    <div class="contact-info">
      <h3>Other Ways to Reach Me</h3>
      <p><strong>Email:</strong> <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></p>
      <p><strong>Instagram:</strong> <a href="https://instagram.com/{{ site.author.instagram }}" target="_blank">@{{ site.author.instagram }}</a></p>
    </div>
  </div>
</div>
