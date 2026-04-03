import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from datetime import datetime

# 1. CONFIGURAZIONE ULTRA-PREMIUM
st.set_page_config(
    page_title="Torretta Elite v20",
    page_icon="🚜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. STILE CSS AVANZATO (Design Moderno)
st.markdown("""
<style>
    /* Sfondo generale */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Sidebar elegante */
    section[data-testid="stSidebar"] {
        background-color: #1b3d2f !important;
    }
    
    /* Card Personalizzate */
    .metric-card {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 20px;
        border-left: 10px solid #2E7D32;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        transition: transform 0.3s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    /* Testi */
    h1, h2, h3 {
        color: #1b3d2f;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Bottoni stile iOS */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        border: none;
        height: 3.5em;
        background: linear-gradient(145deg, #2E7D32, #1b3d2f);
        color: white;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(46, 125, 50, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 3. GESTIONE DATI (Simulata per ora)
if 'prod' not in st.session_state:
    st.session_state.prod = {"Latte": 1240, "Formaggi": 45, "Cassa": 150.50}
if 'log_vendite' not in st.session_state:
    st.session_state.log_vendite = pd.DataFrame({
        'Ora': ['08:00', '09:30', '11:00'],
        'Prodotto': ['Latte', 'Caciocavallo', 'Ricotta'],
        'Prezzo': [20.0, 45.0, 15.0]
    })

# 4. MENU LATERALE ICONICO
with st.sidebar:
    st.markdown("<h1 style='color: white; text-align: center;'>🛡️ TORRETTA PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Stalla", "Cassa", "JD-Link"],
        icons=["speedometer2", "cow", "bag-check", "shredder"],
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#C0C0C0", "font-size": "20px"}, 
            "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "#2E7D32"},
        }
    )
    st.write("---")
    st.caption(f"Ultimo aggiornamento: {datetime.now().strftime('%H:%M:%S')}")

# --- PAGINA DASHBOARD ---
if selected == "Dashboard":
    st.title("📊 Centro di Controllo")
    
    # Widget a tre colonne con design a card
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class='metric-card'>
            <small>PRODUZIONE LATTE</small>
            <div style='font-size: 32px; font-weight: bold;'>{st.session_state.prod['Latte']} L</div>
            <p style='color: green;'>↑ 2.4% da ieri</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class='metric-card'>
            <small>FORME IN MATURAZIONE</small>
            <div style='font-size: 32px; font-weight: bold;'>{st.session_state.prod['Formaggi']} pz</div>
            <p style='color: #2E7D32;'>Stato: Ottimale</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class='metric-card' style='border-left-color: #FFD700;'>
            <small>INCASSO GIORNALIERO</small>
            <div style='font-size: 32px; font-weight: bold;'>{st.session_state.prod['Cassa']} €</div>
            <p style='color: #daa520;'>Obiettivo: 80%</p>
        </div>""", unsafe_allow_html=True)

    st.write("### 📈 Performance Settimanale")
    df_grafico = pd.DataFrame({
        'Giorno': ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'],
        'Litri': [1100, 1250, 1240, 1300, 1280, 1350, 1400]
    })
    fig = px.area(df_grafico, x='Giorno', y='Litri', color_discrete_sequence=['#2E7D32'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

# --- PAGINA CASSA ---
elif selected == "Cassa":
    st.title("🛒 Terminale di Vendita")
    
    col_v1, col_v2 = st.columns([1, 2])
    
    with col_v1:
        st.write("#### ⚡ Azione Rapida")
        if st.button("➕ Vendi 1L Latte"):
            st.session_state.prod['Cassa'] += 1.50
            st.balloons()
        if st.button("➕ Vendi 1 Ricotta"):
            st.session_state.prod['Cassa'] += 5.0
            st.toast("Vendita registrata!")
        
    with col_v2:
        st.write("#### 📋 Registro Ultime Operazioni")
        st.dataframe(st.session_state.log_vendite, use_container_width=True)

# --- PAGINA JD-LINK ---
elif selected == "JD-Link":
    st.title("🚜 Telemetria Macchinari")
    st.markdown("""
        <div style='background-color: white; padding: 30px; border-radius: 20px; border: 1px solid #ddd;'>
            <h3 style='color: #1b3d2f;'>📡 Connessione in attesa</h3>
            <p>In attesa delle credenziali di <b>Azienda Agricola Torretta</b>.</p>
            <hr>
            <div style='display: flex; justify-content: space-between;'>
                <div><b>Trattore 6120:</b> <span style='color: orange;'>⚠️ Manutenzione</span></div>
                <div><b>Gasolio:</b> 65%</div>
                <div><b>Ore Lavoro:</b> 1.450h</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
