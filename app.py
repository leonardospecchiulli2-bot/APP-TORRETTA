import streamlit as st

# 1. Configurazione base
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS "ANIMATO & CORAZZATO"
st.markdown("""
<style>
    /* Sfondo */
    .stApp { background-color: #FDFCF5 !important; }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 1px solid #eee !important; }

    /* --- MENU SENZA PALLINI + ANIMAZIONI --- */
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
        /* ANIMAZIONE DI TRANSIZIONE */
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* Effetto Hover (quando passi sopra col mouse/dito senza cliccare) */
    div[role="radiogroup"] > label:hover {
        border-color: #2E7D32 !important;
        transform: scale(1.02) !important;
        background-color: #f0f4f0 !important;
    }

    /* Stile testo */
    div[role="radiogroup"] > label p {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #444 !important;
        margin: 0 !important;
    }

    /* QUANDO SELEZIONATO: DIVENTA VERDE + MOVIMENTO */
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        border-color: #1B5E20 !important;
        color: white !important;
        transform: translateX(12px) !important; /* Movimento laterale */
        box-shadow: 0 5px 15px rgba(27, 94, 32, 0.3) !important;
    }
    
    div[role="radiogroup"] > label:has(input:checked) p {
        color: #ffffff !important;
    }

    /* Dashboard Cards con animazione al passaggio */
    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-top: 5px solid #1B5E20;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-8px);
    }

    /* Bottoni Dashboard Grandi */
    .stButton > button {
        width: 100% !important;
        height: 110px !important;
        background: linear-gradient(135deg, #2E7D32, #1B5E20) !important;
        color: white !important;
        border-radius: 18px !important;
        font-weight: bold !important;
        font-size: 22px !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:active {
        transform: scale(0.95) !important; /* Effetto pressione */
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    
    scelta = st.radio(
        "NAVIGAZIONE",
        ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita", "🌦️ Meteo Radar"],
        label_visibility="collapsed"
    )
    
    st.write("---")
    st.caption("Operatore: Leonardo | v2.2")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 VENDITE</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.write("##")
    st.subheader("⚡ Operazioni Rapide")
    b1, b2, b3 = st.columns(3)
    with b1: st.button("📝\nSEGNA\nLATTE")
    with b2: st.button("🛒\nNUOVA\nVENDITA")
    with b3: st.button("🌦️\nVEDI\nRADAR")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    st.number_input("Litri munti", min_value=0.0)
    if st.button("SALVA DATI"): st.balloons()

elif scelta == "🧀 Punto Vendita":
    st.title("🧀 Punto Vendita")
    st.number_input("Incasso (€)", min_value=0.0)
    if st.button("REGISTRA"): st.success("Vendita registrata!")

elif scelta == "🌦️ Meteo Radar":
    st.title("🌦️ Radar Pioggia Real-Time")
    radar_url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isVis_0=1&opacity_0=0.7&isPlay=1&isLoop=1&color=6"
    st.components.v1.iframe(radar_url, height=600)
