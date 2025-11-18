from fastapi.testclient import TestClient
from backend.main import app
import json, time

client = TestClient(app)
# Signup
email = f"auto_test_{int(time.time())}@example.com"
resp = client.post('/api/auth/signup', json={'name':'auto_test','email':email,'password':'TestPass123!'})
print('signup status', resp.status_code, resp.text[:400])
if resp.status_code != 200:
    print('Signup failed; if email exists, try logging in or change email')
else:
    token = resp.json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        'full_name':'Auto Test', 'email':email, 'phone':'9999999999',
        'loan_purpose':'Personal','loan_amnt':250000,'annual_inc':1200000,'dti':25.5,'open_acc':4,'credit_age':6.0,'revol_util':20.1
    }
    resp2 = client.post('/api/predict', json=payload, headers={**headers,'Content-Type':'application/json'})
    print('predict status', resp2.status_code)
    print('predict body', resp2.text[:1000])
