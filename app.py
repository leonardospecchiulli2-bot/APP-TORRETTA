import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="Torretta Management PRO", layout="wide", page_icon="🐄")

# --- 2. STILE BEIGE & VERDE ELITE ---
st.markdown("""
<style>
    .stApp { background-color: #FDFBF0; color: #1B3022; }
    [data-testid="stSidebar"] { background-color: #1B3022 !important; }
    [data-testid="stSidebar"] * { color: #FDFBF0 !important; }
    
    .main-card {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #E0E0C0;
        border-left: 8px solid #2E7D32;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .stat-val { font-size: 35px; font-weight: bold; color: #2E7D32; display: block; }
    .stat-label { font-size: 14px; color: #5D6D5F; text-transform: uppercase; font-weight: bold; }
    
    .stButton>button {
        background-color: #2E7D32; color: #FDFBF0; border-radius: 10px;
        font-weight: bold; height: 3.5em; width: 100%; border: none;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE COMPLETO ---
if 'stalla_db' not in st.session_state:
    st.session_state.stalla_db = pd.DataFrame([
        {'Marca': 'IT001', 'Nome': 'Regina', 'Sesso': 'Femmina', 'Categoria': 'Vacca', 'Stato': 'Lattazione', 'Litri': 32},
        {'Marca': 'IT005', 'Nome': 'Toro', 'Sesso': 'Maschio', 'Categoria': 'Torello', 'Stato': '-', 'Litri': 0},
        {'Marca': 'IT009', 'Nome': 'Piccola', 'Sesso': 'Femmina', 'Categoria': 'Vitello', 'Stato': 'Svezzamento', 'Litri': 0}
    ])

if 'vendite_log' not in st.session_state:
    st.session_state.vendite_log = pd.DataFrame(columns=['Orario', 'Prodotto', 'Importo'])
if 'cassa_totale' not in st.session_state: st.session_state.cassa_totale = 0.0

# --- 4. MENU ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    sel = option_menu(None, ["Dashboard", "Registro Stalla", "Cassa & Vendite", "JD-Link"], 
        icons=['speedometer2', 'clipboard2-pulse', 'cart4', 'truck'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "nav-link": {"color": "#FDFBF0", "font-size": "16px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#2E7D32"}
        })

# --- 5. LOGICA PAGINE ---

if sel == "Dashboard":
    st.title("📊 Centro di Controllo Aziendale")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='main-card'><span class='stat-label'>🥛 Latte Oggi</span><span class='stat-val'>{st.session_state.stalla_db['Litri'].sum()} L</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='main-card'><span class='stat-label'>🐄 Capi Totali</span><span class='stat-val'>{len(st.session_state.stalla_db)}</span></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='main-card'><span class='stat-label'>💰 Incasso Giorno</span><span class='stat-val'>{st.session_state.cassa_totale:.2f} €</span></div>", unsafe_allow_html=True)

    st.write("### 📈 Produzione Settimanale")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'], y=[1100, 1250, 1220, 1300, 1280, 1350, 1400],
                    mode='lines+markers', line=dict(color='#2E7D32', width=4), fill='tozeroy', fillcolor='rgba(46, 125, 50, 0.1)'))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

elif sel == "Registro Stalla":
    st.title("🐄 Registro Anagrafico Mandria")
    
    t1, t2 = st.tabs(["📋 Lista Animali", "➕ Inserisci Nuovo Capo"])
    
    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        # Mostriamo la tabella con tutti i dettagli tecnici
        st.dataframe(st.session_state.stalla_db, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with t2:
        with st.form("nuovo_animale"):
            st.write("#### Dati Identificativi")
            col1, col2 = st.columns(2)
            ma = col1.text_input("Marca Auricolare (Es. IT...)")
            no = col2.text_input("Nome Animale")
            
            st.write("#### Caratteristiche")
            c3, c4, c5 = st.columns(3)
            sex = c3.selectbox("Sesso", ["Femmina", "Maschio"])
            cat = c4.selectbox("Categoria", ["Vacca", "Vitello", "Manza", "Torello", "Bue"])
            sta = c5.selectbox("Stato Fisiologico", ["Lattazione", "Asciutta", "Svezzamento", "Ingrasso", "Infermeria"])
            
            li = st.number_
