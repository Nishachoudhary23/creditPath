import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, 'app.log')

logger = logging.getLogger('CreditPathAI')
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    log_file,
    maxBytes=1024*1024,
    backupCount=3
)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def log_prediction(input_data: dict, probability: float, risk_band: str, action: str):
    log_message = f"Input: {input_data} | Probability: {probability:.4f} | Risk: {risk_band} | Action: {action}"
    logger.info(log_message)
