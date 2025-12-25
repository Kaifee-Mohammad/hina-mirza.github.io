# CMS Setup Guide - WordPress-Like Admin Panel

Your site now has a **WordPress-like CMS** built in! Hina can manage all content through a visual web interface.

## 🎯 What's Installed

**Netlify CMS (Decap CMS)** - A free, open-source content management system that provides:
- Visual editor (like WordPress)
- Drag-and-drop image uploads
- No need to edit code or markdown
- Works directly in the browser

---

## 🚀 Setup Steps

### Step 1: Deploy to Netlify (Required)

The CMS needs to be hosted on Netlify to work properly. Here's how:

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Added CMS system"
   git push
   ```

2. **Go to Netlify:**
   - Visit: https://www.netlify.com
   - Click "Sign up" (use GitHub account)
   - Click "Add new site" → "Import an existing project"
   - Choose GitHub → Select your repository
   - Click "Deploy site"

3. **Wait 2-3 minutes** for deployment to complete

### Step 2: Enable Netlify Identity

1. In Netlify dashboard, go to your site
2. Click "Identity" in the top menu
3. Click "Enable Identity"
4. Under "Registration preferences", select "Invite only"
5. Click "Invite users" → Enter Hina's email
6. She'll receive an email invitation

### Step 3: Enable Git Gateway

1. Still in "Identity" settings
2. Scroll to "Services" → "Git Gateway"
3. Click "Enable Git Gateway"
4. Done!

---

## 🎨 How Hina Uses the CMS

### Accessing the Admin Panel

1. **Go to:** `https://yoursite.netlify.app/admin/`
2. **Log in** with email (first time: create password via invitation email)
3. **Welcome to your CMS!** 🎉

### Adding New Portfolio Item

1. Click **"Portfolio"** in sidebar
2. Click **"New Portfolio"** button
3. Fill in the form:
   - **Title:** Name of artwork
   - **Category:** Choose from dropdown
   - **Featured Image:** Click to upload image
   - **Dimensions, Materials, Year:** Fill in details
   - **Availability:** Choose from dropdown
   - **Description:** Write about the artwork
4. Click **"Publish"** → Changes go live instantly!

### Adding New Art Print

1. Click **"Art Prints"** in sidebar
2. Click **"New Art Prints"**
3. Fill in:
   - Title
   - Image (upload)
   - Price Range (e.g., "$45 - $120")
   - Available Sizes
   - Material type
   - Description
4. Click **"Publish"**

### Editing Existing Content

1. Click **"Portfolio"** or **"Art Prints"**
2. Click on any item to edit
3. Make changes
4. Click **"Publish"** to save

### Editing Pages (About, Contact)

1. Click **"Pages"** in sidebar
2. Choose "About Page" or "Contact Page"
3. Edit content using rich text editor
4. Click **"Publish"**

### Uploading Images

- **Drag and drop** images into upload area
- Or click **"Choose an image"** to browse
- Images automatically resize and optimize
- All images stored in `/assets/images/uploads/`

---

## 📱 Features

### Rich Text Editor
- Bold, italic, headings
- Bullet lists, numbered lists
- Links
- WYSIWYG (What You See Is What You Get)

### Image Management
- Drag & drop uploads
- Image library
- Automatic optimization
- Preview before publishing

### Publishing
- **Save Draft** - Save without publishing
- **Publish** - Goes live immediately (1-2 min)
- **Delete** - Remove content
- **Unpublish** - Take offline without deleting

---

## 🔐 Security

- **Login required** - Only invited users can access
- **Git-based** - All changes tracked in GitHub
- **Backup** - Every change is a Git commit
- **Rollback** - Can undo any change via GitHub

---

## 🆘 Troubleshooting

### "Cannot access admin"
- Make sure site is deployed to Netlify (not just localhost)
- Check that Identity is enabled
- Check that Git Gateway is enabled

### "Login not working"
- Check invitation email (might be in spam)
- Try password reset if needed
- Contact Netlify support if issues persist

### "Changes not appearing"
- Wait 1-2 minutes for Netlify to rebuild
- Hard refresh browser (Cmd+Shift+R / Ctrl+F5)
- Check "Deploys" in Netlify dashboard

### "Can't upload images"
- Check file size (keep under 2MB)
- Use JPG or PNG format
- Make sure image has valid filename

---

## 💡 Tips for Hina

✅ **Always click "Publish"** after making changes
✅ **Images:** Use good quality photos (but not too large!)
✅ **Descriptions:** Keep them engaging but concise
✅ **Save drafts** if you're not ready to publish
✅ **Preview** before publishing to check how it looks

---

## 📊 Comparison: Before vs After

### Before (Manual)
- Edit markdown files
- Use command line
- Upload images via folder
- Push to GitHub manually

### After (CMS)
- Visual editor (like WordPress!)
- Click buttons
- Drag-drop images
- Instant publishing

---

## 🌐 Local Development (Optional)

To test CMS locally before deploying:

1. Uncomment this line in `admin/config.yml`:
   ```yaml
   local_backend: true
   ```

2. Install local backend:
   ```bash
   npx netlify-cms-proxy-server
   ```

3. In another terminal:
   ```bash
   bundle exec jekyll serve
   ```

4. Visit: http://localhost:4000/admin/

---

## 🎉 Summary

Your site now has a **full CMS** like WordPress!

**What Hina needs to do:**
1. Wait for you to deploy to Netlify
2. Accept email invitation
3. Set password
4. Go to `yoursite.netlify.app/admin/`
5. Start creating! 🎨

**What she can do:**
✅ Add/edit portfolio items
✅ Add/edit art prints
✅ Upload images
✅ Edit About/Contact pages
✅ All through web interface - NO CODE!

---

## 📞 Next Steps

1. **You:** Push code to GitHub and deploy to Netlify
2. **You:** Enable Identity and Git Gateway in Netlify
3. **You:** Invite Hina via her email
4. **Hina:** Accept invitation and set password
5. **Hina:** Start managing content at `/admin/`!

That's it! 🚀
