# CreditPathAI - Live Server Setup Guide

## ✅ Quick Setup with VS Code Live Server

This guide explains how to run CreditPathAI with VS Code's Live Server extension.

---

## 📋 Prerequisites

1. **VS Code Live Server Extension** - Install from VS Code Extensions
2. **Backend Running** - FastAPI server on port 5000
3. **Python Environment** - Already configured

---

## 🚀 Two-Server Architecture

Your application uses **two separate servers**:

```
┌─────────────────────────────────────────────────────────┐
│                    CreditPathAI                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Frontend Server (Live Server)  │  Backend Server      │
│   PORT: 5500                    │  (FastAPI)           │
│  Location: frontend/            │  PORT: 5000          │
│  - index.html                  │  - API endpoints     │
│  - script.js                   │  - ML Model          │
│  - style.css                   │  - Predictions       │
│                                 │                      │
│  http://localhost:5500          │  http://localhost:5000
└─────────────────────────────────────────────────────────┘

Communication: frontend → backend via API calls
```

---

## 🎯 Step-by-Step Setup

### **Step 1: Start the Backend Server**

Open **Terminal 1** in VS Code and run:

```powershell
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

**Expected Output:**
```
INFO:     Started server process [PID]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

✅ Backend is ready on `http://localhost:5000`

---

### **Step 2: Start the Frontend with Live Server**

1. **Open the frontend folder:**
   - In VS Code Explorer, navigate to `frontend/` folder
   - Click on `index.html`

2. **Launch Live Server:**
   - Right-click on `index.html`
   - Select **"Open with Live Server"**
   - Or press `Alt + L, Alt + O`

**Expected Result:**
- Browser opens automatically to `http://localhost:5500`
- You should see the CreditPathAI form

✅ Frontend is ready on `http://localhost:5500`

---

## 📝 How It Works

### **API Configuration**
The frontend is configured to send requests to the backend:

**Location:** `frontend/script.js` (Line 8)
```javascript
const API_URL = 'http://localhost:5000/api/predict';
```

This hardcoded URL ensures that:
- ✅ Frontend on port 5500 connects to backend on port 5000
- ✅ No routing conflicts
- ✅ Works with Live Server auto-reload

### **CORS Settings**
The backend allows requests from all origins (CORS enabled):
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains including localhost:5500
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ✨ Using the Application

### **1. Fill the Form**
- Complete all required fields (marked with *)
- Use realistic values for predictions

### **2. Click Submit**
- Button: "Submit Application & Assess Risk"
- Form data is sent to backend API

### **3. View Results**
- Default probability calculated
- Risk band assigned (Low/Medium/High)
- Recommended action displayed

### **4. Check Logs**
Terminal 1 (Backend) shows:
```
INFO:     127.0.0.1:55297 - "POST /api/predict HTTP/1.1" 200 OK
2025-11-16 16:28:40,938 - CreditPathAI - INFO - Input: {...} | Probability: 0.9892 | Risk: High
```

---

## 🔧 Troubleshooting

### **Issue: "Cannot reach http://localhost:5000"**

**Solution:**
1. Check Terminal 1 - Backend should show "Application startup complete"
2. If not running, start it with the command from Step 1
3. Verify port 5000 is not blocked by firewall

### **Issue: Form shows loading but nothing happens**

**Solution:**
1. Open browser console (F12)
2. Check Console tab for errors
3. Should show POST request to `http://localhost:5000/api/predict`
4. If failing, backend might not be running

### **Issue: "Error: 422 Unprocessable Entity"**

**Solution:**
1. Verify all required fields are filled
2. Check field formats:
   - Email must be valid (user@domain.com)
   - Phone must have 10+ digits
   - Pincode must be 6 digits
3. Numeric fields must have numbers

### **Issue: "CORS error" in console**

**Solution:**
- This shouldn't happen as CORS is enabled
- If it occurs, restart backend server:
  1. Press `Ctrl+C` in Terminal 1
  2. Run the backend command again (Step 1)

