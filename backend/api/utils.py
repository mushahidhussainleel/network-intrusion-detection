import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from .schemas import NetworkInput

# Model directory
BASE_DIR = Path(__file__).parent.parent
MODEL_DIR = BASE_DIR / "model"

# Load feature encoders
le_protocol = joblib.load(MODEL_DIR / "le_protocol.pkl")
le_service = joblib.load(MODEL_DIR / "le_service.pkl")
le_flag = joblib.load(MODEL_DIR / "le_flag.pkl")


def preprocess_input(data: NetworkInput) -> pd.DataFrame:
    """
    Convert user input to model-ready DataFrame.
    - Encode categorical strings to numbers
    - Maintain exact column order as training data
    """

    # Encode categorical columns
    protocol_encoded = le_protocol.transform([data.protocol_type])[0]
    service_encoded = le_service.transform([data.service])[0]
    flag_encoded = le_flag.transform([data.flag])[0]

    # Build input dict — same column order as training
    input_dict = {
        'duration': data.duration,
        'protocol_type': protocol_encoded,
        'service': service_encoded,
        'flag': flag_encoded,
        'src_bytes': data.src_bytes,
        'dst_bytes': data.dst_bytes,
        'land': data.land,
        'wrong_fragment': data.wrong_fragment,
        'urgent': data.urgent,
        'hot': data.hot,
        'num_failed_logins': data.num_failed_logins,
        'logged_in': data.logged_in,
        'num_compromised': data.num_compromised,
        'root_shell': data.root_shell,
        'su_attempted': data.su_attempted,
        'num_root': data.num_root,
        'num_file_creations': data.num_file_creations,
        'num_shells': data.num_shells,
        'num_access_files': data.num_access_files,
        'num_outbound_cmds': data.num_outbound_cmds,
        'is_host_login': data.is_host_login,
        'is_guest_login': data.is_guest_login,
        'count': data.count,
        'srv_count': data.srv_count,
        'serror_rate': data.serror_rate,
        'srv_serror_rate': data.srv_serror_rate,
        'rerror_rate': data.rerror_rate,
        'srv_rerror_rate': data.srv_rerror_rate,
        'same_srv_rate': data.same_srv_rate,
        'diff_srv_rate': data.diff_srv_rate,
        'srv_diff_host_rate': data.srv_diff_host_rate,
        'dst_host_count': data.dst_host_count,
        'dst_host_srv_count': data.dst_host_srv_count,
        'dst_host_same_srv_rate': data.dst_host_same_srv_rate,
        'dst_host_diff_srv_rate': data.dst_host_diff_srv_rate,
        'dst_host_same_src_port_rate': data.dst_host_same_src_port_rate,
        'dst_host_srv_diff_host_rate': data.dst_host_srv_diff_host_rate,
        'dst_host_serror_rate': data.dst_host_serror_rate,
        'dst_host_srv_serror_rate': data.dst_host_srv_serror_rate,
        'dst_host_rerror_rate': data.dst_host_rerror_rate,
        'dst_host_srv_rerror_rate': data.dst_host_srv_rerror_rate
    }

    return pd.DataFrame([input_dict])