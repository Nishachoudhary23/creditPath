#!/usr/bin/env python
"""Test script for CreditPathAI API"""
import requests
import json

API_URL = "http://localhost:5000/api/predict"

test_data = {
    "full_name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "address": "123 Main Street",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001",
    "employment_status": "Salaried",
    "employer_name": "TCS",
    "work_experience": 5.0,
    "monthly_income": 150000.0,
    "loan_purpose": "Home Purchase",
    "loan_amnt": 500000.0,
    "loan_term": 60,
    "annual_inc": 1800000.0,
    "dti": 35.5,
    "open_acc": 8,
    "total_acc": 10,
    "credit_age": 5.2,
    "revol_util": 45.3,
    "existing_loans": 1
}

print("Testing CreditPathAI API...")
print(f"Endpoint: {API_URL}")
print(f"Test Data: {json.dumps(test_data, indent=2)}")
print("\n" + "="*60)

try:
    response = requests.post(API_URL, json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 200:
        print("\n✅ API Test PASSED!")
    else:
        print(f"\n❌ API Test FAILED with status {response.status_code}")
        
except requests.exceptions.ConnectionError:
    print("❌ Error: Could not connect to API. Is the server running?")
except Exception as e:
    print(f"❌ Error: {str(e)}")
