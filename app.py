import streamlit as st

st.set_page_config(page_title="Torretta Pro", layout="wide")

# CSS - MENU A BOTTONI VERDI SENZA PALLINI
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* TRASFORMA RADIO IN BOTTONI NEL MENU */
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: white;
        padding: 12px 20px !important;
        border-radius: 12px !important;
        border: 1px solid #E0E0E0 !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    
    /* NASCONDE IL CERCHIETTO FISICO */
    div.row-widget.stRadio > div[role="radiogroup"] > label div:first-child { display: none !important; }

    /* TESTO MENU */
    div.row-widget.stRadio > div[role="radiogroup"] > label p {
        font-size: 18px !important;
        font-weight: 600 !important;
        margin: 0 !important;
        text-align: center;
    }

    /* EFFETTO SELEZIONE VERDE */
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        border: none !important;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) p {
        color: white !important;
    }

    /* CARD DASHBOARD */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 5px solid #1B5E20;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* BOTTONI AZIONI RAPIDE */
    .stButton>button {
        height: 80px;
        font-size: 18px !important;
        font-weight: bold;
        border-radius: 12px;
        background-color: #2E7D32 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#1B5E20;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    scelta = st.radio("MENU", ["📊 Dashboard", "🐄 Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")

# LOGICA PAGINE
if scelta == "📊 Dashboard":
    st.title("📊 Riepilogo Aziendale")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 Latte</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 Vendite</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ Pioggia</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)
    
    st.write("##")
    st.subheader("⚡ Azioni Rapide")
    b1, b2, b3 = st.columns(3)
    with b1: st.button("➕ REGISTRA LATTE")
    with b2: st.button("🛒 NUOVA VENDITA")
    with b3: st.button("📡 VEDI RADAR")

elif scelta == "🐄 Stalla":
    st.title("🐄 Registro Stalla")
    st.number_input("Litri totali", min_value=0.0)
    st.button("SALVA DATI")

elif scelta == "🧀 Vendite":
    st.title("🧀 Gestione Cassa")
    st.number_input("Incasso (€)", min_value=0.0)
    st.button("REGISTRA")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Radar Pioggia Real-Time")
    # Radar professionale interattivo centrato sulla Puglia
    radar_url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isVis_0=1&opacity_0=0.7&isPlay=1&isLoop=1&color=6"
    st.components.v1.iframe(radar_url, height=500)
    st.info("Puoi zoomare sulla mappa per vedere i tuoi campi.")
