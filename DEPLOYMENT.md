# Railway Deployment Guide for Django Online Examination System

## 🚀 Quick Deploy to Railway

### Prerequisites
- GitHub account
- Railway account (free at [railway.app](https://railway.app/))

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### Step 2: Deploy on Railway

1. **Go to [Railway.app](https://railway.app/)**
2. **Sign up/Login** with GitHub
3. **Create New Project** → **Deploy from GitHub repo**
4. **Select your repository**
5. **Configure the service:**

#### Environment Variables (Add these in Railway dashboard):
```
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://... (Railway will provide this)
ALLOWED_HOSTS=your-app-name.up.railway.app
```

#### Build Settings:
- **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command:** `gunicorn onlinexam.wsgi:application`

### Step 3: Add PostgreSQL Database

1. In Railway dashboard, go to **"Plugins"** tab
2. Click **"Add Plugin"** → **"PostgreSQL"**
3. Railway will automatically provide `DATABASE_URL` environment variable

### Step 4: Deploy!

Railway will automatically:
- Install dependencies
- Collect static files
- Run migrations
- Start your Django app

Your app will be available at: `https://your-app-name.up.railway.app`

## 🔧 Configuration Details

### Files Created/Modified:
- ✅ `Procfile` - Tells Railway how to run the app
- ✅ `requirements.txt` - Updated with production dependencies
- ✅ `runtime.txt` - Specifies Python version
- ✅ `railway.json` - Railway-specific configuration
- ✅ `build.sh` - Build script for deployment
- ✅ `.gitignore` - Excludes unnecessary files
- ✅ `settings.py` - Updated for production

### Key Changes Made:
1. **Database:** Configured to use PostgreSQL on Railway, SQLite locally
2. **Static Files:** WhiteNoise for serving static files
3. **Security:** Production security settings
4. **Environment Variables:** Configurable settings
5. **WSGI:** Gunicorn for production server

## 🛠️ Local Testing

Test your production setup locally:
```bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Test with gunicorn
gunicorn onlinexam.wsgi:application
```

## 🔍 Troubleshooting

### Common Issues:

1. **Static files not loading:**
   - Check `STATIC_ROOT` and `STATICFILES_STORAGE` in settings
   - Ensure `collectstatic` ran during build

2. **Database connection errors:**
   - Verify `DATABASE_URL` environment variable
   - Check PostgreSQL plugin is added

3. **App not starting:**
   - Check Railway logs in dashboard
   - Verify `gunicorn` is in requirements.txt
   - Check `Procfile` syntax

4. **Environment variables:**
   - Ensure all required env vars are set in Railway dashboard
   - Check `DEBUG=False` for production

### Railway Logs:
- Go to Railway dashboard → Your service → **"Deployments"** tab
- Click on latest deployment → **"View Logs"**

## 📝 Post-Deployment

### Create Superuser:
```bash
# In Railway dashboard → "Variables" → Add command:
python manage.py createsuperuser
```

### Database Migrations:
Railway automatically runs migrations during deployment, but you can manually run:
```bash
python manage.py migrate
```

## 🔒 Security Notes

- ✅ `DEBUG=False` in production
- ✅ `SECRET_KEY` from environment variable
- ✅ HTTPS enabled
- ✅ Security headers configured
- ✅ CSRF protection enabled

## 📊 Monitoring

Railway provides:
- **Real-time logs**
- **Performance metrics**
- **Uptime monitoring**
- **Automatic restarts**

## 🎉 Success!

Your Django Online Examination System is now live on Railway! 🚀

**Next Steps:**
1. Test all functionality
2. Set up custom domain (optional)
3. Configure email settings for production
4. Set up monitoring and alerts

---

**Need Help?**
- [Railway Documentation](https://docs.railway.app/)
- [Django Deployment Guide](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [WhiteNoise Documentation](https://whitenoise.evans.io/en/stable/) 