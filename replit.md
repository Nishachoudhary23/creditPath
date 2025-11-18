# CreditPathAI

## Overview
CreditPathAI is an intelligent loan default risk assessment system powered by machine learning. The application provides secure user authentication and allows users to perform single or batch predictions on loan applications to assess default risk.

## Recent Changes (November 18, 2025)
### Complete Feature Enhancement Implementation
- Added JWT-based authentication system with bcrypt password hashing
- Implemented user registration and login functionality with JSON-based user storage
- Created modern dashboard with sidebar navigation
- Migrated single prediction to dashboard layout
- Added batch prediction with Excel file upload/download
- Created About page with model metrics and project information
- Implemented modern responsive UI with blue/green color scheme
- Added route protection and logout functionality

## Project Architecture

### Backend Structure
- `backend/main.py` - FastAPI application with auth, prediction, and batch routes
- `backend/auth/` - Authentication modules (JWT, password hashing, routes)
- `backend/database/` - User database management (JSON-based)
- `backend/api/` - Prediction API routes and batch processing
- `backend/model/` - ML model loading and training
- `backend/utils/` - Utility functions (logging, recommendations)

### Frontend Structure
- `frontend/index.html` - Login/signup page
- `frontend/dashboard.html` - Main dashboard with all features
- `frontend/auth.js` - Authentication handling
- `frontend/dashboard.js` - Dashboard functionality
- `frontend/style.css` - Modern responsive styling

## Technology Stack
- **Backend**: FastAPI, Python 3.11
- **ML**: Scikit-learn, Random Forest, Pandas, NumPy
- **Authentication**: JWT (PyJWT), bcrypt
- **File Processing**: openpyxl (Excel), pandas
- **Frontend**: Vanilla JavaScript, HTML5, CSS3

## Features
1. **Authentication**: Secure signup/login with JWT tokens
2. **Single Prediction**: Individual loan application risk assessment
3. **Batch Prediction**: Excel file upload for multiple predictions
4. **Dashboard**: Clean interface with sidebar navigation
5. **About Page**: Model metrics and project information
6. **Responsive Design**: Works on desktop and mobile devices

## Model Performance
- Accuracy: 92.5%
- F1 Score: 0.89
- ROC-AUC: 0.94
- Precision: 87%

## User Preferences
None documented yet.

## Dependencies
All dependencies managed via `pyproject.toml` using uv package manager:
- fastapi, uvicorn (API framework)
- scikit-learn, pandas, numpy (ML and data processing)
- pyjwt, bcrypt (Authentication)
- openpyxl (Excel file handling)
- imbalanced-learn, joblib (ML utilities)

## Running the Project
The project runs on port 5000 with the workflow:
```
uv run uvicorn backend.main:app --host 0.0.0.0 --port 5000
```

## API Endpoints
- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user
- `POST /api/predict` - Single prediction
- `POST /api/batch/predict_batch_file` - Batch prediction from Excel
- `POST /api/batch/download_batch_results` - Download results as Excel
- `GET /api/health` - Health check
