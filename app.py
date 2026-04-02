import streamlit as st
# 1. SETTINGS
st.set_page_config(page_title="Torretta Pro", page_icon="🛡️", layout="wide")
# 2. CSS - MENU VERDE E DASHBOARD
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* MENU A BOTTONI */
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: white;
        padding: 15px !important;
        border-radius: 12px !important;
        border: 1px solid #DDD !important;
        margin-bottom: 10px;
        width: 100%;
        transition: 0.3s;
    }
    /* NASCONDI PALLINO */
    div.row-widget.stRadio > div[role="radiogroup"] > label div:first-child { display: none !important; }
    
    /* TESTO MENU */
    div.row-widget.stRadio > div[role="radiogroup"] > label p {
        font-size: 18px !important; font-weight: 600 !important; text-align: center;
    }
    /* COLORE VERDE AL CLICK */
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        border: none !important;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) p {
        color: white !important;
    }
    /* DASHBOARD CARDS */
    .metric-card {
        background-color: white; padding: 25px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    /* BOTTONI AZIONI */
    .stButton>button {
        height: 90px; font-size: 20px !important; border-radius:
