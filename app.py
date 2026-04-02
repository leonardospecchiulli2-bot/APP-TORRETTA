import streamlit as st

st.set_page_config(page_title="Torretta Pro", layout="wide")

# CSS - MENU VERDE SENZA PALLINI E DASHBOARD
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5; }
    [data-testid="stSidebarNav"] {display: none;}
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: white; padding: 15px; border-radius: 12px;
        border: 1px solid #DDD; margin-bottom: 10px; width: 100%;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label div:first-child { display: none !important; }
    div.row-widget.stRadio > div[role="radiogroup"] > label p {
        font-size: 18px !important; font-weight: 600 !important; text-align: center;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important; border: none !important;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) p {
        color: white !important;
    }
    .metric-card {
        background-color: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .stButton>button {
        height: 80px; font-size: 20px !important; border-radius: 15px;
        background-color: #2E7D32 !important; color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#1B5E20;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    scelta = st.radio("MENU", ["📊 Dashboard", "🐄 Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")

# PAGINE
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
    st.button("SALVA")

elif scelta == "🧀 Vendite":
    st.title("🧀 Punto Vendita")
    st.number_input("Incasso (€)", min_value=0.0)
    st.button("REGISTRA")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Meteo Radar")
    st.image("https://www.meteoam.it/images/radar/radar_nazionale.png", use_container_width=True)
