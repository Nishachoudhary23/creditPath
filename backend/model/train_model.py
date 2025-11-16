import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from imblearn.over_sampling import SMOTE
import joblib
import os

def train_and_save_model():
    print("Generating realistic synthetic dataset...")
    np.random.seed(42)
    n_samples = 10000
    
    loan_amnt = np.random.uniform(10000, 1000000, n_samples)
    annual_inc = np.random.uniform(200000, 2000000, n_samples)
    dti = np.random.uniform(5, 80, n_samples)
    open_acc = np.random.randint(1, 20, n_samples)
    credit_age = np.random.uniform(0.5, 20, n_samples)
    revol_util = np.random.uniform(0, 100, n_samples)
    
    risk_score = (
        (dti / 100) * 0.3 +
        (loan_amnt / annual_inc) * 0.25 +
        (revol_util / 100) * 0.2 +
        (1 / (credit_age + 1)) * 0.15 +
        (1 / (open_acc + 1)) * 0.1
    )
    
    noise = np.random.normal(0, 0.15, n_samples)
    risk_score = risk_score + noise
    
    threshold = np.percentile(risk_score, 70)
    y = (risk_score > threshold).astype(int)
    
    df = pd.DataFrame({
        'loan_amnt': loan_amnt,
        'annual_inc': annual_inc,
        'dti': dti,
        'open_acc': open_acc,
        'credit_age': credit_age,
        'revol_util': revol_util
    })
    
    print(f"Default rate: {y.mean():.2%}")
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        df, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print("Applying SMOTE for class balancing...")
    smote = SMOTE(random_state=42)
    X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
    
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_smote)
    X_test_scaled = scaler.transform(X_test)
    
    print("Training Logistic Regression model...")
    model = LogisticRegression(random_state=42, max_iter=1000, C=0.1)
    model.fit(X_train_scaled, y_train_smote)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}")
    
    print("\nFeature coefficients (impact on default risk):")
    feature_names = ['loan_amnt', 'annual_inc', 'dti', 'open_acc', 'credit_age', 'revol_util']
    for name, coef in zip(feature_names, model.coef_[0]):
        print(f"  {name}: {coef:.4f}")
    
    print("Saving model and scaler...")
    model_dir = os.path.dirname(__file__)
    model_path = os.path.join(model_dir, 'model.pkl')
    
    joblib.dump({'model': model, 'scaler': scaler, 'feature_names': feature_names}, model_path)
    
    print(f"Model saved to {model_path}")
    print("Training complete!")
    
    return accuracy, roc_auc

if __name__ == "__main__":
    train_and_save_model()
