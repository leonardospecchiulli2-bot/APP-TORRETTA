import streamlit as st
import pandas as pd

# 1. Configurazione base
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS "DASHBOARD PRO" - NIENTE PALLINI, SOLO STILE
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* MENU RADIO A BOTTONI */
    div[role="radiogroup"] > label {
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        padding: 12px 20px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: 0.3s ease !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        transform: translateX(10px) !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }

    /* CARD METRICHE ALTE */
    .metric-card {
        background: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    
    /* BOTTONI AZIONI */
    .stButton > button {
        width: 100% !important; height: 55px !important;
        background-color: white !important; color: #1B5E20 !important;
        border: 2px solid #1B5E20 !important; border-radius: 12px !important;
        font-weight: bold !important;
    }
    .stButton > button:hover { background-color: #1B5E20 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita", "🌦️ Meteo Radar"], label_visibility="collapsed")
    st.write("---")
    st.caption("Leonardo | v2.5")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    
    # RIGA ALTA
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 VENDITE OGGI</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA 7GG</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.write("##")
    col_az, col_gr = st.columns([1, 3])

    with col_az:
        st.subheader("⚡ Azioni")
        st.button("➕ Segna Latte")
        st.button("🛒 Nuova Vendita")
        st.button("📸 Carica Foto")

    with col_gr:
        st.subheader("📈 Andamento Settimanale")
        giorni = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
        # Dati Grafico
        df_chart = pd.DataFrame({
            'Giorno': giorni,
            'Litri Latte': [1200, 1250, 1180, 1300, 1280, 1350, 1240],
            'Euro Entrate': [350, 410, 320, 500, 460, 620, 450]
        }).set_index('Giorno')
        
        # Mostriamo entrambi i dati nel grafico
        st.bar_chart(df_chart, color=["#2E7D32", "#FFA000"])

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    st.number_input("Litri munti", min_value=0.0)
    st.button("SALVA DATI")

elif scelta == "🧀 Punto Vendita":
    st.title("🧀 Punto Vendita")
    st.number_input("Incasso (€)", min_value=0.0)
    st.button("REGISTRA")

elif scelta == "🌦️ Meteo Radar":
    st.title("🌦️ Radar Pioggia Real-Time")
    radar_url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isVis_0=1&opacity_0=0.7&isPlay=1&isLoop=1&color=6"
    st.components.v1.iframe(radar_url, height=600)
