# CreditPathAI - Quick Start Guide

## 🚀 Current Status: RUNNING & READY

### Access the Application
```
🌐 Frontend: http://localhost:5000
🔧 API Docs: http://localhost:5000/docs (if available)
```

---

## ⚡ Quick Commands

### **Start the Server** (if not running)
```powershell
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

### **Train the Model** (if needed)
```powershell
cd 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
& 'C:\Users\hp\Downloads\CreditPathAI\.venv\Scripts\python.exe' backend/model/train_model.py
```

### **View Logs**
```powershell
Get-Content 'c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\backend\logs\app.log' -Tail 50
```

---

## 📋 Form Fields Explained

### **Personal Information**
| Field | Format | Example |
|-------|--------|---------|
| Full Name | Text | John Doe |
| Email | Email | john@example.com |
| Phone | 10+ digits | 9876543210 |
| City | Text | Mumbai |
| State | Text | Maharashtra |
| Pincode | 6 digits | 400001 |
| Address | Text | 123 Main Street |

### **Employment Details**
| Field | Format | Example |
|-------|--------|---------|
| Status | Dropdown | Salaried |
| Employer | Text | TCS |
| Experience | Years | 5 |
| Monthly Income | Currency | 150000 |

### **Loan Information**
| Field | Format | Range |
|-------|--------|-------|
| Purpose | Dropdown | Home/Car/Personal/etc |
| Amount | Currency | 10,000+ |
| Term | Months | 1-360 |

### **Financial Indicators**
| Field | Format | Range |
|-------|--------|-------|
| Annual Income | Currency | Must be >0 |
| DTI Ratio | % | 0-100 |
| Open Accounts | Number | 1+ |
| Total Accounts | Number | 1+ |
| Credit Age | Years | 0.1+ |
| Revolving Util | % | 0-100 |
| Existing Loans | Number | 0+ |

---

## 🎯 Expected Outcomes

### **Low Risk (0-30%)**
✅ Standard Reminder
- Strong financial profile
- High income relative to loan
- Low DTI
- Good credit history
- Action: Regular payment reminders

### **Medium Risk (30-60%)**
⚠️ Personalized Call
- Moderate financial profile
- Some concerns noted
- Action: Call and discuss options

### **High Risk (60-100%)**
❌ Priority Collection
- Multiple risk factors present
- High DTI relative to income
- Limited credit history
- High revolving utilization
- Action: Intensive collection efforts

---

## 🔍 Example Test Submission

**Low Risk Case:**
- Name: Sarah Johnson
- Email: sarah.j@email.com
- Phone: 9123456789
- Location: Bangalore, Karnataka 560001
- Employment: Salaried at Infosys, 6 years
- Monthly Income: ₹200,000
- Loan: ₹300,000 for Car Purchase, 48 months
- Annual Income: ₹2,400,000
- DTI: 20%
- Open Accounts: 12
- Total Accounts: 15
- Credit Age: 10 years
- Revolving Util: 25%
- Existing Loans: 1

**Expected:** ✅ LOW RISK

---

## ⚠️ Common Issues & Solutions

### **"Cannot connect to localhost:5000"**
- ✅ Check if server is running
- ✅ Verify port 5000 is available
- ✅ Check Windows Firewall settings

### **"Invalid email format" Error**
- ✅ Use proper email: user@domain.com
- ✅ Check for spaces in email

### **"Pincode must be 6 digits"**
- ✅ Enter exactly 6 digits
- ✅ No spaces or special characters

### **"Validation Failed" Error**
- ✅ Fill all required fields (marked with *)
- ✅ Ensure numeric fields have numbers
- ✅ Check field formats

---

## 📊 System Information

- **Backend Framework:** FastAPI
- **Server Port:** 5000
- **Database:** None (Stateless)
- **ML Model:** Logistic Regression
- **Response Time:** <500ms typically
- **Max Concurrent Users:** Limited by server capacity

---

## 📞 Support Checklist

If something isn't working:
1. ✓ Server is running (check terminal)
2. ✓ Port 5000 is not blocked
3. ✓ All required packages installed
4. ✓ Model file exists (backend/model/model.pkl)
5. ✓ Check logs: backend/logs/app.log

---

## 🎓 What Gets Logged

Every prediction logs:
- **Timestamp:** When prediction was made
- **Applicant:** Name and email
- **Financial Data:** Loan amount, income, DTI, etc.
- **Prediction:** Default probability
- **Classification:** Risk band (Low/Medium/High)
- **Recommendation:** Suggested action

---

## 🔗 API Reference

### **POST /api/predict**
Single borrower assessment
- Input: BorrowerInput JSON
- Output: PredictionResponse JSON
- Status: 200 (success) or 422 (validation error)

### **GET /api/health**
Server health check
- Output: `{"status": "ok", "model_loaded": true}`

---

## 📁 Important Files

```
Project Root: c:\Users\hp\Downloads\CreditPathAI\CreditPathAI\

Key Files:
├── backend/main.py               ← FastAPI app
├── backend/api/routes.py         ← Endpoints
├── backend/model/model.pkl       ← ML model
├── backend/logs/app.log          ← Application logs
├── frontend/index.html           ← Web interface
└── SETUP_COMPLETE.md             ← Full documentation
```

---

## ✨ Features Included

✅ Real-time loan risk prediction
✅ Machine learning classification
✅ REST API endpoints
✅ Web-based user interface
✅ Comprehensive logging
✅ Input validation
✅ Risk-based recommendations
✅ Batch prediction support

---

**Version:** 1.0.0
**Status:** ✅ Production Ready
**Last Update:** 2025-11-16
