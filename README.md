<div align="center">

<img src="backend/images/banner.png" alt="Network Intrusion Detection System Banner" width="100%"/>

# 🛡️ Network Intrusion Detection System

### AI-Powered Network Traffic Classifier | XGBoost | NSL-KDD Dataset

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-3.2-orange?style=for-the-badge&logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

**[🌐 Live Demo](https://network-intrusion-detection-8wqjguchviqbu6p8iiwwfv.streamlit.app/) · [⚡ API Docs](https://network-intrusion-detection-zlmu.onrender.com/docs) · [📊 Backend](https://network-intrusion-detection-zlmu.onrender.com) · [👨‍💻 GitHub](https://github.com/mushahidhussainleel) · [💼 LinkedIn](https://linkedin.com/in/mushahid-hussain-dev)**

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Attack Classes](#-attack-classes)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [ML Pipeline](#-ml-pipeline)
- [Model Performance](#-model-performance)
- [API Endpoints](#-api-endpoints)
- [Local Setup](#-local-setup)
- [Deployment](#-deployment)
- [Screenshots](#-screenshots)
- [Developer](#-developer)

---

## 🔍 Overview

The **Network Intrusion Detection System (NIDS)** is an end-to-end Machine Learning solution that classifies network traffic into **5 categories** — distinguishing normal activity from four types of cyber attacks in real time.

Built on the industry-standard **NSL-KDD dataset**, this system demonstrates a complete ML pipeline from raw data exploration to production deployment — covering EDA, preprocessing, model training with class imbalance handling, FastAPI backend, and Streamlit frontend.

> **Note:** This project is built for educational and portfolio purposes. It demonstrates real-world ML engineering practices including class imbalance handling, model evaluation, and API deployment.

---

## 🎯 Attack Classes

| Class | Icon | Description | Real-World Example |
|---|---|---|---|
| **Normal** | ✅ | Legitimate network traffic | Regular web browsing, file transfer |
| **DoS** | 🚨 | Denial of Service — server flooding | SYN flood, Smurf, Neptune attack |
| **Probe** | ⚠️ | Network scanning and reconnaissance | Port scanning, Nmap, IPSweep |
| **R2L** | 🔴 | Remote to Local — unauthorized access | Password guessing, FTP exploit |
| **U2R** | 🔴 | User to Root — privilege escalation | Buffer overflow, Rootkit installation |

---

## 📁 Project Structure

```
network-intrusion-detection/
│
├── backend/
│   ├── data/
│   │   ├── raw/
│   │   │   ├── KDDTrain+.txt          # Raw training data (125,973 samples)
│   │   │   └── KDDTest+.txt           # Raw test data (22,544 samples)
│   │   └── processed/
│   │       ├── train_processed.csv    # Preprocessed training data
│   │       └── test_processed.csv     # Preprocessed test data
│   │
│   ├── notebooks/
│   │   ├── 01_EDA.ipynb               # Exploratory Data Analysis
│   │   └── 02_Model_Training.ipynb    # Model Training & Evaluation
│   │
│   ├── model/
│   │   ├── best_model.pkl             # XGBoost trained pipeline
│   │   ├── label_encoder.pkl          # Target label encoder
│   │   ├── le_protocol.pkl            # Protocol type encoder
│   │   ├── le_service.pkl             # Service encoder
│   │   └── le_flag.pkl                # Flag encoder
│   │
│   ├── api/
│   │   ├── main.py                    # FastAPI app + endpoints
│   │   ├── schemas.py                 # Pydantic input/output models
│   │   ├── utils.py                   # Preprocessing helpers
│   │   ├── predict.py                 # Model load + prediction logic
│   │   └── home.html                  # Landing page HTML
│   │
│   ├── images/                        # EDA visualizations
│   │   ├── outliers_boxplot.png
│   │   ├── feature_distributions.png
│   │   ├── categorical_distribution.png
│   │   ├── class_distribution.png
│   │   └── correlation_heatmap_key.png
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── app.py                         # Streamlit frontend
│   ├── requirements.txt
│   └── assets/
│       └── banner.png                 # Project banner
│
└── README.md
```

---

## 🛠️ Tech Stack

### Machine Learning
| Library | Version | Purpose |
|---|---|---|
| Scikit-learn | 1.9.0 | Pipeline, LabelEncoder, metrics |
| XGBoost | 3.2.0 | Best performing classifier |
| Pandas | 2.2.2 | Data manipulation |
| NumPy | 2.4.4 | Numerical operations |
| Joblib | 1.5.3 | Model serialization |
| Matplotlib / Seaborn | Latest | EDA visualizations |

### Backend
| Library | Version | Purpose |
|---|---|---|
| FastAPI | 0.139.0 | REST API framework |
| Uvicorn | 0.49.0 | ASGI server |
| Pydantic | 2.13.4 | Data validation |

### Frontend & Deployment
| Tool | Purpose |
|---|---|
| Streamlit | Interactive frontend UI |
| Render | Backend cloud deployment |
| Streamlit Cloud | Frontend deployment |
| GitHub | Version control |

---

## 🔬 ML Pipeline

```
Raw Data (NSL-KDD)
        ↓
01_EDA.ipynb
  ├── Data Loading & Column Assignment (43 columns)
  ├── Missing Values Check → 0 missing
  ├── Duplicate Check → 0 duplicates
  ├── Outlier Analysis (Box plots + Log scale)
  │   └── Decision: Retain outliers (real attack signatures)
  ├── Feature Distribution (Right-skewed confirmed)
  ├── Categorical Analysis (protocol, service, flag)
  ├── Correlation Heatmap (multicollinearity noted)
  ├── Label Mapping (23 attack types → 5 classes)
  ├── Class Distribution Analysis
  ├── Preprocessing (Label Encoding + Drop columns)
  └── Save → train_processed.csv, test_processed.csv
        ↓
02_Model_Training.ipynb
  ├── Feature/Target Split (X: 41 features, y: attack_type)
  ├── Target Label Encoding (XGBoost compatibility)
  ├── Baseline Comparison (5 models via Pipeline + StratifiedKFold CV)
  ├── Best Model Selection → XGBoost (CV F1: 0.9990)
  ├── Class Imbalance Fix → compute_class_weight balanced
  ├── Final Model Training with sample_weight
  ├── Evaluation (Classification Report + Confusion Matrix)
  └── Save → best_model.pkl + label_encoder.pkl
        ↓
FastAPI Backend
  ├── schemas.py → Input validation (41 features)
  ├── utils.py → Categorical encoding (LabelEncoder)
  ├── predict.py → Model load + predict + confidence
  └── main.py → Endpoints (/, /model-info, /predict)
        ↓
Streamlit Frontend
  └── app.py → UI + API calls + error handling
```

---

## 📊 Model Performance

### Baseline Comparison (CV F1 Weighted — StratifiedKFold 5-Fold)

| Model | CV F1 Score | Accuracy |
|---|---|---|
| Decision Tree | 0.9975 | 0.7615 |
| Random Forest | 0.9988 | 0.7500 |
| Gradient Boosting | 0.9972 | 0.7611 |
| **XGBoost** ⭐ | **0.9990** | **0.7574** |
| SVM | 0.9921 | 0.7531 |

### Final Model — XGBoost with Class Weight

```
              precision    recall  f1-score   support

         DoS       0.96      0.77      0.85      7458
      Normal       0.67      0.97      0.79      9711
       Probe       0.87      0.75      0.81      2421
         R2L       0.99      0.12      0.21      2889
         U2R       0.62      0.20      0.30        65

    accuracy                           0.77     22544
   macro avg       0.82      0.56      0.59     22544
weighted avg       0.83      0.77      0.74     22544
```

### Before vs After Class Weight Fix

| Class | F1 Before | F1 After | Improvement |
|---|---|---|---|
| DoS | 0.87 | 0.85 | — |
| Normal | 0.79 | 0.79 | = |
| Probe | 0.74 | 0.81 | ↑ +0.07 |
| R2L | 0.02 | 0.21 | ↑ **10x** |
| U2R | 0.25 | 0.30 | ↑ +0.05 |
| **Weighted F1** | **0.71** | **0.74** | ↑ **+0.03** |

> **Why F1 Weighted?** Class imbalance is severe — U2R is only 0.04% of training data. Accuracy alone is misleading; F1 Weighted accounts for class distribution.

> **Why retain outliers?** Extreme values in `src_bytes` (1.3B) and `duration` (42,908s) are real DoS and U2R attack signatures — removing them would eliminate critical attack patterns.

---

## 📡 API Endpoints

Base URL: `https://network-intrusion-detection-zlmu.onrender.com`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Landing page (HTML) |
| `GET` | `/model-info` | Model details & performance metrics |
| `POST` | `/predict` | Classify network traffic (41 features) |
| `GET` | `/docs` | Interactive Swagger UI |
| `GET` | `/redoc` | ReDoc documentation |

### Sample Prediction Request

```json
POST /predict
{
  "duration": 0,
  "protocol_type": "tcp",
  "service": "http",
  "flag": "SF",
  "src_bytes": 232,
  "dst_bytes": 8153,
  "land": 0,
  "logged_in": 1,
  "count": 5,
  "srv_count": 5,
  "serror_rate": 0.0,
  "same_srv_rate": 1.0,
  ...
}
```

### Sample Response

```json
{
  "attack_type": "Normal",
  "confidence": 0.9987,
  "description": "✅ Normal traffic — No threat detected. Connection is safe."
}
```

---

## 🚀 Local Setup

### Prerequisites
- Python 3.11+
- Conda or venv
- Git

### 1. Clone Repository

```bash
git clone https://github.com/mushahidhussainleel/network-intrusion-detection.git
cd network-intrusion-detection
```

### 2. Create Virtual Environment

```bash
conda create -n nids_env python=3.11
conda activate nids_env
```

### 3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Backend runs at: `http://127.0.0.1:8000`

### 5. Install Frontend Dependencies

```bash
cd ../frontend
pip install -r requirements.txt
```

### 6. Run Streamlit Frontend

```bash
streamlit run app.py
```

Frontend runs at: `http://localhost:8501`

> **Note:** Update `API_URL` in `frontend/app.py` to `http://127.0.0.1:8000` for local testing.

---

## ☁️ Deployment

### Backend — Render

| Setting | Value |
|---|---|
| Runtime | Python 3 |
| Root Directory | `backend` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn api.main:app --host 0.0.0.0 --port $PORT` |

### Frontend — Streamlit Cloud

| Setting | Value |
|---|---|
| Repository | `mushahidhussainleel/network-intrusion-detection` |
| Branch | `main` |
| Main file path | `frontend/app.py` |

---

## 📸 Screenshots

### Streamlit Frontend
> Interactive UI with 41 input features, real-time prediction, and color-coded threat results

### FastAPI Swagger UI
> Full API documentation with try-it-out functionality at `/docs`

### EDA Visualizations
> Class distribution, outlier analysis, feature distributions, and correlation heatmap

---

## 👨‍💻 Developer

<div align="center">

**Mushahid Hussain**

Python Backend Developer | ML Practitioner

[![LinkedIn](https://img.shields.io/badge/LinkedIn-mushahid--hussain--dev-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/mushahid-hussain-dev)
[![GitHub](https://img.shields.io/badge/GitHub-mushahidhussainleel-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mushahidhussainleel)
[![Email](https://img.shields.io/badge/Email-mushahidh442007@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mushahidh442007@gmail.com)

</div>

---

## 🙏 Acknowledgements

- **Dataset:** [NSL-KDD](https://www.kaggle.com/datasets/hassan06/nslkdd) — Canadian Institute for Cybersecurity
- **Mentors:** Sir Zafar Iqbal
- **Landing Page UI:** Architecture and design decisions by Mushahid Hussain. 
  HTML/CSS coding assisted by **Claude AI** (Anthropic).
---

<div align="center">

⭐ **If this project helped you, please give it a star!** ⭐

Made with ❤️ by **Mushahid Hussain**

</div>