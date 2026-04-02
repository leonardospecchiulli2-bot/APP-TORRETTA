import streamlit as st

# 1. Configurazione Pagina
st.set_page_config(page_title="Torretta Smart Pro", page_icon="🛡️", layout="wide")

# 2. Design Personalizzato (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #FDFCF5; color: #333333; }
    h1, h2, h3 { color: #1B5E20 !important; font-family: sans-serif; }
    
    /* Card Metriche */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 5px solid #1B5E20;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Bottoni Grandi Verdi */
    .stButton>button {
        height: 100px;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 15px;
        background-color: #2E7D32 !important;
        color: white !important;
        border: none;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.title("🛡️ Torretta Pro")
    st.markdown("---")
    scelta = st.radio("MENU", ["📊 Dashboard", "🐄 Stalla", "🧀 Vendite", "🌦️ Meteo"])
    st.markdown("---")
    st.caption("Accesso: Leonardo")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Riepilogo Aziendale")
    
    # Metriche
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-card"><h4>🥛 Latte</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card"><h4>💰 Vendite</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><h4>🌦️ Pioggia</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.markdown("### ⚡ Azioni Rapide")
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("➕ LATTE"): st.toast("Vai a sezione Stalla")
    with b2:
        if st.button("🛒 CASSA"): st.toast("Vai a sezione Vendite")
    with b3:
        if st.button("📡 RADAR"): st.toast("Caricamento...")

elif scelta == "🐄 Stalla":
    st.title("🐄 Registro Stalla")
    with st.expander("Inserisci Nuova Mungitura", expanded=True):
        litri = st.number_input("Litri totali", min_value=0.0)
        if st.button("SALVA"):
            st.success("Dato salvato!")

elif scelta == "🧀 Vendite":
    st.title("🧀 Punto Vendita")
    euro = st.number_input("Incasso (€)", min_value=0.0)
    if st.button("REGISTRA"):
        st.balloons()
        st.success("Vendita registrata!")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Meteo Radar")
    st.image("https://www.meteoam.it/images/radar/radar_nazionale.png", use_container_width=True)
