import streamlit as st
import pandas as pd
import numpy as np

# 1. Configurazione base
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS "EVOLUZIONE DASHBOARD"
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 1px solid #eee !important; }

    /* MENU SENZA PALLINI */
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
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        height: 100%;
    }

    /* NUOVI BOTTONI AZIONI (SOTTILI) */
    .stButton > button {
        width: 100% !important;
        height: 50px !important;
        background-color: #ffffff !important;
        color: #1B5E20 !important;
        border: 2px solid #1B5E20 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        transition: 0.3s !important;
    }
    .stButton > button:hover {
        background-color: #1B5E20 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita", "🌦️ Meteo Radar"], label_visibility="collapsed")
    st.write("---")
    st.caption("Leonardo | v2.3")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    
    # RIGA ALTA: LE CARD (QUELLE CHE TI PIACEVANO)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 VENDITE</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.write("##")

    # RIGA BASSA: LE TRE NOVITÀ (AZIONI, GRAFICO, STORICO)
    col_azioni, col_grafico, col_storico = st.columns([1, 2, 1.5])

    with col_azioni:
        st.markdown("##### ⚡ Azioni Rapide")
        if st.button("➕ Segna Latte"): st.toast("Vai a Stalla")
        if st.button("🛒 Nuova Vendita"): st.toast("Vai a Cassa")
        if st.button("🌦️ Vedi Meteo"): st.toast("Vai a Radar")
        if st.button("🚜 Stato Mezzi"): st.toast("Funzione JD Prossimamente")

    with col_grafico:
        st.markdown("##### 📈 Produzione Settimanale")
        # Dati simulati per il grafico
        chart_data = pd.DataFrame(np.random.randn(7, 1), columns=['Litri'])
        st.area_chart(chart_data, color="#2E7D32")

    with col_storico:
        st.markdown("##### 📝 Ultime Attività")
        dati_finti = {
            "Ora": ["06:30", "08:45", "10:15", "11:00"],
            "Attività": ["Mungitura", "Vendita Formaggio", "Mungitura", "Cassa"],
            "Esito": ["✅ OK", "€ 45.00", "✅ OK", "€ 22.00"]
        }
        df = pd.DataFrame(dati_finti)
        st.table(df)

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    st.number_input("Litri munti", min_value=0.0)
    st.button("SALVA")

elif scelta == "🧀 Punto Vendita":
    st.title("🧀 Punto Vendita")
    st.number_input("Incasso (€)", min_value=0.0)
    st.button("REGISTRA")

elif scelta == "🌦️ Meteo Radar":
    st.title("🌦️ Radar Pioggia Real-Time")
    radar_url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isVis_0=1&opacity_0=0.7&isPlay=1&isLoop=1&color=6"
    st.components.v1.iframe(radar_url, height=600)
