// Lightbox functionality
document.addEventListener('DOMContentLoaded', function() {
  const lightbox = document.getElementById('lightbox');
  const lightboxImage = document.getElementById('lightbox-image');
  const lightboxTitle = document.getElementById('lightbox-title');
  const lightboxDescription = document.getElementById('lightbox-description');
  const lightboxPrice = document.getElementById('lightbox-price');
  const lightboxDimensions = document.getElementById('lightbox-dimensions');
  const lightboxMaterials = document.getElementById('lightbox-materials');
  const lightboxSizes = document.getElementById('lightbox-sizes');
  const closeBtn = document.querySelector('.lightbox-close');

  // Open lightbox
  document.querySelectorAll('.lightbox-trigger').forEach(trigger => {
    trigger.addEventListener('click', function(e) {
      e.preventDefault();

      const image = this.getAttribute('data-image');
      const title = this.getAttribute('data-title');
      const description = this.getAttribute('data-description');
      const price = this.getAttribute('data-price');
      const dimensions = this.getAttribute('data-dimensions');
      const materials = this.getAttribute('data-materials');
      const sizes = this.getAttribute('data-sizes');

      lightboxImage.src = image;
      lightboxTitle.textContent = title;

      if (lightboxDescription) {
        lightboxDescription.textContent = description || '';
      }

      if (lightboxPrice) {
        lightboxPrice.textContent = price || '';
        lightboxPrice.style.display = price ? 'block' : 'none';
      }

      if (lightboxDimensions) {
        lightboxDimensions.textContent = dimensions ? 'Dimensions: ' + dimensions : '';
        lightboxDimensions.style.display = dimensions ? 'block' : 'none';
      }

      if (lightboxMaterials) {
        lightboxMaterials.textContent = materials ? 'Materials: ' + materials : '';
        lightboxMaterials.style.display = materials ? 'block' : 'none';
      }

      if (lightboxSizes) {
        lightboxSizes.textContent = sizes ? 'Available Sizes: ' + sizes : '';
        lightboxSizes.style.display = sizes ? 'block' : 'none';
      }

      lightbox.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    });
  });

  // Close lightbox
  if (closeBtn) {
    closeBtn.addEventListener('click', function() {
      lightbox.style.display = 'none';
      document.body.style.overflow = 'auto';
    });
  }

  // Close on background click
  if (lightbox) {
    lightbox.addEventListener('click', function(e) {
      if (e.target === lightbox) {
        lightbox.style.display = 'none';
        document.body.style.overflow = 'auto';
      }
    });
  }

  // Close on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && lightbox.style.display === 'flex') {
      lightbox.style.display = 'none';
      document.body.style.overflow = 'auto';
    }
  });

  // Portfolio filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');

  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const category = this.getAttribute('data-category');

      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      // Filter items
      galleryItems.forEach(item => {
        if (category === 'all' || item.getAttribute('data-category') === category) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
});
