# CreditPathAI - Project Demo Guide

## What is CreditPathAI?

CreditPathAI is an intelligent loan default risk prediction system that uses machine learning to assess the likelihood of borrower default. The system analyzes borrower financial data and provides risk-based recommendations for collection strategies.

## System Architecture

### Full Pipeline Flow

1. **Frontend** → User enters borrower information (loan amount, income, DTI, etc.)
2. **API Layer** → FastAPI receives and validates input data using Pydantic schemas
3. **Data Processing** → Input is converted to DataFrame and scaled using StandardScaler
4. **ML Model** → Logistic Regression model predicts default probability
5. **Recommendation Engine** → Maps probability to risk band (Low/Medium/High) and suggests action
6. **Logging** → All predictions are logged with timestamps
7. **Response** → JSON response sent back to frontend with results
8. **Display** → Results displayed in user-friendly format

### Technology Stack

- **Backend**: FastAPI, Python 3.11
- **ML**: scikit-learn (Logistic Regression), SMOTE for class balancing
- **Data**: pandas, numpy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Logging**: Python logging with rotating file handler

## API Endpoints

### 1. POST /api/predict
Single borrower prediction

**Request:**
```json
{
  "loan_amnt": 250000,
  "annual_inc": 600000,
  "dti": 35.5,
  "open_acc": 8,
  "credit_age": 5.2,
  "revol_util": 45.3
}
```

**Response:**
```json
{
  "probability": 0.2456,
  "risk_band": "Low",
  "action": "Standard Reminder",
  "input_data": {
    "loan_amnt": 250000,
    "annual_inc": 600000,
    "dti": 35.5,
    "open_acc": 8,
    "credit_age": 5.2,
    "revol_util": 45.3
  }
}
```

### 2. POST /api/predict_batch
Batch prediction for multiple borrowers

**Request:**
```json
{
  "borrowers": [
    {
      "loan_amnt": 250000,
      "annual_inc": 600000,
      "dti": 35.5,
      "open_acc": 8,
      "credit_age": 5.2,
      "revol_util": 45.3
    },
    {
      "loan_amnt": 500000,
      "annual_inc": 400000,
      "dti": 55.8,
      "open_acc": 3,
      "credit_age": 2.1,
      "revol_util": 78.5
    }
  ]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "probability": 0.2456,
      "risk_band": "Low",
      "action": "Standard Reminder",
      "input_data": {...}
    },
    {
      "probability": 0.7823,
      "risk_band": "High",
      "action": "Priority Collection",
      "input_data": {...}
    }
  ]
}
```

### 3. GET /api/health
Health check endpoint

**Response:**
```json
{
  "status": "ok",
  "model_loaded": true
}
```

## Risk Band Classification

| Probability Range | Risk Band | Recommended Action |
|------------------|-----------|-------------------|
| 0.0 - 0.3 | Low | Standard Reminder |
| 0.3 - 0.6 | Medium | Personalized Call |
| 0.6 - 1.0 | High | Priority Collection |

## How to Run the Project

### Step 1: Train the Model
```bash
python backend/model/train_model.py
```

This will:
- Generate synthetic dataset
- Apply preprocessing and SMOTE
- Train Logistic Regression model
- Evaluate accuracy and ROC-AUC
- Save model.pkl

### Step 2: Start the Backend
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 5000 --reload
```

The API will be available at: `http://localhost:5000`

### Step 3: Open the Frontend
Open your browser and navigate to:
```
http://localhost:5000
```

The frontend will automatically load and connect to the API.

## 5-Step Demo Script for Presentation

### Step 1: Introduction (1 minute)
"Welcome to CreditPathAI - an intelligent loan default risk prediction system. This system helps financial institutions make data-driven decisions about loan collection strategies by predicting default probability and recommending appropriate actions."

### Step 2: System Overview (2 minutes)
"Our system uses a trained Logistic Regression model that analyzes six key borrower features:
- Loan Amount
- Annual Income
- Debt-to-Income Ratio
- Number of Open Accounts
- Credit History Age
- Revolving Credit Utilization

The model was trained on 10,000 synthetic records with SMOTE for class balancing, achieving strong accuracy and ROC-AUC scores."

### Step 3: Live Demo - Low Risk Case (2 minutes)
Enter the following data:
- Loan Amount: 200000
- Annual Income: 800000
- DTI: 25
- Open Accounts: 10
- Credit Age: 8
- Revolving Utilization: 30

**Expected Result:** Low risk, Standard Reminder

"This borrower has a strong financial profile with low DTI and high income. The system classifies them as low risk and recommends standard reminder procedures."

### Step 4: Live Demo - High Risk Case (2 minutes)
Enter the following data:
- Loan Amount: 800000
- Annual Income: 300000
- DTI: 65
- Open Accounts: 2
- Credit Age: 1.5
- Revolving Utilization: 85

**Expected Result:** High risk, Priority Collection

"This borrower shows multiple risk factors: high loan amount relative to income, high DTI, limited credit history, and high revolving utilization. The system flags them for priority collection."

### Step 5: Technical Highlights & Q&A (3 minutes)
"Key technical features:
- ✅ Real-time predictions via FastAPI
- ✅ Input validation with Pydantic
- ✅ Comprehensive logging system
- ✅ Batch prediction support
- ✅ Responsive web interface
- ✅ CORS-enabled for integration

The system is production-ready and can be easily integrated with existing loan management systems through our REST API."

## Project Structure

```
CreditPathAI/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── api/
│   │   ├── routes.py          # API endpoints
│   │   └── schema.py          # Pydantic models
│   ├── model/
│   │   ├── train_model.py     # Model training script
│   │   ├── model_loader.py    # Model loading utility
│   │   └── model.pkl          # Trained model
│   ├── utils/
│   │   ├── recommendation.py  # Risk band logic
│   │   └── logger.py          # Logging system
│   └── logs/
│       └── app.log            # Application logs
├── frontend/
│   ├── index.html             # Main UI
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
└── PROJECT_DEMO.md            # This file
```

## Future Enhancements

1. Add user authentication and role-based access
2. Implement database for storing prediction history
3. Add data visualization dashboard
4. Support for model retraining with new data
5. Integration with actual loan management systems
6. A/B testing framework for model comparison
7. Advanced ensemble models (XGBoost, Random Forest)

## Contact & Support

For questions or issues, please refer to the application logs at `backend/logs/app.log`.

---

**CreditPathAI** - Intelligent Loan Default Risk Prediction System
