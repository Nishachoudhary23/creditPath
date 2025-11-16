## CreditPathAI - Quick Start

This single README replaces earlier dispersed MD files. It contains the essential information to set up, run, and debug the project locally.

**Prerequisites:**
- Python 3.11+ installed
- (Optional) VS Code and Live Server extension for frontend rapid edits

**Project layout (important files):**
- `backend/main.py` — FastAPI app (serves API and can mount frontend static files)
- `backend/api/routes.py` — prediction endpoints (`/api/predict`, `/api/predict_batch`, `/api/health`)
- `backend/model/train_model.py` — script to train and save the model (`backend/model/model.pkl`)
- `backend/model/model_loader.py` — model loader used by the routes
- `frontend/index.html`, `frontend/script.js`, `frontend/style.css` — frontend UI and client logic
- `backend/logs/app.log` — rotating log file for server predictions

## Setup (recommended)
1. Open a terminal in the project root (this repository root):

```powershell
cd 'C:\Users\hp\Downloads\CreditPathAI\CreditPathAI'
```

2. Create and activate a Python virtual environment (if you haven't already):

```powershell
python -m venv .venv
& '.venv\Scripts\Activate.ps1'
```

3. Install dependencies (from `pyproject.toml` or pip):

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not present, install these main packages:

```powershell
pip install fastapi uvicorn scikit-learn pandas numpy joblib pydantic email-validator python-multipart imbalanced-learn requests
```

4. Train the model (creates `backend/model/model.pkl`):

```powershell
python backend/model/train_model.py
```

## Run the backend (serves API and optionally the frontend)
Start the FastAPI server. This command mounts the `frontend` folder and serves both the API and static site at port 5000:

```powershell
& '.venv\Scripts\python.exe' -m uvicorn backend.main:app --host 0.0.0.0 --port 5000 --workers 1
```

Open the app at:
- Backend-served frontend: http://localhost:5000
- API base: http://localhost:5000/api

## Run the frontend with Live Server (optional)
If you prefer editing the frontend in VS Code with Live Server (which serves on port 5500), start the backend first (port 5000), then Open `frontend/index.html` with Live Server. The client is preconfigured to call the backend at `http://localhost:5000/api/predict` when served from Live Server.

## API Usage
- POST `/api/predict` — accepts JSON payload from the form and returns prediction JSON including `probability`, `risk_band`, `recommendation_details`, etc.

Example curl (replace fields as needed):

```bash
curl -X POST 'http://localhost:5000/api/predict' \
  -H 'Content-Type: application/json' \
  -d '{"full_name":"Test User","email":"a@b.com","phone":"9999999999","loan_amount":500000,"loan_term":60,"annual_inc":600000,"dti":30,"open_acc":2,"total_acc":5,"credit_age":3.5,"revol_util":30,"existing_loans":0,"employment_status":"Salaried","employer_name":"ACME","monthly_income":50000}'
```

## Troubleshooting
- ModuleNotFoundError when starting uvicorn: ensure you run the command from the project root where `backend` is a package (the command above expects `backend.main:app`).
- CORS: `backend/main.py` enables CORS for `allow_origins=["*"]` to allow Live Server (port 5500) to call the API at port 5000.
- 422 errors: occur when request JSON does not match the Pydantic schema. Use the browser DevTools Network tab to inspect the request payload and the response body for detailed validation errors. The frontend (`frontend/script.js`) logs the payload and response to the browser console.
- Frontend not responding: open browser DevTools Console. The client prints `script.js loaded`, `Form submit event fired`, and `Prepared formData` when you submit.

## Logs
- Server prediction logs are written to `backend/logs/app.log`. Check this file for recorded prediction lines and errors.

## Next improvements (optional)
- Add `requirements.txt` for easier installs.
- Add a single environment config to toggle API base URL instead of relying on port detection.
- Restore stricter server-side validation after adding corresponding client-side checks.

If you want, I can also commit these changes and run a quick end-to-end test from this environment.
