from .model import predict_log

def process_log(log: str):
    prediction = predict_log(log)
    processed_log = f"Prediction: {prediction}"
    return processed_log
