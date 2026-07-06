from fastapi import APIRouter
from app.predictor import predict_spam
from app.schemas import Prediction, PredictionReq

router = APIRouter(prefix="/api")

@router.post("/predict", response_model=Prediction)
def predict(req: PredictionReq):
    pred, prob = predict_spam(req.email_text)
    return Prediction(
        prediction=pred,
        confidence=prob,
    )
