from app.preprocessing import clean_text
from app.model_loader import model, vectorizer

def predict_spam(text: str):
    # clean text 
    cleaned_text = clean_text(text)
    # convert to vector
    vector = vectorizer.transform([cleaned_text])
    # make prediction
    prediction = model.predict(vector)
    probs = model.predict_proba(vector)
    label = "spam" if prediction[0] == 1 else "ham"
    confidence = probs[0][prediction[0]]

    return label, confidence


