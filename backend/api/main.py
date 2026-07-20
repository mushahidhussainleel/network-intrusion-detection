from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from .schemas import NetworkInput, PredictionResponse
from .predict import predict_attack

# Load HTML file
HOME_HTML = (Path(__file__).parent / "home.html").read_text(encoding="utf-8")

app = FastAPI(
    title="Network Intrusion Detection System",
    description="""
🛡️ AI-powered API to classify network traffic into 5 categories:

| Class | Description |
|---|---|
| ✅ Normal | Safe, legitimate traffic |
| 🚨 DoS | Server flooding attack |
| ⚠️ Probe | Network scanning |
| 🔴 R2L | Unauthorized remote access |
| 🔴 U2R | Privilege escalation attempt |

> **Model:** XGBoost | **Dataset:** NSL-KDD | **CV F1:** 0.9990
    """,
    version="1.0.0",
    contact={
        "name": "Mushahid Hussain",
        "email": "mushahidh442007@gmail.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(content=HOME_HTML, status_code=200)


@app.get("/model-info")
def model_info():
    return {
        "model": "XGBoost Classifier",
        "dataset": "NSL-KDD",
        "classes": ["Normal", "DoS", "Probe", "R2L", "U2R"],
        "cv_f1_score": 0.9990,
        "weighted_f1_score": 0.74,
        "features": 41,
        "training_samples": 125973,
        "class_imbalance_fix": "compute_class_weight balanced"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(data: NetworkInput):
    return predict_attack(data)