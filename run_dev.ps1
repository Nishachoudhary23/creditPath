<#
Run Dev helper for CreditPath (PowerShell)

Usage:
  .\run_dev.ps1           # create venv if missing, install deps, run server
  .\run_dev.ps1 -Reinstall  # recreate/install dependencies then run

This script uses the repository's Python (the same `python` on PATH) to create
a local virtual environment at `./.venv`, installs needed packages, then runs
the FastAPI app using the venv python.
#>

param(
    [switch]$Reinstall
)

$venvPath = Join-Path $PSScriptRoot '.venv'
$python = Join-Path $venvPath 'Scripts\python.exe'

if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment at $venvPath..."
    python -m venv $venvPath
}

if ($Reinstall -or -not (Test-Path $python)) {
    Write-Host "Installing/Updating dependencies inside venv..."
    & $venvPath\Scripts\python.exe -m pip install --upgrade pip
    & $venvPath\Scripts\python.exe -m pip install bcrypt email-validator fastapi imbalanced-learn joblib numpy openpyxl pandas pydantic pyjwt python-multipart scikit-learn uvicorn
}

Write-Host "Starting CreditPathAPI at http://127.0.0.1:5000"
& $venvPath\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 5000
