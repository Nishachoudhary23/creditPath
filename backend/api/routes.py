from fastapi import APIRouter, HTTPException
from backend.api.schema import BorrowerInput, PredictionResponse, BatchPredictionRequest, BatchPredictionResponse
from backend.model.model_loader import load_model, is_model_loaded
from backend.utils.recommendation import get_recommendation
from backend.utils.logger import log_prediction
import pandas as pd
import numpy as np

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(borrower: BorrowerInput):
    try:
        model_data = load_model()
        model = model_data['model']
        scaler = model_data['scaler']
        
        input_dict = borrower.model_dump()
        
        df = pd.DataFrame([input_dict])
        
        df_scaled = scaler.transform(df)
        
        probability = float(model.predict_proba(df_scaled)[0][1])
        
        recommendation = get_recommendation(probability)
        
        log_prediction(input_dict, probability, recommendation['risk_band'], recommendation['action'])
        
        return PredictionResponse(
            probability=recommendation['probability'],
            risk_band=recommendation['risk_band'],
            action=recommendation['action'],
            input_data=input_dict
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
            input_dict = borrower.model_dump()
            df = pd.DataFrame([input_dict])
            df_scaled = scaler.transform(df)
            probability = float(model.predict_proba(df_scaled)[0][1])
            recommendation = get_recommendation(probability)
            log_prediction(input_dict, probability, recommendation['risk_band'], recommendation['action'])
            
            predictions.append(PredictionResponse(
                probability=recommendation['probability'],
                risk_band=recommendation['risk_band'],
                action=recommendation['action'],
                input_data=input_dict
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
