# Running CreditPath locally

Quick steps (PowerShell)

1. Open PowerShell in the project root (`C:\Users\hp\Downloads\creditPath`).
2. Run the helper script:

```powershell
.\run_dev.ps1
```

Options:
- `-Reinstall` : re-install dependencies before starting, e.g. `.\run_dev.ps1 -Reinstall`.

What the script does:
- Creates a virtual environment at `./.venv` if missing.
- Installs required Python packages into the venv.
- Starts the FastAPI app on `http://127.0.0.1:5000` using `uvicorn`.

Quick manual commands you can memorize:

```powershell
# create venv (once)
python -m venv .venv
# install deps (once)
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install bcrypt email-validator fastapi imbalanced-learn joblib numpy openpyxl pandas pydantic pyjwt python-multipart scikit-learn uvicorn
# run server
.\.venv\Scripts\python -m uvicorn backend.main:app --host 127.0.0.1 --port 5000
```

Test endpoints:
- Open `http://127.0.0.1:5000/` in your browser to see the login page.
- Use the seeded user in `backend/database/users.json` or sign up via the UI.

Developer test script
- I added a small test helper at `tools/e2e_test.py` you can run with the venv python:

```powershell
.\.venv\Scripts\python tools\e2e_test.py
```

If you want, I can commit these helper files to git and open a PR. Say "commit" and I'll add a clear commit message.