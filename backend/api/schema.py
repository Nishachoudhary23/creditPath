from pydantic import BaseModel, Field, field_validator, EmailStr, ConfigDict
from typing import List, Optional

class BorrowerInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    
    full_name: str = Field(..., description="Full name of borrower")
    email: EmailStr = Field(..., description="Email address")
    phone: str = Field(..., description="Phone number")
    address: Optional[str] = Field(None, description="Residential address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    pincode: Optional[str] = Field(None, description="Pincode")

    employment_status: Optional[str] = Field(None, description="Employment status")
    employer_name: Optional[str] = Field(None, description="Employer/Business name")
    work_experience: Optional[float] = Field(None, description="Years of work experience")
    monthly_income: Optional[float] = Field(None, description="Monthly income")
    
    loan_purpose: str = Field(..., description="Purpose of loan")
    loan_amnt: float = Field(..., description="Loan amount requested")
    loan_term: Optional[int] = Field(None, description="Loan term in months")
    
    annual_inc: float = Field(..., description="Annual income")
    dti: float = Field(..., description="Debt-to-Income ratio (%)")
    open_acc: int = Field(..., description="Number of open credit accounts")
    total_acc: Optional[int] = Field(None, description="Total number of credit accounts")
    credit_age: float = Field(..., description="Age of credit history in years")
    revol_util: float = Field(..., description="Revolving credit utilization (%)")
    existing_loans: Optional[int] = Field(None, description="Number of existing loans")

class PredictionResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    applicant_name: str
    email: str
    phone: str
    probability: float
    risk_band: str
    action: str
    loan_amount: float
    loan_purpose: str
    recommendation_details: str
    financial_data: dict = {}

class BatchPredictionRequest(BaseModel):
    borrowers: List[BorrowerInput]

class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]
