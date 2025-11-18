const API_BASE = window.API_BASE || window.location.origin;
const token = localStorage.getItem('token');
const user = JSON.parse(localStorage.getItem('user') || '{}');

if (!token) {
    window.location.href = '/index.html';
}

document.getElementById('userName').textContent = `Welcome, ${user.name || 'User'}`;

const navLinks = document.querySelectorAll('.nav-link:not(.logout)');
const pages = document.querySelectorAll('.page-content');

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const page = link.getAttribute('data-page');
        
        navLinks.forEach(l => l.classList.remove('active'));
        pages.forEach(p => p.style.display = 'none');
        
        link.classList.add('active');
        const pageId = page === 'about' ? 'about' : `${page}Prediction`;
        document.getElementById(pageId).style.display = 'block';
    });
});

document.getElementById('logoutBtn').addEventListener('click', (e) => {
    e.preventDefault();
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    // show loading while redirecting to login
    try { showLoading('Signing out...'); } catch(e){}
    setTimeout(() => window.location.href = '/index.html', 120);
});

document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        full_name: document.getElementById('full_name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        loan_purpose: document.getElementById('loan_purpose').value,
        loan_amnt: parseFloat(document.getElementById('loan_amnt').value),
        annual_inc: parseFloat(document.getElementById('annual_inc').value),
        dti: parseFloat(document.getElementById('dti').value),
        open_acc: parseInt(document.getElementById('open_acc').value),
        credit_age: parseFloat(document.getElementById('credit_age').value),
        revol_util: parseFloat(document.getElementById('revol_util').value)
    };

    showLoading('Analyzing application...');

    try {
        const response = await fetch(`${API_BASE}/api/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Prediction failed');
        }

        const data = await response.json();
        displaySingleResult(data);
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        hideLoading();
    }
});

function displaySingleResult(data) {
    document.getElementById('resultName').textContent = data.applicant_name;
    document.getElementById('resultProb').textContent = (data.probability * 100).toFixed(2) + '%';
    document.getElementById('resultRisk').textContent = data.risk_band;
    document.getElementById('resultRisk').className = 'value risk-badge ' + data.risk_band.toLowerCase();
    document.getElementById('resultAction').textContent = data.action;
    document.getElementById('resultDetails').textContent = data.recommendation_details;
    document.getElementById('resultsSection').style.display = 'block';
    document.getElementById('resultsSection').scrollIntoView({ behavior: 'smooth' });
}

document.getElementById('uploadBtn').addEventListener('click', async () => {
    const fileInput = document.getElementById('excelFile');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select a file');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    showLoading('Processing batch predictions...');

    try {
        const response = await fetch(`${API_BASE}/api/batch/predict_batch_file`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            body: formData
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Batch prediction failed');
        }

        const data = await response.json();
        displayBatchResults(data.predictions);
        window.batchResultsData = data;
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        hideLoading();
    }
});

function displayBatchResults(predictions) {
    const tbody = document.querySelector('#resultsTable tbody');
    tbody.innerHTML = '';
    
    predictions.forEach(pred => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${pred.row_number}</td>
            <td>${(pred.probability * 100).toFixed(2)}%</td>
            <td><span class="risk-badge ${pred.risk_level.toLowerCase()}">${pred.risk_level}</span></td>
            <td>${pred.recommendation}</td>
        `;
        tbody.appendChild(row);
    });
    
    document.getElementById('batchResults').style.display = 'block';
}

document.getElementById('downloadBtn').addEventListener('click', async () => {
    if (!window.batchResultsData) {
        alert('No results to download');
        return;
    }

    showLoading('Preparing download...');
    try {
        const response = await fetch(`${API_BASE}/api/batch/download_batch_results`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(window.batchResultsData)
        });

        if (!response.ok) {
            throw new Error('Download failed');
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'batch_predictions.xlsx';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    } catch (error) {
        alert('Error downloading file: ' + error.message);
    } finally {
        hideLoading();
    }
});

