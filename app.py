import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Early Auction Fraud Detection System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# LOAD MODEL FILES
# -----------------------------
model = joblib.load("fraud_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #07111f 0%, #08111d 100%);
        color: #f3f4f6;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2.2rem;
        padding-bottom: 2rem;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
    }

    div[data-testid="column"] {
    background: linear-gradient(180deg, #1d2b40 0%, #1a2638 100%);
    padding: 24px;
    border-radius: 20px;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .hero-title {
        text-align: center;
        font-size: 3.25rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 0.6rem;
        letter-spacing: -0.03em;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.15rem;
        color: #94a3b8;
        margin-bottom: 2.25rem;
    }

    .panel-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        gap: 0.55rem;
    }

    div[data-testid="column"] > div {
        height: 100%;
    }

    div[data-testid="stForm"] {
        margin-top: 0.2rem;
    }

    div[data-testid="stForm"] form {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }

    .panel-icon {
        color: #00d26a;
        font-size: 1rem;
    }

    .field-label {
        font-size: 0.98rem;
        font-weight: 600;
        color: #e5e7eb;
        margin-top: 0.6rem;
        margin-bottom: 0.3rem;
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="base-input"] > div {
        background: #08162b !important;
        border: 1px solid #2a3d5f !important;
        border-radius: 10px !important;
        min-height: 46px !important;
    }

    input {
        color: #f8fafc !important;
        font-size: 1rem !important;
    }

    .stNumberInput [data-testid="stWidgetLabel"] {
        display: none;
    }

    .stButton > button {
        width: 100%;
        background: #08b33f;
        color: white;
        border: none;
        border-radius: 10px;
        min-height: 54px;
        font-size: 1rem;
        font-weight: 800;
        margin-top: 1.2rem;
    }

    .stButton > button:hover {
        background: #07a339;
        color: white;
    }

    .risk-pill-high,
    .risk-pill-mid,
    .risk-pill-low {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 999px;
        font-size: 0.88rem;
        font-weight: 800;
        letter-spacing: 0.04em;
        margin-top: 6.5rem;
        margin-bottom: 1rem;
    }

    .risk-pill-high {
        background: rgba(179, 42, 52, 0.28);
        color: #ff6b6b;
    }

    .risk-pill-mid {
        background: rgba(196, 138, 13, 0.22);
        color: #facc15;
    }

    .risk-pill-low {
        background: rgba(10, 140, 84, 0.25);
        color: #00d26a;
    }

    .percent-wrap {
        text-align: center;
        margin-top: 0.3rem;
        margin-bottom: 1.6rem;
    }

    .big-percent {
        font-size: 6rem;
        line-height: 1;
        font-weight: 900;
        color: #f8fafc;
        letter-spacing: -0.06em;
    }

    .percent-symbol {
        font-size: 2.2rem;
        color: #6b7280;
        font-weight: 800;
        margin-left: 0.15rem;
    }

    .risk-scale-labels {
        display: flex;
        justify-content: space-between;
        font-size: 0.92rem;
        font-weight: 800;
        margin-bottom: 0.45rem;
        padding: 0 0.1rem;
    }

    .safe-label { color: #00d26a; }
    .suspicious-label { color: #facc15; }
    .fraud-label { color: #ff2d2d; }

    .risk-bar {
        width: 100%;
        height: 16px;
        background: rgba(19, 34, 55, 0.95);
        border-radius: 999px;
        overflow: hidden;
        margin-bottom: 2rem;
    }

    .risk-fill-low,
    .risk-fill-mid,
    .risk-fill-high {
        height: 100%;
    }

    .risk-fill-low {
        background: linear-gradient(90deg, #22c55e 0%, #34d399 100%);
    }

    .risk-fill-mid {
        background: linear-gradient(90deg, #facc15 0%, #f59e0b 100%);
    }

    .risk-fill-high {
        background: linear-gradient(90deg, #991b1b 0%, #ef4444 100%);
    }

    .insight-box {
        border: 1px solid #314867;
        border-radius: 14px;
        padding: 1.15rem 1.1rem;
        background: rgba(14, 25, 44, 0.35);
        margin-top: 1.4rem;
    }

    .insight-title {
        font-size: 0.95rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 0.65rem;
    }

    .insight-text {
        font-size: 0.98rem;
        line-height: 1.7;
        color: #c7d2fe;
    }

    .insight-text span.green { color: #22c55e; font-weight: 700; }
    .insight-text span.blue { color: #3b82f6; font-weight: 700; }
    .insight-text span.red { color: #ff5a5f; font-weight: 700; }
    .insight-text span.yellow { color: #facc15; font-weight: 700; }

    @media (max-width: 900px) {
        .hero-title {
            font-size: 2.2rem;
        }
        .big-percent {
            font-size: 4.7rem;
        }
        .risk-pill-high,
        .risk-pill-mid,
        .risk-pill-low {
            margin-top: 1rem;
        }
        .panel {
            min-height: auto;
        }
    }

    /* Center the button */
    div[data-testid="stFormSubmitButton"] {
        display: flex;
        justify-content: center;
        margin-top: 18px;
    }

    /* Green button styling */
    div[data-testid="stFormSubmitButton"] button {
        background: linear-gradient(90deg, #00d26a, #00b85c);
        color: white;
        font-weight: 700;
        border-radius: 8px;
        padding: 0.6rem 1.8rem;
        border: none;
    }

    /* Hover effect */
    div[data-testid="stFormSubmitButton"] button:hover {
        background: linear-gradient(90deg, #00e676, #00c864);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HELPERS
# -----------------------------
def normalize_probability(prob):
    return max(0, min(100, round(prob * 100)))

def get_risk_bucket(prob_percent):
    if prob_percent >= 70:
        return "high"
    elif prob_percent >= 35:
        return "mid"
    return "low"

def get_insight_text(prob_percent):
    if prob_percent >= 70:
        return """
        The current bidder profile demonstrates a significant alignment with established shill bidding patterns.
        The high <span class="blue">Successive Outbidding</span> score, combined with an anomalous
        <span class="blue">Bidder Tendency</span>, suggests a non-competitive behavior aimed at price inflation
        rather than item acquisition. We recommend manual audit or account restriction.
        """
    elif prob_percent >= 35:
        return """
        The current bidder profile shows several <span class="yellow">suspicious early-stage indicators</span>.
        While the pattern is not conclusively fraudulent, this behavior departs from typical organic bidding activity.
        Additional monitoring is recommended before allowing unrestricted participation.
        """
    return """
    The current bidder profile demonstrates behavior consistent with organic, competitive auction participation.
    All behavioral indicators fall within normal parameters, suggesting legitimate intent.
    The user is <span class="green">ALLOWED TO BID</span> without further restriction.
    """

def make_risk_html(prob_percent):
    bucket = get_risk_bucket(prob_percent)

    if bucket == "high":
        pill_class = "risk-pill-high"
        pill_text = "HIGH RISK DETECTED"
        fill_class = "risk-fill-high"
    elif bucket == "mid":
        pill_class = "risk-pill-mid"
        pill_text = "SUSPICIOUS ACTIVITY"
        fill_class = "risk-fill-mid"
    else:
        pill_class = "risk-pill-low"
        pill_text = "LOW RISK DETECTED"
        fill_class = "risk-fill-low"

    insight = get_insight_text(prob_percent)

    return f"""
    <div class="{pill_class}">{pill_text}</div>

    <div class="percent-wrap">
        <span class="big-percent">{prob_percent}</span><span class="percent-symbol">%</span>
    </div>

    <div class="risk-scale-labels">
        <span class="safe-label">SAFE</span>
        <span class="suspicious-label">SUSPICIOUS</span>
        <span class="fraud-label">FRAUDULENT</span>
    </div>

    <div class="risk-bar">
        <div class="{fill_class}" style="width: {prob_percent}%;"></div>
    </div>

    <div class="insight-box">
        <div class="insight-title">ℹ️ Model Insight</div>
        <div class="insight-text">{insight}</div>
    </div>
    """

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="hero-title">Early Auction Fraud Detection System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Predicting shill bidding behavior using early-stage auction indicators.</div>',
    unsafe_allow_html=True
)

# -----------------------------
# DEFAULT RESULT STATE
# -----------------------------
if "fraud_percent" not in st.session_state:
    st.session_state.fraud_percent = 12

# -----------------------------
# LAYOUT
# -----------------------------
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown('<div class="panel-title"><span class="panel-icon">▣</span>Early Behavioral Indicators</div>', unsafe_allow_html=True)

    with st.form("fraud_form"):
        st.markdown('<div class="field-label">Bidder Tendency</div>', unsafe_allow_html=True)
        bidder_tendency = st.number_input("Bidder Tendency", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Bidding Ratio</div>', unsafe_allow_html=True)
        bidding_ratio = st.number_input("Bidding Ratio", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Successive Outbidding</div>', unsafe_allow_html=True)
        successive_outbidding = st.number_input("Successive Outbidding", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Last Bidding</div>', unsafe_allow_html=True)
        last_bidding = st.number_input("Last Bidding", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Auction Bids Participation</div>', unsafe_allow_html=True)
        auction_bids = st.number_input("Auction Bids Participation", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Starting Price Influence</div>', unsafe_allow_html=True)
        starting_price_average = st.number_input("Starting Price Influence", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Early Bidding Ratio</div>', unsafe_allow_html=True)
        early_bidding = st.number_input("Early Bidding Ratio", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Winning Ratio</div>', unsafe_allow_html=True)
        winning_ratio = st.number_input("Winning Ratio", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        st.markdown('<div class="field-label">Auction Duration</div>', unsafe_allow_html=True)
        auction_duration = st.number_input("Auction Duration", min_value=0.0, max_value=1.0, value=0.00, step=0.01, format="%.2f", label_visibility="collapsed")

        submitted = st.form_submit_button("◎ Run Fraud Screening")

        if submitted:
            input_data = pd.DataFrame([{
                "Bidder_Tendency": bidder_tendency,
                "Bidding_Ratio": bidding_ratio,
                "Successive_Outbidding": successive_outbidding,
                "Last_Bidding": last_bidding,
                "Auction_Bids": auction_bids,
                "Starting_Price_Average": starting_price_average,
                "Early_Bidding": early_bidding,
                "Winning_Ratio": winning_ratio,
                "Auction_Duration": auction_duration
            }])

            input_data = input_data[feature_names]
            fraud_probability = model.predict_proba(input_data)[0][1]
            st.session_state.fraud_percent = normalize_probability(fraud_probability)

    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="panel-title"><span class="panel-icon">▣</span>Fraud Risk Assessment</div>', unsafe_allow_html=True)
    st.markdown(make_risk_html(st.session_state.fraud_percent), unsafe_allow_html=True)