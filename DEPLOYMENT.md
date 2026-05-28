# Deployment Guide: Render & Vercel

## Prerequisites
- GitHub account with your project repository
- Render account (https://render.com)
- Vercel account (https://vercel.com)

---

## Option 1: Deploy to Render (⭐ Recommended for Flask)

Render is ideal for Flask applications and provides better support for long-running processes.

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/crop-recommendation.git
git push -u origin main
```

### Step 2: Create Render Service
1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Fill in the details:
   - **Name:** `crop-recommendation`
   - **Runtime:** Python 3.10
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Plan:** Free (or Paid)

### Step 3: Configure Environment
- Set **FLASK_ENV** to `production`
- Click **"Create Web Service"**

### Step 4: Access Your App
Your app will be available at: `https://crop-recommendation.onrender.com`

**Important:** On free tier, services spin down after 15 mins of inactivity. Upgrade to paid for always-on service.

---

## Option 2: Deploy to Vercel (For Serverless)

Vercel is best for serverless Python deployments but may have cold start delays.

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Deploy
```bash
vercel login
vercel --prod
```

### Step 3: Follow Prompts
- Confirm project scope
- Accept defaults for build settings

### Step 4: Access Your App
Your app will be available at: `https://crop-recommendation.vercel.app`

---

## Troubleshooting

### Model File Not Found
Ensure `model.pkl` is included in your repository:
```bash
git add model.pkl
git commit -m "Add trained model"
git push
```

### Module Import Errors
- Verify all dependencies are in `requirements.txt`
- Render/Vercel will install from this file automatically

### File Size Issues
If `model.pkl` is too large (>50MB):
- Consider compressing: `import joblib; joblib.dump(model, 'model.pkl', compress=3)`
- Or use cloud storage (S3, Google Cloud Storage)

### CORS Errors
If frontend is on a different domain, update `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

## Environment Variables

Create a `.env` file locally (don't commit):
```
FLASK_ENV=production
```

On Render/Vercel dashboards, add these in Settings → Environment.

---

## Database or File Storage

For persistent storage beyond deployment:
- **Render:** Connect PostgreSQL/MySQL from Render Dashboard
- **Vercel:** Use AWS S3 or similar cloud storage

---

## Testing Locally

Before deploying, test locally:
```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

---

## Updating Your Deployment

Just push changes to GitHub:
```bash
git add .
git commit -m "Your message"
git push
```

Render & Vercel will automatically redeploy!
