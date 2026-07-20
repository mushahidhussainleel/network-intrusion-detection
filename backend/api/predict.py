import joblib
import numpy as np
from pathlib import Path
from .schemas import NetworkInput, PredictionResponse
from .utils import preprocess_input

# Model directory
BASE_DIR = Path(__file__).parent.parent
MODEL_DIR = BASE_DIR / "model"

# Load model and label encoder
model = joblib.load(MODEL_DIR / "best_model.pkl")
le_target = joblib.load(MODEL_DIR / "label_encoder.pkl")

# Attack type descriptions — plain English for user
ATTACK_DESCRIPTIONS = {
    "Normal": "✅ Normal traffic — No threat detected. Connection is safe.",
    "DoS": "🚨 DoS Attack — Someone is flooding your server with requests to crash it.",
    "Probe": "⚠️ Probe Attack — Someone is scanning your network to find vulnerabilities.",
    "R2L": "🔴 R2L Attack — Unauthorized remote access attempt detected on your system.",
    "U2R": "🔴 U2R Attack — Someone is trying to gain admin/root privileges on your system."
}


def predict_attack(data: NetworkInput) -> PredictionResponse:
    """
    Main prediction function.
    1. Preprocess user input
    2. Predict attack type
    3. Get confidence score
    4. Return response
    """

    # Step 1: Preprocess input
    input_df = preprocess_input(data)

    # Step 2: Predict class
    prediction_encoded = model.predict(input_df)[0]

    # Step 3: Get confidence score
    probabilities = model.predict_proba(input_df)[0]
    confidence = float(np.max(probabilities))

    # Step 4: Decode label
    attack_type = le_target.inverse_transform([prediction_encoded])[0]

    # Step 5: Get description
    description = ATTACK_DESCRIPTIONS.get(
        attack_type,
        "Unknown attack type detected."
    )

    return PredictionResponse(
        attack_type=attack_type,
        confidence=round(confidence, 4),
        description=description
    )