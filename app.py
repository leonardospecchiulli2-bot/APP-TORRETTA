import streamlit as st
import pandas as pd
import numpy as np

# 1. Configurazione base
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS "EVOLUZIONE DASHBOARD PRO"
st.markdown("""
<style>
    /* Sfondo e Sidebar */
    .stApp { background-color: #FDFCF5 !important; }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 1px solid #eee !important; }

    /* MENU SENZA PALLINI + ANIMAZIONI */
    [data-testid="stWidgetLabel"] { display: none !important; }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        padding: 14px 20px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
        display: flex !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    div[role="radiogroup"] > label:hover {
        background-color: #f0f4f0 !important;
        transform: scale(1.02) !important;
    }
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        transform: translateX(12px) !important;
        box-shadow: 0 5px 15px rgba(27, 94, 32, 0.3) !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: #ffffff !important; }

    /* CARD METRICHE ALTE */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 5px solid #1B5E20;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* CARD BIANCHE PER GRAFICI E TABELLE */
    .content-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
        border: 1px solid #f0f0f0;
        height: 100%;
    }

    /* BOTTONI AZIONI (SOTTILI) */
    .stButton > button {
        width: 100% !important;
        height: 55px !important;
        background-color: #ffffff !important;
        color: #1B5E20 !important;
        border: 2px solid #1B5E20 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        transition: 0.3s !important;
        margin-bottom: 10px;
    }
    .stButton > button:hover {
        background-color: #1B5E20 !important;
        color: white !important;
        box-shadow: 0 4px 8px rgba(27, 94, 32, 0.2) !important;
    }
    .stButton > button:active {
        transform: scale(0.97) !important;
    }

    /* Titoli sezioni bassi */
    .section-title {
        color: #1B5E20;
        font-weight: 700;
        margin-bottom: 15px;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita", "🌦️ Meteo Radar"], label_visibility="collapsed")
    st.write("---")
    st.caption("Leonardo | v2.4")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    
    # RIGA ALTA: LE CARD (QUELLE CHE TI PIACEVANO)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 VENDITE OGGI</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA 7GG</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.write("##")

    # RIGA BASSA: LE SEZIONI RIORGANIZZATE
    col_azioni, col_grafici, col_storico = st.columns([1, 2.5, 1.5])

    # ⚡ AZIONI RAPIDE
    with col_azioni:
        st.markdown('<p class="section-title">⚡ AZIONI RAPIDE</p>', unsafe_allow_html=True)
        if st.button("➕ Segna Latte"): st.toast("Vai a Stalla")
        if st.button("🛒 Nuova Vendita"): st.toast("Vai a Cassa")
        if st.button("🚜 Stato Mezzi"): st.toast("Funzione JD Prossimamente")
        if st.button("📸 Carica Foto"): st.toast("In arrivo...")

    # 📈 I DUE GRAFICI AFFIANCATI (PRODUZIONE E ENTRATE)
    with col_grafici:
        st.markdown('<div class="content-box">', unsafe_allow
