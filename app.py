import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from datetime import datetime

# 1. CONFIGURAZIONE
st.set_page_config(page_title="Torretta Pro v21", layout="wide", page_icon="🐄")

# 2. DATABASE PERSISTENTE (Stalla e Produzione)
if 'stalla_db' not in st.session_state:
    st.session_state.stalla_db = pd.DataFrame([
        {'ID': 'IT0192', 'Nome': 'Bella', 'Razza': 'Frisona', 'Stato': 'In Lattazione', 'Ultima Mungitura': '06:00'},
        {'ID': 'IT0195', 'Nome': 'Stella', 'Razza': 'Bruna', 'Stato': 'Asciutta', 'Ultima Mungitura': '-'}
    ])

if 'latte_oggi' not in st.session_state: st.session_state.latte_oggi = 1240.0
if 'cassa_oggi' not in st.session_state: st.session_state.cassa_oggi = 0.0

# 3. STILE CSS (Il look professionale che volevi)
st.markdown("""
<style>
    .stApp { background: #f8f9fa; }
    [data-testid="stSidebar"] { background-color: #1b3d2f !important; }
    .main-card { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 5px solid #2E7D32; }
    .stat-val { font-size: 35px; font-weight: bold; color: #2E7D32; }
    .stButton>button { border-radius: 12px; height: 3em; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { background-color: #1b3d2f; color: white; border: 2px solid #2E7D32; }
</style>
""", unsafe_allow_html=True)

# 4. MENU
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2396/2396069.png", width=80)
    st.markdown("<h2 style='color:white;'>TORRETTA ELITE</h2>", unsafe_allow_html=True)
    scelta = option_menu(None, ["Dashboard", "Stalla", "Cassa", "JD-Link"], 
        icons=['speedometer2', 'cow', 'cart4', 'broadcast-pin'], 
        menu_icon="cast", default_index=0,
        styles={"nav-link": {"color": "white"}, "nav-link-selected": {"background-color": "#2E7D32"}})

# --- LOGICA PAGINE ---

if scelta == "Dashboard":
    st.title("📊 Centro di Comando Aziendale")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='main-card'>🥛 LATTE TOTALE<br><span class='stat-val'>{st.session_state.latte_oggi} L</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='main-card'>🐄 CAPI IN STALLA<br><span class='stat-val'>{len(st.session_state.stalla_db)}</span></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='main-card'>💰 INCASSO<br><span class='stat-val'>{st.session_state.cassa_oggi} €</span></div>", unsafe_allow_html=True)

    st.write("### 📈 Produzione Ultimi 7 Giorni")
    df_graf = pd.DataFrame({'G': ['L','M','M','G','V','S','D'], 'L': [1150, 1200, 1240, 1190, 1210, 1260, 1300]})
    fig = px.bar(df_graf, x='G', y='L', color='L', color_continuous_scale='Greens', labels={'L':'Litri', 'G':'Giorno'})
    st.plotly_chart(fig, use_container_width=True)

elif scelta == "Stalla":
    st.title("🐄 Registro Anagrafico Stalla")
    
    tab1, tab2 = st.tabs(["📋 Elenco Capi", "➕ Aggiungi Capo"])
    
    with tab1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.dataframe(st.session_state.stalla_db, use_container_width
