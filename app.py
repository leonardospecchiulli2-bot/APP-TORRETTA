import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Torretta Management Elite", layout="wide", page_icon="🌿")

# --- 2. STILE BEIGE & VERDE (PULITO E LEGGIBILE) ---
st.markdown("""
<style>
    /* Sfondo beige panna */
    .stApp { background-color: #FDFBF0; color: #1B3022; }
    
    /* Sidebar Verde Scuro con testo Beige */
    [data-testid="stSidebar"] { background-color: #1B3022 !important; }
    [data-testid="stSidebar"] * { color: #FDFBF0 !important; }

    /* Card bianche con bordo verde */
    .stat-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #E0E0C0;
        border-top: 6px solid #2E7D32;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .stat-val { font-size: 38px; font-weight: bold; color: #2E7D32; margin: 0; }
    .stat-lab { font-size: 13px; color: #5D6D5F; text-transform: uppercase; letter-spacing: 1px; }

    /* Pulsante Verde Agricolo */
    .stButton>button {
        background-color: #2E7D32;
        color: #FDFBF0;
        border-radius: 8px;
        width: 100%;
        border: none;
        padding: 10px;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #1B3022; color: white; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE INIZIALE ---
if 'stalla_db' not in st.session_state:
    st.session_state.stalla_db = pd.DataFrame([
        {'ID': 'IT001', 'Nome': 'Regina', 'Stato': 'Lattazione', 'Salute': 'Ottima', 'Litri': 35},
        {'ID': 'IT002', 'Nome': 'Mora', 'Stato': 'Asciutta', 'Salute': 'Ottima', 'Litri': 0}
    ])
if 'cassa' not in st.session_state: st.session_state.cassa = 0.0

# --- 4. MENU LATERALE ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; padding-bottom: 20px;'>AZ. AGR.<br>TORRETTA</h2>", unsafe_allow_html=True)
    selected = option_menu(None, ["Dashboard", "Registro Stalla", "Cassa Vendite", "JD-Link"], 
        icons=['grid-1x2
