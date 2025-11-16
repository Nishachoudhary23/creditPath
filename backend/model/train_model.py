import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from imblearn.over_sampling import SMOTE
import joblib
import os

def train_and_save_model():
    print("Generating synthetic dataset...")
    X, y = make_classification(
        n_samples=10000,
        n_features=6,
        n_informative=5,
        n_redundant=1,
        n_classes=2,
        weights=[0.7, 0.3],
        random_state=42
    )
    
    feature_names = ['loan_amnt', 'annual_inc', 'dti', 'open_acc', 'credit_age', 'revol_util']
    df = pd.DataFrame(X, columns=feature_names)
    
    df['loan_amnt'] = np.abs(df['loan_amnt']) * 50000 + 10000
    df['annual_inc'] = np.abs(df['annual_inc']) * 100000 + 20000
    df['dti'] = np.abs(df['dti']) * 30 + 5
    df['open_acc'] = (np.abs(df['open_acc']) * 10 + 1).astype(int)
    df['credit_age'] = np.abs(df['credit_age']) * 15 + 1
    df['revol_util'] = np.abs(df['revol_util']) * 80 + 10
    
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
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train_smote)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}")
    
    print("Saving model and scaler...")
    model_dir = os.path.dirname(__file__)
    model_path = os.path.join(model_dir, 'model.pkl')
    scaler_path = os.path.join(model_dir, 'scaler.pkl')
    
    joblib.dump({'model': model, 'scaler': scaler}, model_path)
    
    print(f"Model saved to {model_path}")
    print("Training complete!")
    
    return accuracy, roc_auc

if __name__ == "__main__":
    train_and_save_model()
