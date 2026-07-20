import streamlit as st
import requests
from PIL import Image
import os

# Page config
st.set_page_config(
    page_title="Network Intrusion Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# API URL
API_URL = "https://network-intrusion-detection-zlmu.onrender.com"

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #0f172a; }
    .stApp { background-color: #0f172a; }
    
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 30px;
    }
    .result-box {
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
        text-align: center;
    }
    .normal-box { background: #052e16; border: 2px solid #22c55e; }
    .dos-box { background: #2d0707; border: 2px solid #ef4444; }
    .probe-box { background: #2d1a00; border: 2px solid #f59e0b; }
    .r2l-box { background: #2d0707; border: 2px solid #ef4444; }
    .u2r-box { background: #2d0707; border: 2px solid #dc2626; }
    
    .attack-label {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .confidence-text {
        font-size: 1rem;
        color: #94a3b8;
        margin-bottom: 10px;
    }
    .description-text {
        font-size: 0.95rem;
        color: #e2e8f0;
        line-height: 1.6;
    }
    .section-header {
        color: #38bdf8;
        font-size: 1rem;
        font-weight: 600;
        padding: 8px 0;
        border-bottom: 1px solid #1e3a5f;
        margin-bottom: 15px;
    }
    .metric-card {
        background: #1e293b;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        border: 1px solid #334155;
    }
    .stButton > button {
        background: linear-gradient(135deg, #0284c7, #0369a1);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 30px;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        cursor: pointer;
    }
    .error-box {
        background: #2d0707;
        border: 2px solid #ef4444;
        border-radius: 10px;
        padding: 20px;
        color: #fca5a5;
        text-align: center;
    }
    .warning-box {
        background: #2d1a00;
        border: 2px solid #f59e0b;
        border-radius: 10px;
        padding: 20px;
        color: #fcd34d;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Banner
banner_path = os.path.join(os.path.dirname(__file__), "assets", "banner.png")
if os.path.exists(banner_path):
    banner = Image.open(banner_path)
    st.image(banner, use_column_width=True)

# Title
st.markdown('<div class="main-title">🛡️ Network Intrusion Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered network traffic classifier — XGBoost | NSL-KDD Dataset | CV F1: 0.9990</div>', unsafe_allow_html=True)

# Model info metrics
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown('<div class="metric-card"><div style="color:#38bdf8;font-size:1.3rem;font-weight:700;">XGBoost</div><div style="color:#94a3b8;font-size:0.8rem;">Algorithm</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div style="color:#38bdf8;font-size:1.3rem;font-weight:700;">0.9990</div><div style="color:#94a3b8;font-size:0.8rem;">CV F1 Score</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div style="color:#38bdf8;font-size:1.3rem;font-weight:700;">125,973</div><div style="color:#94a3b8;font-size:0.8rem;">Training Samples</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div style="color:#38bdf8;font-size:1.3rem;font-weight:700;">41</div><div style="color:#94a3b8;font-size:0.8rem;">Features</div></div>', unsafe_allow_html=True)
with col5:
    st.markdown('<div class="metric-card"><div style="color:#38bdf8;font-size:1.3rem;font-weight:700;">5 Classes</div><div style="color:#94a3b8;font-size:0.8rem;">Attack Types</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🛡️ Attack Classes")
    st.success("✅ Normal — Safe traffic")
    st.error("🚨 DoS — Server flooding")
    st.warning("⚠️ Probe — Network scanning")
    st.error("🔴 R2L — Remote access attempt")
    st.error("🔴 U2R — Privilege escalation")

    st.markdown("---")
    st.markdown("### 📡 API Status")
    try:
        health = requests.get(f"{API_URL}/", timeout=5)
        if health.status_code == 200:
            st.success("🟢 Backend Online")
        else:
            st.error("🔴 Backend Error")
    except:
        st.error("🔴 Backend Offline")

    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("**Mushahid Hussain**")
    st.markdown("mushahidh442007@gmail.com")

# Main form
st.markdown('<div class="section-header">🔌 Connection Info</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    duration = st.number_input("Duration (seconds)", min_value=0, value=0)
    src_bytes = st.number_input("Src Bytes", min_value=0, value=0)
    dst_bytes = st.number_input("Dst Bytes", min_value=0, value=0)
with col2:
    protocol_type = st.selectbox("Protocol Type", ["tcp", "udp", "icmp"])
    service = st.selectbox("Service", [
        "http", "ftp", "smtp", "ssh", "telnet", "private",
        "domain_u", "ftp_data", "other", "finger", "pop_3",
        "auth", "eco_i", "urp_i", "domain", "netbios_ssn",
        "imap4", "time", "sun_rpc", "shell", "Z39_50"
    ])
with col3:
    flag = st.selectbox("Flag", ["SF", "S0", "REJ", "RSTR", "RSTO", "S1", "SH", "S2", "S3", "OTH"])
    land = st.selectbox("Land", [0, 1])
    wrong_fragment = st.number_input("Wrong Fragment", min_value=0, value=0)

st.markdown('<div class="section-header">📊 Traffic Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    urgent = st.number_input("Urgent", min_value=0, value=0)
    hot = st.number_input("Hot", min_value=0, value=0)
    num_failed_logins = st.number_input("Num Failed Logins", min_value=0, value=0)
    logged_in = st.selectbox("Logged In", [0, 1])
    num_compromised = st.number_input("Num Compromised", min_value=0, value=0)
    root_shell = st.selectbox("Root Shell", [0, 1])
with col2:
    su_attempted = st.number_input("Su Attempted", min_value=0, value=0)
    num_root = st.number_input("Num Root", min_value=0, value=0)
    num_file_creations = st.number_input("Num File Creations", min_value=0, value=0)
    num_shells = st.number_input("Num Shells", min_value=0, value=0)
    num_access_files = st.number_input("Num Access Files", min_value=0, value=0)
    num_outbound_cmds = st.number_input("Num Outbound Cmds", min_value=0, value=0)
with col3:
    is_host_login = st.selectbox("Is Host Login", [0, 1])
    is_guest_login = st.selectbox("Is Guest Login", [0, 1])
    count = st.number_input("Count", min_value=0, value=1)
    srv_count = st.number_input("Srv Count", min_value=0, value=1)

st.markdown('<div class="section-header">📈 Rate Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    serror_rate = st.slider("Serror Rate", 0.0, 1.0, 0.0, 0.01)
    srv_serror_rate = st.slider("Srv Serror Rate", 0.0, 1.0, 0.0, 0.01)
    rerror_rate = st.slider("Rerror Rate", 0.0, 1.0, 0.0, 0.01)
    srv_rerror_rate = st.slider("Srv Rerror Rate", 0.0, 1.0, 0.0, 0.01)
    same_srv_rate = st.slider("Same Srv Rate", 0.0, 1.0, 1.0, 0.01)
    diff_srv_rate = st.slider("Diff Srv Rate", 0.0, 1.0, 0.0, 0.01)
with col2:
    srv_diff_host_rate = st.slider("Srv Diff Host Rate", 0.0, 1.0, 0.0, 0.01)
    dst_host_count = st.number_input("Dst Host Count", min_value=0, max_value=255, value=1)
    dst_host_srv_count = st.number_input("Dst Host Srv Count", min_value=0, max_value=255, value=1)
    dst_host_same_srv_rate = st.slider("Dst Host Same Srv Rate", 0.0, 1.0, 1.0, 0.01)
    dst_host_diff_srv_rate = st.slider("Dst Host Diff Srv Rate", 0.0, 1.0, 0.0, 0.01)
with col3:
    dst_host_same_src_port_rate = st.slider("Dst Host Same Src Port Rate", 0.0, 1.0, 0.0, 0.01)
    dst_host_srv_diff_host_rate = st.slider("Dst Host Srv Diff Host Rate", 0.0, 1.0, 0.0, 0.01)
    dst_host_serror_rate = st.slider("Dst Host Serror Rate", 0.0, 1.0, 0.0, 0.01)
    dst_host_srv_serror_rate = st.slider("Dst Host Srv Serror Rate", 0.0, 1.0, 0.0, 0.01)
    dst_host_rerror_rate = st.slider("Dst Host Rerror Rate", 0.0, 1.0, 0.0, 0.01)
    dst_host_srv_rerror_rate = st.slider("Dst Host Srv Rerror Rate", 0.0, 1.0, 0.0, 0.01)

st.markdown("<br>", unsafe_allow_html=True)

# Predict button
if st.button("🔍 Analyze Network Traffic"):
    payload = {
        "duration": duration,
        "protocol_type": protocol_type,
        "service": service,
        "flag": flag,
        "src_bytes": src_bytes,
        "dst_bytes": dst_bytes,
        "land": land,
        "wrong_fragment": wrong_fragment,
        "urgent": urgent,
        "hot": hot,
        "num_failed_logins": num_failed_logins,
        "logged_in": logged_in,
        "num_compromised": num_compromised,
        "root_shell": root_shell,
        "su_attempted": su_attempted,
        "num_root": num_root,
        "num_file_creations": num_file_creations,
        "num_shells": num_shells,
        "num_access_files": num_access_files,
        "num_outbound_cmds": num_outbound_cmds,
        "is_host_login": is_host_login,
        "is_guest_login": is_guest_login,
        "count": count,
        "srv_count": srv_count,
        "serror_rate": serror_rate,
        "srv_serror_rate": srv_serror_rate,
        "rerror_rate": rerror_rate,
        "srv_rerror_rate": srv_rerror_rate,
        "same_srv_rate": same_srv_rate,
        "diff_srv_rate": diff_srv_rate,
        "srv_diff_host_rate": srv_diff_host_rate,
        "dst_host_count": dst_host_count,
        "dst_host_srv_count": dst_host_srv_count,
        "dst_host_same_srv_rate": dst_host_same_srv_rate,
        "dst_host_diff_srv_rate": dst_host_diff_srv_rate,
        "dst_host_same_src_port_rate": dst_host_same_src_port_rate,
        "dst_host_srv_diff_host_rate": dst_host_srv_diff_host_rate,
        "dst_host_serror_rate": dst_host_serror_rate,
        "dst_host_srv_serror_rate": dst_host_srv_serror_rate,
        "dst_host_rerror_rate": dst_host_rerror_rate,
        "dst_host_srv_rerror_rate": dst_host_srv_rerror_rate
    }

    with st.spinner("🔄 Analyzing traffic..."):
        try:
            response = requests.post(
                f"{API_URL}/predict",
                json=payload,
                timeout=10
            )

            if response.status_code == 200:
                result = response.json()
                attack_type = result["attack_type"]
                confidence = result["confidence"]
                description = result["description"]

                # CSS class per attack
                box_class = {
                    "Normal": "normal-box",
                    "DoS": "dos-box",
                    "Probe": "probe-box",
                    "R2L": "r2l-box",
                    "U2R": "u2r-box"
                }.get(attack_type, "dos-box")

                color = {
                    "Normal": "#22c55e",
                    "DoS": "#ef4444",
                    "Probe": "#f59e0b",
                    "R2L": "#ef4444",
                    "U2R": "#dc2626"
                }.get(attack_type, "#ef4444")

                st.markdown(f"""
                <div class="result-box {box_class}">
                    <div class="attack-label" style="color:{color};">{attack_type}</div>
                    <div class="confidence-text">Confidence: {confidence*100:.2f}%</div>
                    <div class="description-text">{description}</div>
                </div>
                """, unsafe_allow_html=True)

            elif response.status_code == 422:
                st.markdown("""
                <div class="warning-box">
                    ⚠️ <strong>Invalid Input</strong><br>
                    Please check all input values and try again.
                </div>
                """, unsafe_allow_html=True)

            else:
                st.markdown(f"""
                <div class="error-box">
                    ❌ <strong>Server Error ({response.status_code})</strong><br>
                    Backend returned an unexpected error. Please try again.
                </div>
                """, unsafe_allow_html=True)

        except requests.exceptions.Timeout:
            st.markdown("""
            <div class="error-box">
                ⏱️ <strong>Request Timeout</strong><br>
                Server took more than 10 seconds to respond.<br>
                Render free tier may be waking up — please wait 30 seconds and try again.
            </div>
            """, unsafe_allow_html=True)

        except requests.exceptions.ConnectionError:
            st.markdown("""
            <div class="error-box">
                🔌 <strong>Connection Error</strong><br>
                Could not connect to the backend server.<br>
                Please check your internet connection or try again later.
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.markdown(f"""
            <div class="error-box">
                ❌ <strong>Unexpected Error</strong><br>
                {str(e)}<br>
                Please try again or contact the developer.
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#475569; font-size:0.85rem;">
    Built with ❤️ by <strong style="color:#38bdf8;">Mushahid Hussain</strong> | 
    FastAPI + XGBoost + Streamlit | NSL-KDD Dataset
</div>
""", unsafe_allow_html=True)