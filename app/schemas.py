from pydantic import BaseModel

class Prediction(BaseModel):
    prediction: str
    confidence: float


class PredictionReq(BaseModel):
    email_text: str