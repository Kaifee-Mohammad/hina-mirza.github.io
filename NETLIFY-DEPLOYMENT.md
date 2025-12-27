# Complete Netlify Deployment Guide

Follow these steps exactly to deploy your site to Netlify and enable the CMS.

---

## Part 1: Deploy Site to Netlify (5 minutes)

### Step 1: Create Netlify Account

1. Open your browser and go to: **https://www.netlify.com**
2. Click the **"Sign up"** button (top right)
3. Choose **"GitHub"** to sign up with your GitHub account
4. Click **"Authorize Netlify"** when GitHub asks for permission
5. You'll be redirected to your Netlify dashboard

### Step 2: Import Your Repository

1. In the Netlify dashboard, click the big **"Add new site"** button
   - Or click **"Sites"** in the left sidebar → **"Add new site"**

2. Choose **"Import an existing project"**

3. Click **"Deploy with GitHub"**
   - If asked, click **"Authorize Netlify"** again

4. **Find your repository:**
   - You'll see a list of your repositories
   - Search for: **"hina-mirza.github.io"**
   - Click on it to select it

5. **Configure build settings:**
   - Netlify should auto-detect these (you'll see them pre-filled):
   ```
   Build command: bundle exec jekyll build
   Publish directory: _site
   ```
   - If they're empty, type them in exactly as shown above
   - Leave everything else as default

6. Click the big **"Deploy hina-mirza.github.io"** button at the bottom

7. **Wait for deployment:**
   - You'll see a deployment in progress
   - Wait 2-3 minutes (watch the logs if you're curious!)
   - When done, you'll see: **"Published"** with a green checkmark ✓

8. **Your site is live!**
   - Netlify gives you a random URL like: `wonderful-curie-123abc.netlify.app`
   - Click the URL to see your live site!
   - (You can change this URL later)

---

## Part 2: Enable CMS Access (5 minutes)

Now let's enable the WordPress-like admin panel:

### Step 3: Enable Netlify Identity

1. In your Netlify site dashboard, look at the top menu bar
2. Click **"Identity"** (between "Site settings" and "Domain management")

3. You'll see: **"Enable Identity"**
4. Click the **"Enable Identity"** button

5. **Configure registration:**
   - Scroll down to **"Registration preferences"**
   - Click **"Edit settings"**
   - Select: **"Invite only"** (recommended for security)
   - Click **"Save"**

### Step 4: Enable Git Gateway

1. Still on the Identity page, scroll down to the **"Services"** section
2. You'll see **"Git Gateway"** with status: "Not enabled"
3. Click **"Enable Git Gateway"**
4. Confirm if asked

**Important:** Git Gateway allows the CMS to save changes back to GitHub!

### Step 5: Invite Hina to Use the CMS

1. Still on the Identity page, at the top
2. Click the **"Invite users"** button
3. Enter Hina's email address
4. Click **"Send"** or **"Invite"**

**What happens next:**
- Hina receives an email invitation
- She clicks the link in the email
- She sets her password
- She can now access the CMS!

---

## Part 3: Access the CMS

### Step 6: Find Your Admin URL

Your CMS admin panel is at:
```
https://YOUR-SITE-NAME.netlify.app/admin/
```

**To find YOUR-SITE-NAME:**
1. In Netlify dashboard, look at the top
2. You'll see something like: **wonderful-curie-123abc.netlify.app**
3. Copy that URL and add `/admin/` at the end

**Example:**
- If your site is: `wonderful-curie-123abc.netlify.app`
- Admin panel is: `wonderful-curie-123abc.netlify.app/admin/`

### Step 7: Hina Logs In for First Time

1. **Hina checks her email** (check spam folder too!)
2. **Clicks the invitation link** in the email
3. **Sets a password** (make it strong!)
4. **She's automatically logged into the CMS** 🎉

### Step 8: Using the CMS

Once logged in, Hina will see the CMS interface with:

- **Portfolio** (left sidebar)
  - Click "New Portfolio" to add artwork
  - Click existing items to edit them

- **Art Prints** (left sidebar)
  - Click "New Art Prints" to add prints
  - Click existing items to edit them

- **Pages** (left sidebar)
  - Edit About page
  - Edit Contact page

**To add new artwork:**
1. Click **"Portfolio"** in sidebar
2. Click **"New Portfolio"**
3. Fill in the form:
   - Title
   - Category (dropdown)
   - Click "Featured Image" to upload
   - Fill in dimensions, materials, etc.
   - Write description
4. Click **"Publish"**
5. Changes go live in 1-2 minutes!

---

## Part 4: Optional - Custom URL

### Change Your Netlify URL (Optional)

The random URL like `wonderful-curie-123abc.netlify.app` can be changed:

1. In Netlify dashboard → **"Domain management"**
2. Click **"Options"** → **"Edit site name"**
3. Change to: **hina-mirza** (if available)
4. Save
5. Your new URL: `hina-mirza.netlify.app`

---

## 🆘 Troubleshooting

### "Build failed" Error

If deployment fails:

1. Click on the failed deploy
2. Look at the logs (scroll down)
3. Common issues:
   - **Bundler error:** Should be fixed (we updated it)
   - **Ruby version:** Should be fixed (set to 3.2.2)
   - **Missing gems:** Netlify will auto-install

If you see an error, copy it and send it to me!

### "Cannot access /admin/" Error

Make sure:
- ✓ Site is deployed successfully (check Deploy log)
- ✓ Identity is enabled (check Identity tab)
- ✓ Git Gateway is enabled (check Services section)
- ✓ Using the correct URL (ends with `/admin/`)

### "No login button" Error

1. Hard refresh: Press `Cmd + Shift + R` (Mac) or `Ctrl + F5` (Windows)
2. Clear browser cache
3. Make sure Identity is enabled in Netlify

### "Invitation email not received"

1. Check spam/junk folder
2. In Netlify → Identity → Click user → **"Resend invitation"**
3. Try a different email address

---

## ✅ Success Checklist

After following all steps, you should have:

- [ ] Netlify account created
- [ ] Site deployed successfully
- [ ] Site is live at a .netlify.app URL
- [ ] Identity is enabled
- [ ] Git Gateway is enabled
- [ ] Hina invited via email
- [ ] Can access /admin/ page
- [ ] Hina can log in
- [ ] Hina can add/edit content

---

## 🎯 Quick Summary

1. **Netlify.com** → Sign up with GitHub
2. **Add new site** → Import from GitHub
3. Select **hina-mirza.github.io** repo
4. Click **Deploy** → Wait 2-3 mins
5. Click **Identity** → Enable Identity
6. Scroll down → **Enable Git Gateway**
7. Click **Invite users** → Add Hina's email
8. Hina gets email → Sets password
9. Go to: `your-site.netlify.app/admin/`
10. Start creating! 🎨

---

Need help with any specific step? Just let me know which part you're stuck on!
