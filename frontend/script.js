const form = document.getElementById('predictionForm');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');
const loadingSection = document.getElementById('loadingSection');
const submitBtn = document.getElementById('submitBtn');

// Backend API URL - choose dynamically so frontend works both when served by Live Server (5500)
// and when served from the backend (same origin, port 5000).
const API_URL = (function() {
    try {
        const port = window.location.port;
        // If the page is served by Live Server on 5500, target backend at 5000
        if (port === '5500') return 'http://127.0.0.1:5000/api/predict';
        // Otherwise assume backend is mounted at same origin (e.g. http://localhost:5000/)
        return `${window.location.origin}/api/predict`;
    } catch (e) {
        // fallback to localhost:5000
        console.warn('Failed to compute API_URL dynamically, falling back to localhost:5000', e);
        return 'http://localhost:5000/api/predict';
    }
})();

// Basic debug boot log so we can confirm the script is loading in the browser
console.log('script.js loaded');
if (!form) {
    console.error('predictionForm not found in DOM');
    // showError is hoisted below; safe to call
    showError('Internal error: form not found on page.');
}

// Global error handlers to surface uncaught runtime errors to the page
window.addEventListener('error', (ev) => {
    console.error('Global error captured:', ev.error || ev.message);
    showError('An unexpected error occurred: ' + (ev.error?.message || ev.message));
});
window.addEventListener('unhandledrejection', (ev) => {
    console.error('Unhandled rejection:', ev.reason);
    showError('An unexpected error occurred: ' + (ev.reason?.message || JSON.stringify(ev.reason)));
});

function sanitizeNumber(val) {
    const n = Number(val);
    return Number.isFinite(n) ? n : null;
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    console.log('Form submit event fired');
    
    resultsSection.style.display = 'none';
    errorSection.style.display = 'none';
    loadingSection.style.display = 'block';
    submitBtn.disabled = true;

    const loanAmntRaw = document.getElementById('loan_amnt').value;
    const loanAmnt = sanitizeNumber(loanAmntRaw);

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
        work_experience: sanitizeNumber(document.getElementById('work_experience').value),
        monthly_income: sanitizeNumber(document.getElementById('monthly_income').value),

        loan_purpose: document.getElementById('loan_purpose').value,
        loan_amnt: loanAmnt,
        // include a second key name the backend may expect
        loan_amount: loanAmnt,
        loan_term: sanitizeNumber(document.getElementById('loan_term').value),

        annual_inc: sanitizeNumber(document.getElementById('annual_inc').value),
        dti: sanitizeNumber(document.getElementById('dti').value),
        open_acc: sanitizeNumber(document.getElementById('open_acc').value),
        total_acc: sanitizeNumber(document.getElementById('total_acc').value),
        credit_age: sanitizeNumber(document.getElementById('credit_age').value),
        revol_util: sanitizeNumber(document.getElementById('revol_util').value),
        existing_loans: sanitizeNumber(document.getElementById('existing_loans').value)
    };

    console.log('Prepared formData:', formData);

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            try {
                const errorData = await response.json();
                const errorMessage = errorData.detail || JSON.stringify(errorData);
                throw new Error(errorMessage);
            } catch (parseError) {
                throw new Error(`Assessment failed with status ${response.status}`);
            }
        }

        const data = await response.json();
        console.log('Response data:', data);

        displayResults(data);

    } catch (error) {
        console.error('Error during submit flow:', error);
        showError(error.message || String(error));
    } finally {
        loadingSection.style.display = 'none';
        submitBtn.disabled = false;
    }
});

function displayResults(data) {
    try {
        document.getElementById('applicantName').textContent = data.applicant_name || 'N/A';
        document.getElementById('applicantEmail').textContent = data.email || 'N/A';
        document.getElementById('applicantPhone').textContent = data.phone || 'N/A';
        document.getElementById('loanPurpose').textContent = data.loan_purpose || 'N/A';
        
        const loanAmount = typeof data.loan_amount === 'number' ? data.loan_amount : parseFloat(data.loan_amount);
        document.getElementById('loanAmount').textContent = isNaN(loanAmount) ? 'N/A' : loanAmount.toLocaleString('en-IN');
        
        const probability = typeof data.probability === 'number' ? data.probability : parseFloat(data.probability);
        const probabilityPercent = isNaN(probability) ? 'N/A' : (probability * 100).toFixed(2);
        document.getElementById('probability').textContent = `${probabilityPercent}%`;
        
        const riskBandElement = document.getElementById('riskBand');
        riskBandElement.textContent = data.risk_band || 'N/A';
        riskBandElement.className = 'result-value risk-badge ' + (data.risk_band ? data.risk_band.toLowerCase() : '');
        
        document.getElementById('action').textContent = data.action || 'N/A';
        document.getElementById('recommendationDetails').textContent = data.recommendation_details || 'N/A';
        
        resultsSection.style.display = 'block';
        resultsSection.scrollIntoView({ behavior: 'smooth' });
        // Show raw JSON in debug box for easier troubleshooting
        try {
            const rawEl = document.getElementById('rawResponse');
            const debugSection = document.getElementById('debugSection');
            if (rawEl) {
                rawEl.textContent = JSON.stringify(data, null, 2);
            }
            if (debugSection) debugSection.style.display = 'block';
        } catch (err) {
            console.warn('Could not render raw debug response', err);
        }
    } catch (error) {
        console.error('Error displaying results:', error);
        showError('Failed to display results: ' + error.message);
    }
}

function showError(message) {
    errorSection.textContent = `Error: ${message}`;
    errorSection.style.display = 'block';
    errorSection.scrollIntoView({ behavior: 'smooth' });

    // also display the error in the debug box
    try {
        const rawEl = document.getElementById('rawResponse');
        const debugSection = document.getElementById('debugSection');
        if (rawEl) rawEl.textContent = message;
        if (debugSection) debugSection.style.display = 'block';
    } catch (err) {
        // ignore
    }
}
