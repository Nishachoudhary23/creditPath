# CreditPathAI

## Overview
CreditPathAI is an Intelligent Loan Default Risk Assessment System. It's a full-stack application that uses machine learning to predict loan default risk and provide personalized recommendations.

**Current State**: Successfully imported and running on Replit environment as of November 18, 2025.

## Recent Changes
- **November 18, 2025**: Migrated project to Replit environment
  - Synced Python dependencies using uv
  - Configured workflow to run FastAPI backend with uvicorn on port 5000
  - Verified frontend and API are working correctly

## Project Architecture

### Backend (FastAPI)
- **Location**: `backend/`
- **Framework**: FastAPI with uvicorn server
- **Port**: 5000 (bound to 0.0.0.0 for Replit compatibility)
- **Key Components**:
  - `backend/main.py`: Main FastAPI application with CORS middleware
  - `backend/api/routes.py`: API endpoints
  - `backend/api/schema.py`: Pydantic schemas for validation
  - `backend/model/`: Machine learning model (scikit-learn)
  - `backend/utils/`: Utility functions (logging, recommendations)

### Frontend
- **Location**: `frontend/`
- **Technology**: Vanilla HTML, CSS, JavaScript
- **Files**:
  - `index.html`: Loan application form
  - `style.css`: Styling
  - `script.js`: Frontend logic and API integration

### Dependencies
- **Python**: 3.11.13
- **Package Manager**: uv (modern Python package manager)
- **Key Libraries**:
  - FastAPI & Uvicorn (web framework)
  - scikit-learn (machine learning)
  - pandas, numpy (data processing)
  - imbalanced-learn (handling imbalanced datasets)
  - pydantic (data validation)

## Running the Project
The project runs automatically via the configured workflow:
```bash
uv run uvicorn backend.main:app --host 0.0.0.0 --port 5000
```

## Development Environment
- **Platform**: Replit
- **OS**: NixOS (Linux)
- **Virtual Environment**: Managed by uv at `.pythonlibs/`
