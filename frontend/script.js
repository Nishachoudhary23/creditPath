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
        loan_amnt: parseFloat(document.getElementById('loan_amnt').value),
        annual_inc: parseFloat(document.getElementById('annual_inc').value),
        dti: parseFloat(document.getElementById('dti').value),
        open_acc: parseInt(document.getElementById('open_acc').value),
        credit_age: parseFloat(document.getElementById('credit_age').value),
        revol_util: parseFloat(document.getElementById('revol_util').value)
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
            throw new Error(errorData.detail || 'Prediction failed');
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
    const probabilityElement = document.getElementById('probability');
    const riskBandElement = document.getElementById('riskBand');
    const actionElement = document.getElementById('action');
    
    const probabilityPercent = (data.probability * 100).toFixed(2);
    probabilityElement.textContent = `${probabilityPercent}%`;
    
    riskBandElement.textContent = data.risk_band;
    riskBandElement.className = 'result-value risk-badge ' + data.risk_band.toLowerCase();
    
    actionElement.textContent = data.action;
    
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

function showError(message) {
    errorSection.textContent = `Error: ${message}`;
    errorSection.style.display = 'block';
    errorSection.scrollIntoView({ behavior: 'smooth' });
}
