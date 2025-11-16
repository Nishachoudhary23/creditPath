from pydantic import BaseModel, Field, field_validator
from typing import List

class BorrowerInput(BaseModel):
    loan_amnt: float = Field(..., gt=0, description="Loan amount must be positive")
    annual_inc: float = Field(..., gt=0, description="Annual income must be positive")
    dti: float = Field(..., gt=0, le=100, description="DTI must be between 0 and 100")
    open_acc: int = Field(..., gt=0, description="Open accounts must be positive")
    credit_age: float = Field(..., gt=0, description="Credit age must be positive")
    revol_util: float = Field(..., gt=0, description="Revolving utilization must be positive")
    
    @field_validator('loan_amnt')
    @classmethod
    def validate_loan_amount(cls, v):
        if v > 10000000:
            raise ValueError('Loan amount must be less than 1 crore (10000000)')
        return v
    
    @field_validator('annual_inc')
    @classmethod
    def validate_annual_income(cls, v):
        if v > 10000000:
            raise ValueError('Annual income must be less than 1 crore (10000000)')
        return v

class PredictionResponse(BaseModel):
    probability: float
    risk_band: str
    action: str
    input_data: dict

class BatchPredictionRequest(BaseModel):
    borrowers: List[BorrowerInput]

class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
