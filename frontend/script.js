const form = document.getElementById('predictionForm');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');
const loadingSection = document.getElementById('loadingSection');
const submitBtn = document.getElementById('submitBtn');

const API_URL = window.location.origin + '/api/predict';

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    resultsSection.style.display = 'none';
    errorSection.style.display = 'none';
    loadingSection.style.display = 'block';
    submitBtn.disabled = true;
    
    const formData = {
        full_name: document.getElementById('full_name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        address: document.getElementById('address').value,
        city: document.getElementById('city').value,
        state: document.getElementById('state').value,
        pincode: document.getElementById('pincode').value,
        
        employment_status: document.getElementById('employment_status').value,
        employer_name: document.getElementById('employer_name').value,
        work_experience: parseFloat(document.getElementById('work_experience').value),
        monthly_income: parseFloat(document.getElementById('monthly_income').value),
        
        loan_purpose: document.getElementById('loan_purpose').value,
        loan_amnt: parseFloat(document.getElementById('loan_amnt').value),
        loan_term: parseInt(document.getElementById('loan_term').value),
        
        annual_inc: parseFloat(document.getElementById('annual_inc').value),
        dti: parseFloat(document.getElementById('dti').value),
        open_acc: parseInt(document.getElementById('open_acc').value),
        total_acc: parseInt(document.getElementById('total_acc').value),
        credit_age: parseFloat(document.getElementById('credit_age').value),
        revol_util: parseFloat(document.getElementById('revol_util').value),
        existing_loans: parseInt(document.getElementById('existing_loans').value)
    };
    
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Assessment failed');
        }
        
        const data = await response.json();
        
        displayResults(data);
        
    } catch (error) {
        showError(error.message);
    } finally {
        loadingSection.style.display = 'none';
        submitBtn.disabled = false;
    }
});

function displayResults(data) {
    document.getElementById('applicantName').textContent = data.applicant_name;
    document.getElementById('applicantEmail').textContent = data.email;
    document.getElementById('applicantPhone').textContent = data.phone;
    document.getElementById('loanPurpose').textContent = data.loan_purpose;
    document.getElementById('loanAmount').textContent = data.loan_amount.toLocaleString('en-IN');
    
    const probabilityPercent = (data.probability * 100).toFixed(2);
    document.getElementById('probability').textContent = `${probabilityPercent}%`;
    
    const riskBandElement = document.getElementById('riskBand');
    riskBandElement.textContent = data.risk_band;
    riskBandElement.className = 'result-value risk-badge ' + data.risk_band.toLowerCase();
    
    document.getElementById('action').textContent = data.action;
    
    document.getElementById('recommendationDetails').textContent = data.recommendation_details;
    
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

function showError(message) {
    errorSection.textContent = `Error: ${message}`;
    errorSection.style.display = 'block';
    errorSection.scrollIntoView({ behavior: 'smooth' });
}
