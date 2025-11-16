import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

_model_cache = None

def load_model():
    global _model_cache
    
    if _model_cache is not None:
        return _model_cache
    
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. "
            "Please run 'python backend/model/train_model.py' first."
        )
    
    try:
        _model_cache = joblib.load(MODEL_PATH)
        return _model_cache
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")

def is_model_loaded():
    return os.path.exists(MODEL_PATH)
