from fastapi import APIRouter, Request
from app.predictor import predict_spam
from app.schemas import Prediction, PredictionReq
from app.rate_limiting import limiter

router = APIRouter(prefix="/api")

@router.post("/predict", response_model=Prediction)
@limiter.limit("10/minute;200/day")
def predict(request: Request,req: PredictionReq):
    pred, prob = predict_spam(req.email_text)
    return Prediction(
        prediction=pred,
        confidence=prob,
    )
