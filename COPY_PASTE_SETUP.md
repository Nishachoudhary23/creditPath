# 🎬 EXACT STEPS TO RUN - Copy & Paste

## 🖥️ Terminal 1: Backend Server

### Command to Copy:
```powershell
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI' ; & 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

### What You'll See:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
==================================================
CreditPathAI API running...
==================================================
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

✅ **KEEP THIS TERMINAL OPEN - Don't close it!**

---

## 🌐 VS Code: Frontend (Live Server)

### Steps:
1. Open VS Code
2. In Explorer on the left, find: **`frontend` folder**
3. Click on **`index.html`** inside frontend folder
4. **Right-click** on index.html
5. Select **"Open with Live Server"**

### What Happens:
- Browser opens automatically
- Shows: `http://localhost:5500` (or similar)
- You see the loan application form

### If Right-Click Menu Doesn't Show "Open with Live Server":
- Open Extensions (left sidebar, icon with 4 squares)
- Search: "Live Server"
- Click "Install"
- Then try right-click again

---

## 📋 Form to Test With

Copy and paste these values:

```
Full Name: John Doe
Email: john@example.com
Phone: 9876543210
City: Mumbai
State: Maharashtra
Pincode: 400001
Address: 123 Main Street

Employment Status: Salaried
Employer Name: TCS
Work Experience: 5
Monthly Income: 150000

Loan Purpose: Home Purchase
Loan Amount: 500000
Loan Term: 60

Annual Income: 1800000
DTI: 25
Open Accounts: 10
Total Accounts: 12
Credit Age: 5
Revolving Utilization: 30
Existing Loans: 1
```

---

## ✅ Expected Results

### Browser (Frontend):
```
RISK ASSESSMENT RESULTS

Applicant: John Doe
Email: john@example.com
Phone: 9876543210
Loan Purpose: Home Purchase
Loan Amount: 500,000

Default Probability: 25.45%
Risk Level: LOW
Recommended Action: Standard Reminder
```

### Terminal 1 (Backend):
```
2025-11-16 HH:MM:SS,XXX - CreditPathAI - INFO - Received prediction request for: John Doe
2025-11-16 HH:MM:SS,XXX - CreditPathAI - INFO - Input: {...} | Probability: 0.2545 | Risk: Low | Action: Standard Reminder
INFO:     127.0.0.1:xxxxx - "POST /api/predict HTTP/1.1" 200 OK
```

---

## 🔄 If Backend Crashes

### Step 1: Press Ctrl+C in Terminal 1
```
(terminates the server)
```

### Step 2: Run command again:
```powershell
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI' ; & 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

### Step 3: Wait for "Application startup complete"

---

## 🔄 If Live Server Crashes

### Option 1: Reload Browser
```
Press F5 in browser
or
Click reload button
```

### Option 2: Stop and Restart Live Server
1. Click "Go Live" button in bottom right (VS Code)
2. It will turn off (button disappears or changes)
3. Wait 2 seconds
4. Right-click `index.html` again
5. Select "Open with Live Server"

---

## 🧪 Test Multiple Predictions

### Test Case 1: LOW RISK
```
Full Name: Alice Smith
Email: alice@example.com
Phone: 9123456789
City: Bangalore
State: Karnataka
Pincode: 560001
Address: Tech Park
Employment: Salaried
Employer: Infosys
Experience: 8
Monthly Income: 200000
Loan Purpose: Home Purchase
Loan Amount: 300000
Loan Term: 84
Annual Income: 2400000
DTI: 15
Open Accounts: 15
Total Accounts: 18
Credit Age: 12
Revolving Util: 20
Existing Loans: 0

✅ EXPECTED: LOW RISK (0-30% probability)
```

### Test Case 2: HIGH RISK
```
Full Name: Bob Johnson
Email: bob@example.com
Phone: 9987654321
City: Delhi
State: Delhi
Pincode: 110001
Address: Market Street
Employment: Self-Employed
Employer: Startup
Experience: 1.5
Monthly Income: 30000
Loan Purpose: Debt Consolidation
Loan Amount: 800000
Loan Term: 36
Annual Income: 300000
DTI: 75
Open Accounts: 3
Total Accounts: 5
Credit Age: 1.5
Revolving Util: 90
Existing Loans: 3

⚠️ EXPECTED: HIGH RISK (60-100% probability)
```

---

## 📱 Browser Console Debugging (F12)

### If Something Goes Wrong:
1. In browser, press **F12**
2. Click **"Console"** tab
3. Look for red error messages
4. Also check **"Network"** tab:
   - Find POST request to `http://localhost:5000/api/predict`
   - Click it
   - Check "Response" tab for data

### Common Console Errors:

**Error:** "Failed to fetch"
```
Fix: Backend not running - check Terminal 1
```

**Error:** "CORS policy"
```
Fix: Should not happen - restart backend
```

**Error:** "Cannot read property 'xxx' of undefined"
```
Fix: Check form is filled properly
```

---

## ⚡ Performance Tips

1. **Keep Both Running:** Don't close either terminal/server
2. **Edit Frontend:** Live Server auto-reloads (no refresh needed)
3. **Edit Backend:** Restart backend (Ctrl+C and re-run)
4. **Check Logs:** Open `backend/logs/app.log` for details
5. **Network Speed:** Should be <2 seconds per prediction

---

## 🎯 Summary of Ports

| Application | Port | URL |
|---|---|---|
| Frontend (Live Server) | 5500 | `http://localhost:5500` |
| Backend (FastAPI) | 5000 | `http://localhost:5000` |
| API Calls | 5000 | `http://localhost:5000/api/predict` |

---

## 📂 Important Files

```
Terminal 1 (Backend Server):
  c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\backend\main.py
  c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\backend\model\model.pkl

Browser (Frontend):
  c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\frontend\index.html
  c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\frontend\script.js
  (API URL in script.js: line 8)

Logs:
  c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\backend\logs\app.log
```

---

## ✨ What's Fixed

✅ **API URL in script.js** - Changed from `window.location.origin` to `http://localhost:5000`
✅ **CORS in backend** - Already enabled (allow_origins=["*"])
✅ **Port 5000** - Backend server
✅ **Port 5500** - Live Server for frontend
✅ **Communication** - Works across different ports

---

## 🎉 YOU'RE READY!

Just follow the 2 main steps:
1. **Terminal 1:** Run backend command (keep it open)
2. **VS Code:** Right-click `frontend/index.html` → Open with Live Server

Done! The application is working! 🚀

---

## 🆘 Emergency Reset

If everything breaks:

```powershell
# Kill Python processes
taskkill /F /IM python.exe

# Start fresh
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

Then restart Live Server in VS Code.

---

**Status:** ✅ READY TO USE
**Version:** 1.0.0
**Last Updated:** 2025-11-16
