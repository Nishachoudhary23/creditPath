#!/usr/bin/env python
import subprocess
import sys
import os

# Change to the correct directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Run uvicorn
subprocess.run([
    sys.executable, 
    "-m", 
    "uvicorn", 
    "backend.main:app",
    "--host", "0.0.0.0",
    "--port", "5000",
    "--reload"
], cwd=os.getcwd())
