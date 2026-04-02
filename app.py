import streamlit as st
import pandas as pd

# 1. Configurazione base
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS "DASHBOARD PRO"
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* MENU RADIO A BOTTONI */
    div[role="radiogroup"] > label {
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        padding: 12px 20px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: 0.3s ease !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        transform: translateX(10px) !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }

    /* CARD METRICHE ALTE */
    .metric-card {
        background: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    
    /* BOTTONI AZIONI */
    .stButton > button {
        width: 100% !important; height: 50px !important;
        background-color: white !important; color: #1B5E20 !important;
        border: 2px solid #1B5E20 !important; border-radius: 12px !important;
        font-weight: bold !important; margin-bottom: 10px;
    }
    .stButton > button:hover { background-color: #1B5E20 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita"],
