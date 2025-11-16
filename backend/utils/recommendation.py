def get_recommendation(probability: float) -> dict:
    if probability < 0.3:
        risk_band = "Low"
        action = "Standard Reminder"
    elif probability < 0.6:
        risk_band = "Medium"
        action = "Personalized Call"
    else:
        risk_band = "High"
        action = "Priority Collection"
    
    return {
        "risk_band": risk_band,
        "action": action
    }
