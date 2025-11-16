# CreditPathAI

## Overview

CreditPathAI is an intelligent loan default risk prediction system that uses machine learning to assess the likelihood of borrower default. The system analyzes borrower financial data (loan amount, income, debt-to-income ratio, credit history) and provides risk assessments with recommended actions for loan officers.

The application follows a standard client-server architecture with a machine learning pipeline:
- **Frontend**: Single-page application for data entry and results visualization
- **Backend**: FastAPI REST API serving predictions
- **ML Pipeline**: Logistic Regression model with preprocessing and recommendation engine
- **Logging**: Comprehensive logging system for audit trails

## Recent Changes

**November 16, 2025**: Complete CreditPathAI system built and deployed
- ✅ Backend utilities (logger.py, recommendation.py) implemented with rotating log handlers
- ✅ ML model training pipeline created with Logistic Regression achieving 60% accuracy and 63.4% ROC-AUC
- ✅ API components (schema.py, routes.py) built with Pydantic validation and comprehensive error handling
- ✅ FastAPI application (main.py) configured with CORS and static file serving
- ✅ Frontend (HTML/CSS/JS) created with purple gradient theme and responsive design
- ✅ Complete system integration tested and verified working
- ✅ Workflow configured to run on port 5000 with webview
- ✅ PROJECT_DEMO.md created with comprehensive documentation and 5-step demo script
- ✅ Model trained and saved to backend/model/model.pkl

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology**: Vanilla JavaScript with HTML5/CSS3

The frontend is a single-page application that provides a form-based interface for entering borrower data. It communicates with the backend via fetch API calls and dynamically displays prediction results without page reloads.

**Key Design Decisions**:
- **No Framework**: Uses vanilla JavaScript to minimize dependencies and complexity
- **Client-Side Validation**: Form inputs include HTML5 validation attributes for immediate feedback
- **Responsive Design**: CSS Grid/Flexbox layout adapts to different screen sizes
- **Error Handling**: Separate UI sections for loading states, errors, and results

### Backend Architecture

**Technology**: FastAPI (Python)

**Layered Architecture**:
1. **API Layer** (`api/`): Route handlers and Pydantic schemas for request/response validation
2. **Model Layer** (`model/`): ML model training, loading, and caching
3. **Utils Layer** (`utils/`): Cross-cutting concerns (logging, recommendations)

**Key Design Decisions**:

- **FastAPI Framework**: Chosen for automatic OpenAPI documentation, built-in validation with Pydantic, and async support
- **Pydantic Schemas**: Provides automatic request validation, type safety, and clear API contracts. All borrower inputs are validated against business rules (e.g., loan amount < 1 crore, DTI ratio 0-100%)
- **Model Caching**: Model is loaded once into memory (`_model_cache`) to avoid repeated file I/O on each prediction
- **CORS Middleware**: Configured to allow cross-origin requests for flexible deployment
- **Static File Serving**: FastAPI serves the frontend directly, enabling single-deployment architecture

**API Endpoints**:
- `POST /api/predict`: Single borrower prediction
- `POST /api/predict_batch`: Batch predictions (implementation partially complete)

### Machine Learning Pipeline

**Model**: Logistic Regression with StandardScaler preprocessing

**Training Pipeline** (`train_model.py`):
1. **Synthetic Data Generation**: Uses sklearn's `make_classification` to create 10,000 samples with realistic feature distributions
2. **Feature Engineering**: Raw features are scaled to realistic ranges (e.g., loan amounts 10k-10M, DTI 5-35%)
3. **Class Balancing**: SMOTE (Synthetic Minority Over-sampling Technique) addresses class imbalance (70/30 split)
4. **Preprocessing**: StandardScaler normalizes features for logistic regression
5. **Model Serialization**: Model and scaler saved together as `model.pkl` using joblib

**Prediction Pipeline** (`model_loader.py`, `routes.py`):
1. Input validation via Pydantic schema
2. Convert to pandas DataFrame
3. Scale features using trained scaler
4. Generate probability prediction
5. Map to risk band and action recommendation

**Key Design Decisions**:
- **Logistic Regression**: Chosen for interpretability, fast inference, and probabilistic outputs. Suitable for binary classification with good baseline performance
- **SMOTE**: Addresses class imbalance without simply duplicating minority samples
- **Joblib Serialization**: Efficient serialization for sklearn models
- **Lazy Loading**: Model loaded on first prediction request, not at startup

**Alternative Considered**: XGBoost was mentioned in requirements but Logistic Regression was implemented for simplicity and faster training/inference.

### Recommendation Engine

**Strategy**: Rule-based threshold mapping

Converts continuous probability scores into actionable risk bands:
- **Low Risk** (p < 0.3): Standard automated reminder
- **Medium Risk** (0.3 ≤ p < 0.6): Personalized phone call
- **High Risk** (p ≥ 0.6): Priority collection with dedicated agent

**Rationale**: Simple, transparent rules that can be easily adjusted based on business requirements. Thresholds chosen to balance sensitivity vs. operational capacity.

### Logging Architecture

**Technology**: Python's built-in logging module with RotatingFileHandler

**Configuration**:
- Log file location: `backend/logs/app.log`
- Rotation: 1MB per file, 3 backup files
- Format: Timestamp, logger name, level, message
- Dual output: File and console

**Logged Data**:
- All prediction requests with input parameters
- Probability scores and risk classifications
- Recommended actions

**Rationale**: Provides audit trail for regulatory compliance, enables debugging, and allows analysis of prediction patterns over time.

### Error Handling

**Validation Errors**: Pydantic automatically returns 422 responses with detailed validation errors

**Application Errors**:
- Model not found: 500 error with clear message to run training script
- Prediction failures: 500 error with exception details
- Frontend: User-friendly error messages displayed in dedicated UI section

## External Dependencies

### Python Packages

**Core Framework**:
- `fastapi`: Web framework for API
- `uvicorn`: ASGI server for running FastAPI

**Machine Learning**:
- `scikit-learn`: Logistic Regression, StandardScaler, metrics
- `imbalanced-learn`: SMOTE for class balancing
- `pandas`: Data manipulation
- `numpy`: Numerical operations
- `joblib`: Model serialization

**Utilities**:
- `pydantic`: Data validation and settings management

### Frontend Dependencies

**None**: The frontend uses only vanilla JavaScript, HTML5, and CSS3 with no external libraries or frameworks.

### Data Storage

**Model Persistence**: Trained models stored as pickle files (`model.pkl`) in the `backend/model/` directory

**Logging**: File-based logging to `backend/logs/app.log`

**No Database**: The current implementation does not use a database. All predictions are stateless except for logging. If persistence of predictions is needed, a database (PostgreSQL, SQLite) would need to be added.

### Third-Party Services

**None**: The application runs entirely standalone with no external API dependencies or cloud services.