from fastapi import APIRouter, HTTPException
from backend.api.schema import BorrowerInput, PredictionResponse, BatchPredictionRequest, BatchPredictionResponse
from backend.model.model_loader import load_model, is_model_loaded
from backend.utils.recommendation import get_recommendation
from backend.utils.logger import log_prediction
import pandas as pd

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(borrower: BorrowerInput):
    try:
        model_data = load_model()
        model = model_data['model']
        scaler = model_data['scaler']
        
        financial_features = {
            'loan_amnt': borrower.loan_amnt,
            'annual_inc': borrower.annual_inc,
            'dti': borrower.dti,
            'open_acc': borrower.open_acc,
            'credit_age': borrower.credit_age,
            'revol_util': borrower.revol_util
        }
        
        df = pd.DataFrame([financial_features])
        df_scaled = scaler.transform(df)
        probability = float(model.predict_proba(df_scaled)[0][1])
        
        recommendation = get_recommendation(probability)
        
        recommendation_details = f"Based on financial analysis, the applicant shows a {recommendation['risk_band'].lower()} probability ({probability*100:.2f}%) of loan default. {recommendation['action']} is recommended."
        
        log_prediction(
            {
                'name': borrower.full_name,
                'email': borrower.email,
                **financial_features
            },
            probability,
            recommendation['risk_band'],
            recommendation['action']
        )
        
        return PredictionResponse(
            applicant_name=borrower.full_name,
            email=borrower.email,
            phone=borrower.phone,
            probability=round(probability, 4),
            risk_band=recommendation['risk_band'],
            action=recommendation['action'],
            loan_amount=borrower.loan_amnt,
            loan_purpose=borrower.loan_purpose,
            recommendation_details=recommendation_details,
            financial_data=financial_features
        )
        
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@router.post("/predict_batch", response_model=BatchPredictionResponse)
async def predict_batch(request: BatchPredictionRequest):
    try:
        model_data = load_model()
        model = model_data['model']
        scaler = model_data['scaler']
        
        predictions = []
        
        for borrower in request.borrowers:
            financial_features = {
                'loan_amnt': borrower.loan_amnt,
                'annual_inc': borrower.annual_inc,
                'dti': borrower.dti,
                'open_acc': borrower.open_acc,
                'credit_age': borrower.credit_age,
                'revol_util': borrower.revol_util
            }
            
            df = pd.DataFrame([financial_features])
            df_scaled = scaler.transform(df)
            probability = float(model.predict_proba(df_scaled)[0][1])
            recommendation = get_recommendation(probability)
            
            recommendation_details = f"Based on financial analysis, the applicant shows a {recommendation['risk_band'].lower()} probability ({probability*100:.2f}%) of loan default. {recommendation['action']} is recommended."
            
            log_prediction(
                {
                    'name': borrower.full_name,
                    'email': borrower.email,
                    **financial_features
                },
                probability,
                recommendation['risk_band'],
                recommendation['action']
            )
            
            predictions.append(PredictionResponse(
                applicant_name=borrower.full_name,
                email=borrower.email,
                phone=borrower.phone,
                probability=round(probability, 4),
                risk_band=recommendation['risk_band'],
                action=recommendation['action'],
                loan_amount=borrower.loan_amnt,
                loan_purpose=borrower.loan_purpose,
                recommendation_details=recommendation_details,
                financial_data=financial_features
            ))
        
        return BatchPredictionResponse(predictions=predictions)
        
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction error: {str(e)}")

@router.get("/health")
async def health():
    return {
        "status": "ok",
        "model_loaded": is_model_loaded()
    }
