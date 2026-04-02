import streamlit as st

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Torretta Pro", layout="wide", initial_sidebar_state="expanded")

# 2. CSS AGGRESSIVO PER ESTETICA PROFESSIONALE
st.markdown("""
<style>
    /* Sfondo generale e font */
    .stApp {
        background: linear-gradient(135deg, #f5f7f2 0%, #eef2e6 100%);
    }

    /* ELIMINA DEFINITIVAMENTE I PALLINI E I CERCHIETTI DEL MENU */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Rende invisibili i radio button originali (pallini) */
    div.row-widget.stRadio > div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }

    /* TRASFORMA IL MENU IN BOTTONI MODERNI */
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(0, 0, 0, 0.05) !important;
        padding: 18px 25px !important;
        border-radius: 15px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        cursor: pointer !important;
    }

    /* TESTO DEL MENU */
    div.row-widget.stRadio > div[role="radiogroup"] > label p {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #444 !important;
        text-align: left !important;
        margin: 0 !important;
    }

    /* EFFETTO SELEZIONE: IL TASTO DIVENTA VERDE TORRETTA */
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        border: none !important;
        transform: translateX(10px) !important;
        box-shadow: 0 10px 20px rgba(27, 94, 32, 0.2) !important;
    }

    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) p {
        color: white !important;
    }

    /* DASHBOARD CARD */
    .metric-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border-bottom: 5px solid #1B5E20;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* BOTTONI AZIONI (VERDI) */
    .stButton>button {
        width: 100%;
        height: 120px;
        font-size: 1.2rem !important;
        font-weight: 800 !important;
        border-radius: 20px;
        background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 8px 15px rgba(27, 94, 32, 0.2) !important;
        transition: 0.3s !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(27, 94, 32, 0.3) !important;
    }

    /* BARRA LATERALE */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #eee !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='color: #1B5E20; font-size: 28px;'>🛡️ TORRETTA PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Menu senza pallini
    scelta = st.radio(
        "NAVIGAZIONE",
        ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita", "🌦️ Meteo Radar"],
        label_visibility="collapsed"
    )
    
    st.write("---")
    st.markdown("<p style='text-align:center; color:gray;'>Leonardo | v2.0</p>", unsafe_allow_html=True)

# 4. PAGINE
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-card"><p style="color:gray;">🥛 LATTE OGGI</p><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card"><p style="color:gray;">💰 INCASSO</p><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><p style="color:gray;">🌦️ PIOGGIA</p><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.write("##")
    st.subheader("⚡ Operazioni Rapide")
    
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("📝\nSEGNA\nLATTE"): st.toast("Caricamento Stalla...")
    with b2:
        if st.button("🛒\nNUOVA\nVENDITA"): st.toast("Caricamento Cassa...")
    with b3:
        if st.button("🌦️\nCONTROLLA\nMETEO"): st.toast("Caricamento Radar...")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    st.number_input("Litri munti", min_value=0.0)
    st.button("SALVA DATI")

elif scelta == "🧀 Punto Vendita":
    st.title("🧀 Punto Vendita")
    st.number_input("Incasso (€)", min_value=0.0)
    st.button("REGISTRA VENDITA")

elif scelta == "🌦️ Meteo Radar":
    st.title("🌦️ Radar Pioggia Real-Time")
    radar_url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isVis_0=1&opacity_0=0.7&isPlay=1&isLoop=1&color=6"
    st.components.v1.iframe(radar_url, height=600)
