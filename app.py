import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Torretta Management Elite", layout="wide", page_icon="🌿")

# --- STILE BEIGE & VERDE (LOOK MOZZAFIATO) ---
st.markdown("""
<style>
    /* Sfondo beige caldo */
    .stApp {
        background-color: #F5F5DC; 
        color: #1B3022;
    }
    
    /* Sidebar Verde Foresta con scritte chiare */
    [data-testid="stSidebar"] {
        background-color: #1B3022 !important;
    }
    [data-testid="stSidebar"] * {
        color: #F5F5DC !important;
    }

    /* Card eleganti in bianco panna */
    .glass-card {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 25px;
        border: 1px solid #D4D4BA;
        box-shadow: 0 10px 30px rgba(27, 48, 34, 0.05);
        margin-bottom: 20px;
        color: #1B3022;
    }
    
    .stat-value {
        font-size: 45px;
        font-weight: 900;
        color: #2E7D32; /* Verde Agricolo */
    }
    
    .stat-title {
        font-size: 14px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #5D6D5F;
    }

    /* Pulsanti Premium */
    .stButton>button {
        background-color: #2E7D32;
        color: #F5F5DC;
        border-radius: 10px;
        border: none;
        padding: 12px;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1B3022;
        color: #FFFFFF;
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.2);
    }

    /* Header */
    h1, h2, h3 {
        color: #1B3022 !important;
        font-family: 'Georgia', serif;
    }
</style>
""", unsafe_allow_html=True)

# --- DATI ---
if 'db_stalla' not in st.session_state:
    st.session_state.db_stalla = pd.
