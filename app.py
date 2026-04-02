import streamlit as st
import pandas as pd

# 1. Configurazione base
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS "DASHBOARD PRO" - NIENTE PALLINI, SOLO STILE ELEGANTE
st.markdown("""
<style>
    .stApp {
        background-color: #FDFCF5 !important;
    }
    
    /* Rimuove i pallini e lo stile di default di Streamlit */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Stile personalizzato per il menu Radio (NAV) */
    div[role="radiogroup"] > label {
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        padding: 15px 20px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        display: flex !important;
        align-items: center !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }

    /* Nasconde il cerchietto originale */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }

    /* Stile dell'elemento selezionato */
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important; /* Verde Scuro Aziendale */
        color: white !important;
        transform: translateX(5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Forza il colore del testo quando selezionato */
    div[role="radiogroup"] > label:has(input:checked) p {
        color: white !important;
        font-weight: bold;
    }

    /* Stile card metriche alte */
    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-top: 5px solid #1B5E20;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar (Menu)
with st.sidebar:
    st.markdown("<h1 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Il menu che ora apparirà senza pallini
    scelta = st.radio(
        "NAV",
        ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita", "🌦️ Meteo Radar"],
        label_visibility="collapsed"
    )
    
    st.write("---")
    st.caption("Operatore: Leonardo | v2.4")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    
    # Metriche principali
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card"><h4>💰 VENDITE OGGI</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA 7GG</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.write("##") # Spazio
    
    # Due grafici separati (Latte e Euro)
    col_grafico1, col_grafico2 = st.columns(2)
    
    # Dati finti per il grafico (stessa logica di prima)
    giorni = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
    dati_latte = [1200, 1250, 1180, 1300, 1280, 1350, 1240]
    dati_euro = [350, 410, 320, 500, 460, 620, 450]
    
    df_chart = pd.DataFrame({
        'Giorno': giorni,
        'Litri Latte': dati_latte,
        'Euro Entrate': dati_euro
    }).set_index('Giorno')

    with col_grafico1:
        st.subheader("📈 Andamento Latte (Litri)")
        # Grafico VERDE per il latte
        st.bar_chart(df_chart['Litri Latte'], color="#2E7D32")

    with col_grafico2:
        st.subheader("📈 Andamento Entrate (Euro)")
        # Grafico ORO/ARANCIO per i soldi
        st.bar_chart(df_chart['Euro Entrate'], color="#FFA000")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    st.info("Sezione in fase di sviluppo. Qui gestirai i tuoi capi.")

elif scelta == "🧀 Punto Vendita":
    st.title("🧀 Punto Vendita")
    st.info("Sezione in fase di sviluppo. Qui registrerai le vendite.")

elif scelta == "🌦️ Meteo Radar":
    st.title("🌦️ Radar Pioggia Real-Time")
    # Integrazione di un radar pioggia esterno (RainViewer)
    radar_url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isVis_0=1&opacity_0=0.7&isPlay=1&isLoop=1&color=6"
    st.components.v1.iframe(radar_url, height=600)
