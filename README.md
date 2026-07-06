# Email Spam Detector

A simple and practical email spam detection web application built with FastAPI, scikit-learn, and a Random Forest classifier. The app predicts whether an incoming email text is spam or not and provides a confidence score.

## Features

- Detects spam vs. ham from email text input
- Uses a Random Forest model for training and prediction
- Provides a web interface for easy testing
- Includes a REST API with interactive documentation
- Implements rate limiting using SlowAPI to protect the API
- Free and open source

## Project Structure

```text
EmailSpamDetector/
├── app/
│   ├── app.py              # FastAPI app entry point
│   ├── model_loader.py     # Loads the trained model and vectorizer
│   ├── predictor.py        # Prediction logic
│   ├── preprocessing.py    # Text cleaning and preprocessing
│   ├── rate_limiting.py    # SlowAPI rate limiting setup
│   ├── routes.py           # API routes
│   └── schemas.py          # Request and response schemas
├── data/
│   └── spam_ham_dataset.csv
├── model/
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│   ├── test_predictor.py
│   ├── test_ratelimit.py
│   ├── test_router.py
│   └── tests.py
├── EmailSpamDetection.ipynb  # Training notebook
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Model and Training

- The machine learning model was trained using a Random Forest classifier.
- The training workflow and experiments are documented in the notebook: [EmailSpamDetection.ipynb](EmailSpamDetection.ipynb).
- The trained model and vectorizer are loaded at runtime from the app model files.

## API Overview

The application exposes a FastAPI-based API for spam detection.

### Main Endpoints

- POST /api/predict: Submit email text and receive a prediction
- GET /health: Check API health status
- GET /: Web UI homepage

### API Documentation

FastAPI provides interactive API documentation:

- Swagger UI: /docs
- ReDoc: /redoc

## Rate Limiting

The API uses SlowAPI to limit requests and reduce abuse.

- Current limits: 10 requests per minute and 200 requests per day per client
- The limiter is configured in the app rate limiting module

## Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

or with Poetry/uv if preferred via the project configuration.

## Run the Application

Start the development server with:

```bash
fastapi dev app/app.py
```

Then open the app in your browser or use the API endpoints.

## License and Open Source

This project is free and open source. You are welcome to use, study, improve, and contribute to it.

## Developer

Developed by: Aditya Shinde
