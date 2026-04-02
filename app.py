import streamlit as st
import pandas as pd

# 1. Configurazione Pagina e Stile Avanzato (CSS)
st.set_page_config(page_title="Torretta Smart Pro", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* 🎨 TAVOLOZZA COLORI AZIENDALE */
    :root {
        --bg-color: #FDFCF5; /* Crema chiarissimo per lo sfondo */
        --card-color: #FFFFFF; /* Bianco per i riquadri dati */
        --primary-green: #1B5E20; /* Verde scuro per titoli e bordi */
        --action-green: #2E7D32; /* Verde intermedio per i bottoni */
        --text-dark: #333333;
    }

    /* Sfondo generale della pagina */
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-dark);
    }

    /* Stile dei Titoli Principali (h1, h2) */
    h1, h2, h3 {
        color: var(--primary-green) !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700 !important;
    }

    /* Card per i quadratoni della dashboard (Metriche) */
    .metric-card {
        background-color: var(--card-color);
        padding: 25px;
        border-radius: 20px;
        border-top: 6px solid var(--primary-green); /* Bordo colorato in alto */
        box-shadow: 0 6px 12px rgba(0,0,0,0.08); /* Ombra più morbida */
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px); /* Effetto al passaggio del mouse */
    }
    .metric-card h4 {
        color: #757575;
        margin-bottom: 5px;
        font-size: 1.1rem;
    }
    .metric-card h2 {
        margin: 0;
        font-size: 2.8rem;
    }

    /* Bottoni stile "Azione Rapida" (Grandi a quadretti) */
    .stButton>button {
        height: 90px;
        font-size: 19px !important;
        font-weight: bold;
        border-radius: 15px;
        border: none;
        background-color: var(--action-green); /* Colore pieno */
        color: white !important; /* Testo bianco */
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: var(--primary-green); /* Più scuro al passaggio */
        box-shadow: 0 6px 15px rgba(0,0,0,0.25);
        transform: scale(1.03);
    }
    
    /* Bottoni secondari (es. "Torna Indietro") */
    .stButton>button.secondary-btn {
        background-color: #f0f0f0;
        color: #333 !important;
        height: 50px;
        font-size: 16px !important;
    }

    /* Stile dei Container per i Form (Stalla, Vendite) */
    .data-form-container {
        background-color: var(--card-color);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #eee;
    }
    
    /* Personalizzazione Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f1f3f1; /* Grigio-verde chiarissimo */
        border-right: 1px solid #ddd;
    }
    section[data-testid="stSidebar"] h1 {
        color: var(--primary-green) !important;
    }
    </style>
