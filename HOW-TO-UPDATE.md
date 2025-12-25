# How to Update Your Website Content

Hi Hina! This guide will show you how to update your portfolio website. It's easier than you think! 🎨

## Quick Overview

Your website is built with **Jekyll** - a simple system that uses text files to create web pages. All your content is in easy-to-edit markdown files (`.md` files) that you can update with any text editor.

---

## 📁 Where Everything Lives

```
hina-mirza.github.io/
├── _portfolio/          ← Your portfolio artwork files
├── _prints/             ← Your art prints for sale
├── assets/images/       ← All your images
│   ├── portfolio/       ← Portfolio images
│   └── prints/          ← Print images
├── about.md             ← About page content
└── contact.md           ← Contact page content
```

---

## 🎨 Adding a New Portfolio Item

### Step 1: Prepare Your Image
1. Save your artwork image (JPG, PNG, or SVG)
2. Name it something simple like `sunset-roses.jpg`
3. Move it to: `assets/images/portfolio/`

### Step 2: Create the Portfolio File
1. Go to the `_portfolio/` folder
2. Create a new file named `sunset-roses.md` (must end in `.md`)
3. Copy this template and fill in your details:

```markdown
---
layout: portfolio-item
title: "Sunset Roses"
category: "Paintings"
image: "/assets/images/portfolio/sunset-roses.jpg"
featured: true
dimensions: "24 x 36 inches"
materials: "Watercolor on paper"
year: 2024
availability: "Available"
---

Write your description here. This can be a few sentences about
the artwork, your inspiration, or any details you want to share.
```

### Step 3: Save and Done!
- Save the file
- Your new artwork will automatically appear on the website!

**Categories you can use:**
- Paintings
- Fabric
- Digital Art
- Mixed Media

---

## 🖼️ Adding a New Art Print

### Step 1: Prepare Your Print Image
1. Save your print image
2. Name it like `lavender-field.jpg`
3. Move it to: `assets/images/prints/`

### Step 2: Create the Print File
1. Go to the `_prints/` folder
2. Create a new file named `lavender-field.md`
3. Use this template:

```markdown
---
layout: print-item
title: "Lavender Field"
image: "/assets/images/prints/lavender-field.jpg"
price: "$45 - $120"
sizes: "8x10, 11x14, 16x20 inches"
material: "Museum-quality giclée print"
---

Beautiful lavender field captured in soft watercolors.
Perfect for creating a calming atmosphere in any room.

Each print is professionally produced with archival inks.
```

### Step 3: Save and Done!
- The new print will show up in your Art Prints gallery!

---

## ✏️ Editing Existing Content

### To Update an Artwork or Print:
1. Find the `.md` file in `_portfolio/` or `_prints/`
2. Open it with any text editor (TextEdit, Notepad, VS Code)
3. Change the text between the `---` lines or the description
4. Save the file

### Example - Changing the Price:
```markdown
Before: price: "$45 - $120"
After:  price: "$50 - $130"
```

---

## 📝 Updating Your About Page

1. Open the file: `about.md`
2. Edit the text (everything below the `---` section)
3. Save the file

You can use simple formatting:
- `**bold text**` for bold
- `*italic text*` for italic
- `## Heading` for headings
- `- item` for bullet lists

---

## 📧 Updating Contact Information

1. Open: `contact.md`
2. Update your email, social media links, or message
3. Save

---

## 🖼️ Replacing Images

### To Replace a Portfolio or Print Image:
1. Delete or rename the old image in `assets/images/portfolio/` or `assets/images/prints/`
2. Add your new image with the **exact same name** as referenced in the `.md` file
3. The website will automatically show the new image!

**Important:** The image filename in the `.md` file must match the actual file:
```markdown
image: "/assets/images/portfolio/roses.jpg"  ← This name
Must match: assets/images/portfolio/roses.jpg  ← This file
```

---

## 🗑️ Deleting Content

### To Remove a Portfolio Item or Print:
1. Delete the `.md` file from `_portfolio/` or `_prints/`
2. Optionally delete the image from `assets/images/`
3. It will disappear from the website!

---

## 🚀 Publishing Your Changes

There are **two ways** to work with your site:

