import re

def clean_text(text: str) -> str:
    # Convert to lowercase
    text = text.lower()
    # Remove the email subject header
    text = re.sub(r"^subject:\s*", "", text)
    # Replace newlines and tabs with spaces
    text = re.sub(r"[\r\n\t]", " ", text)
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text