import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configurazione
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS - STILE
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background-color: white !important; border: 1px solid #ddd !important;
        padding: 10px !important; border-radius: 10px !important; margin-bottom: 5px !important;
    }
    div[role="radiogroup"] > label:has(input:checked) { background-color: #1B5E20 !important; }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }
    .metric-card {
        background: white; padding: 15px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff; border-radius: 10px; padding: 10px 20px; border: 1px solid #ddd;
    }
    .stTabs [aria-selected="true"] { background-color: #1B5E20 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.header("🛡️ TORRETTA PRO")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")

# 4. Logica Database (Simulata in memoria)
if 'stalla_db' not in st.session_state:
    st.session_state.stalla_db = pd.DataFrame([
        {"Codice": "IT001", "Sesso": "Femmina", "Tipo": "Adulto", "Stato": "In Mungitura"},
        {"Codice": "IT002", "Sesso": "Maschio", "Tipo": "Vitello", "Stato": "In Stalla"},
        {"Codice": "IT003", "Sesso": "Femmina", "Tipo": "Vitello", "Stato": "In Stalla"}
    ])

# 5. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 EURO</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)
    st.markdown("---")
    col_l, col_e = st.columns(2)
    with col_l:
        st.subheader("🥛 Latte")
        st.bar_chart(pd.DataFrame({'Litri': [1200, 1250, 1180, 1300, 1280, 1350, 1240]}, index=['L','M','M','G','V','S','D']), color="#2E7D32")
    with col_e:
        st.subheader("💰 Euro")
        st.bar_chart(pd.DataFrame({'Euro': [350, 410, 320, 500, 460, 620, 450]}, index=['L','M','M','G','V','S','D']), color="#FFA000")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla Fotografico")
    
    # SEPARAZIONE IN TAB (SCHEDE)
    tab1, tab2, tab3 = st.tabs(["🥛 Femmine in Mungitura", "👶 Vitelli / Giovani", "🐂 Maschi Adulti"])
    
    db = st.session_state.stalla_db

    with tab1:
        st.subheader("Capi in Produzione")
        df_mung = db[(db["Sesso"] == "Femmina") & (db["Stato"] == "In Mungitura")]
        st.data_editor(df_mung, use_container_width=True, num_rows="dynamic")
        st.file_uploader("Allega foto Capo (Mungitura)", type=['jpg', 'png'], key="foto_mung")

    with tab2:
        st.subheader("Vitelli e Rimonta")
        df_vit = db[db["Tipo"] == "Vitello"]
        st.data_editor(df_vit, use_container_width=True, num_rows="dynamic")
        st.file_uploader("Allega foto Vitello", type=['jpg', 'png'], key="foto_vit")

    with tab3:
        st.subheader("Tori e Maschi")
        df_maschi = db[(db["Sesso"] == "Maschio") & (db["Tipo"] == "Adulto")]
        st.data_editor(df_maschi, use_container_width=True, num_rows="dynamic")
        st.file_uploader("Allega foto Maschio", type=['jpg', 'png'], key="foto_mas")

    if st.button("💾 AGGIORNA TUTTO IL REGISTRO"):
        st.success("Dati e foto salvati nel database!")

elif scelta == "🧀 Vendite":
    st.title("🧀 Punto Vendita")
    st.info("Prossimo passo: Trasformare anche questa in una tabella prodotti!")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Radar")
    url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isPlay=1&color=6"
    st.components.v1.iframe(url, height=500)
