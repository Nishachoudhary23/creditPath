# CreditPathAI - Quick Reference Card

## 🎯 TL;DR - Quick Start with Live Server

### **Terminal 1: Start Backend (Port 5000)**
```powershell
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```
✅ Wait for: `Application startup complete`

### **VS Code: Start Frontend (Port 5500)**
1. Open `frontend/index.html`
2. Right-click → "Open with Live Server"
3. Browser opens `http://localhost:5500` automatically

✅ Done! Now use the application.

---

## 📊 Architecture at a Glance

```
Your Browser (localhost:5500)
           ↓ (HTTP Request)
         Live Server
           ↓ (Frontend files)
         index.html + script.js + style.css
           ↓ (API Call)
  http://localhost:5000 ← Backend FastAPI
           ↓
         ML Model (Logistic Regression)
           ↓ (Prediction)
         JSON Response
           ↓
         Display Results
```

---

## 🔗 URLs

| Service | URL | Port |
|---------|-----|------|
| Frontend (Live Server) | `http://localhost:5500` | 5500 |
| Backend API | `http://localhost:5000` | 5000 |
| Backend Health | `http://localhost:5000/api/health` | 5000 |

---

## 🧪 Quick Test

1. **Fill form:**
   - Name: Test User
   - Email: test@example.com
   - Phone: 9876543210
   - All other fields: realistic values

2. **Click:** "Submit Application & Assess Risk"

3. **Expected:** See results in 1-2 seconds

4. **Check:** Terminal 1 shows `POST /api/predict HTTP/1.1 200 OK`

---

## ⚠️ Common Issues & Quick Fixes

| Issue | Fix |
|-------|-----|
| "Cannot reach localhost:5000" | Check Terminal 1 - backend must be running |
| "CORS error" | Not expected; restart backend if occurs |
| "Form shows loading forever" | Check browser F12 console for errors |
| "422 Validation Error" | Fill all required fields with valid data |
| "Live Server won't start" | Right-click `index.html` (not folder) |

---

## 📂 Key Files

| File | Purpose |
|------|---------|
| `frontend/script.js` | API_URL hardcoded to `http://localhost:5000` |
| `backend/main.py` | CORS enabled, FastAPI app |
| `backend/api/routes.py` | `/api/predict` endpoint |
| `backend/logs/app.log` | Prediction logs |

---

## 💾 Configuration Reminder

✅ Frontend API URL is **already configured:**
```javascript
const API_URL = 'http://localhost:5000/api/predict';
```

✅ Backend CORS is **already enabled:**
```python
allow_origins=["*"]  # Allows localhost:5500
```

**No additional configuration needed!**

---

## 🛠️ Maintenance

### **Restart Backend**
```powershell
# In Terminal 1, press Ctrl+C, then:
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

### **Restart Frontend**
```
Live Server: Refresh browser (F5) or stop/start from extension
```

### **Check Logs**
```powershell
Get-Content 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\backend\logs\app.log' -Tail 20
```

---

## 🎓 Understanding the Setup

- **Why two servers?**
  - Frontend (Live Server) = Quick reload, dev experience
  - Backend (FastAPI) = API, ML model, data processing
  - Separate concerns = Cleaner architecture

- **Why localhost:5000 in script.js?**
  - Ensures frontend on any port connects to backend
  - Works with port 5500 (Live Server), 5000 (embedded), etc.

- **Why CORS?**
  - Allows browsers on different ports to communicate
  - `allow_origins=["*"]` = Accept from any origin

---

## ✨ What's Happening Behind the Scenes

```
User fills form on port 5500
    ↓
JavaScript collects data
    ↓
fetch() sends POST to localhost:5000
    ↓
Backend receives, validates data
    ↓
Loads ML model (Logistic Regression)
    ↓
Scales features, makes prediction
    ↓
Returns JSON with:
  - Default probability (0-1)
  - Risk band (Low/Medium/High)
  - Recommended action
    ↓
Frontend displays results
    ↓
Backend logs to app.log
```

---

## 🚨 Emergency Troubleshooting

### **Nothing is working**
```powershell
# Kill any processes on ports
taskkill /F /IM python.exe
taskkill /F /IM node.exe

# Start fresh
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

### **Live Server not working**
- Uninstall and reinstall Live Server extension
- Or use Python's built-in server:
```powershell
cd c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\frontend
python -m http.server 5500
```

### **Model not loading**
```powershell
# Retrain the model
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' backend/model/train_model.py
```

---

## 📈 Expected Performance

- **Page load:** <500ms
- **Form submission:** 1-2 seconds
- **Results display:** Instant
- **Server uptime:** 24/7 (while running)

---

## 🔐 Security Notes

- ⚠️ CORS allows all origins (development only)
- ⚠️ No authentication (local development)
- ✅ Input validation enabled
- ✅ Error messages safe

---

## 📚 Full Documentation

- **SETUP_COMPLETE.md** - Full technical docs
- **QUICK_START.md** - Complete reference
- **LIVE_SERVER_GUIDE.md** - Detailed setup guide

---

**Status:** ✅ Ready to Use
**Version:** 1.0.0
**Last Updated:** 2025-11-16