### **Issue: Live Server won't start**

**Solution:**
1. Ensure Live Server extension is installed
2. Right-click on `index.html` (not folder)
3. Select "Open with Live Server"
4. Check VS Code extensions are enabled

---

## 📊 What's Running Where

| Component | Location | Port | Status |
|-----------|----------|------|--------|
| **Frontend** | frontend/ | 5500 | Live Server |
| **Backend** | backend/ | 5000 | FastAPI/Uvicorn |
| **Model** | backend/model/model.pkl | - | Loaded in memory |
| **Logs** | backend/logs/app.log | - | File based |

---

## 🔄 Workflow

```
User opens: http://localhost:5500 (Live Server)
                    ↓
          Fills application form
                    ↓
          Clicks "Submit Application"
                    ↓
          Frontend sends POST request
          to http://localhost:5000/api/predict
                    ↓
          Backend receives request
          Loads ML model
          Processes financial data
                    ↓
          Returns prediction:
          {
            "applicant_name": "...",
            "probability": 0.9892,
            "risk_band": "High",
            "action": "Priority Collection",
            ...
          }
                    ↓
          Frontend displays results
          to user
                    ↓
          Logs saved to:
          backend/logs/app.log
```

---

## 💡 Pro Tips

1. **Auto-reload:** Live Server will auto-reload when you edit frontend files
2. **Backend Changes:** Backend changes require manual restart (Ctrl+C and re-run)
3. **Console Debugging:** Press F12 in browser to see:
   - Network requests
   - Response data
   - Any JavaScript errors
4. **Server Logs:** Terminal 1 shows backend activity in real-time
5. **Separate Terminals:** Keep backend in Terminal 1, use Terminal 2 for other commands

---

## 📁 File Structure

```
c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\
│
├── backend/                    (API server - port 5000)
│   ├── main.py                (FastAPI app)
│   ├── api/
│   │   ├── routes.py         (API endpoints)
│   │   └── schema.py         (Data validation)
│   ├── model/
│   │   ├── train_model.py    (Training script)
│   │   ├── model_loader.py   (Load model)
│   │   └── model.pkl         (ML model)
│   ├── utils/
│   │   ├── recommendation.py (Risk classification)
│   │   └── logger.py         (Logging)
│   └── logs/
│       └── app.log           (Application logs)
│
├── frontend/                   (Web UI - port 5500 via Live Server)
│   ├── index.html            (Main page)
│   ├── script.js             (Frontend logic)
│   └── style.css             (Styling)
│
└── Configuration files
    ├── pyproject.toml
    ├── SETUP_COMPLETE.md
    ├── QUICK_START.md
    └── README.md
```

---

## ✅ Verification Checklist

Before testing:
- [ ] Backend terminal shows "Application startup complete"
- [ ] Live Server opened `index.html` on port 5500
- [ ] Browser shows the loan application form
- [ ] No console errors (F12 to check)
- [ ] Can type in form fields

Ready to test:
- [ ] Fill all required form fields
- [ ] Click "Submit Application & Assess Risk"
- [ ] Check Terminal 1 for request log
- [ ] See results appear on page

---

## 🎓 Learning Points

- **Frontend-Backend Separation:** Two servers working together
- **API Communication:** HTTP POST requests with JSON
- **CORS:** Cross-Origin Resource Sharing enabled
- **Async Operations:** Frontend waits for API response
- **Error Handling:** Graceful error messages to user

---

## 📞 Need Help?

Check these in order:
1. **Browser Console (F12):** JavaScript errors
2. **Terminal 1:** Backend server status and logs
3. **backend/logs/app.log:** Detailed application logs
4. **SETUP_COMPLETE.md:** Full technical documentation
5. **QUICK_START.md:** Quick reference guide

---

**Version:** 1.0.0
**Status:** ✅ Ready to Use
**Last Updated:** 2025-11-16
