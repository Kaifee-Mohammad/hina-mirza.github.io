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