### Option 1: Local Changes (Preview First)
1. Make your changes to the files
2. Open Terminal
3. Run: `bundle exec jekyll serve`
4. View at: `http://localhost:4000`
5. When happy, push to GitHub (see below)

### Option 2: Direct to GitHub (Live Immediately)
1. Go to your GitHub repository online
2. Click on a file to edit
3. Click the pencil icon (✏️) to edit
4. Make changes
5. Click "Commit changes" at the bottom
6. Your live site updates in 1-2 minutes!

---

## 📤 Pushing Changes to GitHub (Make Site Live)

### Using GitHub Desktop (Easiest):
1. Open GitHub Desktop
2. You'll see your changed files listed
3. Write a short description: "Added new rose painting"
4. Click "Commit to main"
5. Click "Push origin"
6. Done! Your site updates in 1-2 minutes

### Using Terminal:
```bash
git add .
git commit -m "Added new artwork"
git push
```

---

## 💡 Quick Tips

✅ **Always name files with lowercase and hyphens:**
- Good: `sunset-roses.md`, `lavender-field.jpg`
- Bad: `Sunset Roses.md`, `Lavender Field.jpg`

✅ **Keep image files small:**
- Aim for under 500KB per image
- Use JPG for photos, PNG for graphics

✅ **Test locally before pushing:**
- Run `bundle exec jekyll serve`
- Check at `http://localhost:4000`
- Make sure everything looks good!

✅ **Make small changes:**
- It's easier to fix one thing at a time
- You can always undo changes in GitHub

---

## 🆘 Common Issues

### "My image isn't showing!"
- Check the filename matches exactly in the `.md` file
- Check the image is in the correct folder
- Make sure the filename doesn't have spaces

### "My changes aren't appearing!"
- Wait 1-2 minutes for GitHub Pages to rebuild
- Hard refresh your browser (Cmd+Shift+R on Mac, Ctrl+F5 on Windows)
- Check you pushed the changes to GitHub

### "I made a mistake!"
- In GitHub Desktop, you can right-click and "Discard changes"
- Or contact your husband for help! 😊

---

## 📞 Need Help?

1. Ask your husband (he built this!)
2. Check the Jekyll documentation: https://jekyllrb.com/docs/
3. Everything is backed up on GitHub - you can't break it permanently!

---

## 🎨 Content Creation Workflow

**Recommended workflow for adding new art:**

1. ✏️ Create your artwork
2. 📸 Photograph or scan it (good quality!)
3. 🖼️ Save image to `assets/images/portfolio/` or `assets/images/prints/`
4. 📝 Create corresponding `.md` file in `_portfolio/` or `_prints/`
5. 💻 Test locally: `bundle exec jekyll serve`
6. 👀 Preview at `http://localhost:4000`
7. ✅ If happy, push to GitHub
8. 🎉 Live in 1-2 minutes!

---

## Example: Complete Workflow

Let's say you want to add a new painting called "Spring Garden":

1. **Save your image:**
   - File: `spring-garden.jpg`
   - Location: `assets/images/portfolio/spring-garden.jpg`

2. **Create markdown file:**
   - File: `_portfolio/spring-garden.md`
   - Content:
   ```markdown
   ---
   layout: portfolio-item
   title: "Spring Garden"
   category: "Paintings"
   image: "/assets/images/portfolio/spring-garden.jpg"
   featured: true
   dimensions: "18 x 24 inches"
   materials: "Acrylic on canvas"
   year: 2024
   availability: "Available"
   ---

   A vibrant spring garden bursting with colorful blooms.
   This piece captures the joy and energy of springtime.
   ```

3. **Test locally:**
   ```bash
   bundle exec jekyll serve
   ```
   Visit: http://localhost:4000

4. **Push to GitHub:**
   - Open GitHub Desktop
   - Commit: "Added Spring Garden painting"
   - Push origin

5. **Done!** Check your live site in 2 minutes! 🎉

---

## 🎨 That's It!

You now know everything you need to manage your portfolio website. Remember:
- Text files = content
- Images = visuals
- Jekyll = magic that turns them into a website
- GitHub = where it lives online

Happy creating! 🌸
