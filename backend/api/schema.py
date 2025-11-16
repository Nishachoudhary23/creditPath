from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import List, Optional

class BorrowerInput(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100, description="Full name of borrower")
    email: EmailStr = Field(..., description="Email address")
    phone: str = Field(..., min_length=10, max_length=15, description="Phone number")
    address: str = Field(..., min_length=10, max_length=200, description="Residential address")
    city: str = Field(..., min_length=2, max_length=50, description="City")
    state: str = Field(..., min_length=2, max_length=50, description="State")
    pincode: str = Field(..., min_length=6, max_length=6, description="Pincode")
    
    employment_status: str = Field(..., description="Employment status (Salaried/Self-Employed/Business)")
    employer_name: str = Field(..., min_length=2, max_length=100, description="Employer/Business name")
    work_experience: float = Field(..., gt=0, description="Years of work experience")
    monthly_income: float = Field(..., gt=0, description="Monthly income")
    
    loan_purpose: str = Field(..., min_length=2, max_length=100, description="Purpose of loan")
    loan_amnt: float = Field(..., gt=0, description="Loan amount requested")
    loan_term: int = Field(..., gt=0, le=360, description="Loan term in months")
    
    annual_inc: float = Field(..., gt=0, description="Annual income")
    dti: float = Field(..., gt=0, le=100, description="Debt-to-Income ratio (%)")
    open_acc: int = Field(..., gt=0, description="Number of open credit accounts")
    total_acc: int = Field(..., gt=0, description="Total number of credit accounts")
    credit_age: float = Field(..., gt=0, description="Age of credit history in years")
    revol_util: float = Field(..., gt=0, le=100, description="Revolving credit utilization (%)")
    existing_loans: int = Field(..., ge=0, description="Number of existing loans")
    
    @field_validator('loan_amnt')
    @classmethod
    def validate_loan_amount(cls, v):
        if v > 10000000:
            raise ValueError('Loan amount must be less than 1 crore (10000000)')
        return v
    
    @field_validator('annual_inc', 'monthly_income')
    @classmethod
    def validate_income(cls, v):
        if v > 10000000:
            raise ValueError('Income must be less than 1 crore (10000000)')
        return v
    
    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v):
        cleaned = ''.join(filter(str.isdigit, v))
        if len(cleaned) < 10:
            raise ValueError('Phone number must have at least 10 digits')
        return v
    
    @field_validator('pincode')
    @classmethod
    def validate_pincode(cls, v):
        if not v.isdigit():
            raise ValueError('Pincode must contain only digits')
        return v

class PredictionResponse(BaseModel):
    applicant_name: str
    email: str
    phone: str
    probability: float
    risk_band: str
    action: str
    loan_amount: float
    loan_purpose: str
    recommendation_details: str
    financial_data: dict

class BatchPredictionRequest(BaseModel):
    borrowers: List[BorrowerInput]

class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
