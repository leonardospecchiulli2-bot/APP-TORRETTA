import streamlit as st
import pandas as pd

# 1. Configurazione Iniziale
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. Pulizia e Inizializzazione Memoria (Evita gli errori delle foto)
if 'prodotti_v2' not in st.session_state:
    st.session_state.prodotti_v2 = {"Latte": 0, "Caciocavallo": 0, "Ricotta": 0}
if 'latte_oggi' not in st.session_state:
    st.session_state.latte_oggi = 1240
if 'vendite_registro' not in st.session_state:
    st.session_state.vendite_registro = []
if 'n_m' not in st.session_state: st.session_state.n_m = 1
if 'n_v' not in st.session_state: st.session_state.n_v = 1
if 'n_t' not in st.session_state: st.session_state.n_t = 1

# 3. CSS - Design Elegante (Niente pallini, box verdi)
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background-color: white !important; border: 1px solid #e0e0e0 !important;
        padding: 12px 20px !important; border-radius: 12px !important;
        margin-bottom: 8px !important; display: flex !important; cursor: pointer !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important; color: white !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }
    .metric-box {
        background: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B
