import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="Torretta Management PRO", layout="wide", page_icon="🌿")

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
    .stButton>button:hover { background-color: #1B3022; border: 1px solid #2E7D32; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE COMPLETO (SESSION STATE) ---
if 'stalla_db' not in st.session_state:
    st.session_state.stalla_db = pd.DataFrame([
        {'ID': 'IT001', 'Nome': 'Regina', 'Stato': 'Lattazione', 'Salute': 'Ottima', 'Mungitura': '06:00', 'Litri': 32},
        {'ID': 'IT002', 'Nome': 'Mora', 'Stato': 'Asciutta', 'Salute': 'Monitoraggio', 'Mungitura': '-', 'Litri': 0}
    ])

if 'vendite_log' not in st.session_state:
    st.session_state.vendite_log = pd.DataFrame(columns=['Orario', 'Prodotto', 'Importo'])

if 'cassa_totale' not in st.session_state: st.session_state.cassa_totale = 0.0

# --- 4. MENU LATERALE ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    sel = option_menu(None, ["Dashboard", "Stalla Dettagliata", "Cassa & Vendite", "JD-Link"], 
        icons=['speedometer2', 'cow', 'cart4', 'truck'], 
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
        st.markdown(f"<div class='main-card'><span class='stat-label'>🥛 Latte Totale</span><span class='stat-val'>{st.session_state.stalla_db['Litri'].sum()} L</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='main-card'><span class='stat-label'>🐄 Capi in Stalla</span><span class='stat-val'>{len(st.session_state.stalla_db)}</span></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='main-card'><span class='stat-label'>💰 Incasso Giorno</span><span class='stat-val'>{st.session_state.cassa_totale:.2f} €</span></div>", unsafe_allow_html=True)

    st.write("### 📈 Andamento Produzione")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'], y=[1100, 1250, 1220, 1300, 1280, 1350, 1400],
                    mode='lines+markers', line=dict(color='#2E7D32', width=4), fill='tozeroy', fillcolor='rgba(46, 125, 50, 0.1)'))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

elif sel == "Stalla Dettagliata":
    st.title("🐄 Registro Avanzato Stalla")
    
    t1, t2 = st.tabs(["📋 Lista Mandria", "➕ Registra Nuovo Capo"])
    
    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.dataframe(st.session_state.stalla_db, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with t2:
        with st.form("nuova_vacca"):
            col1, col2 = st.columns(2)
            id_v = col1.text_input("Marca Auricolare")
            nome_v = col2.text_input("Nome Vacca")
            stato_v = col1.selectbox("Stato", ["Lattazione", "Asciutta", "Rimonta", "Infermeria"])
            salute_v = col2.selectbox("Salute", ["Ottima", "Monitoraggio", "Trattamento"])
            litri_v = st.number_input("Litri/Giorno", 0)
            if st.form_submit_button("REGISTRA IN STALLA"):
                nuova = {'ID': id_v, 'Nome': nome_v, 'Stato': stato_v, 'Salute': salute_v, 'Mungitura': 'Da fare', 'Litri': litri_v}
                st.session_state.stalla_db = pd.concat([st.session_state.stalla_db, pd.DataFrame([nuova])], ignore_index=True)
                st.rerun()

elif sel == "Cassa & Vendite":
    st.title("🛒 Gestione Cassa")
    
    col_a, col_b = st.columns([1, 1.5])
    
    with col_a:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.write("#### Nuova Vendita")
        prod = st.selectbox("Prodotto", ["Latte Crudo", "Caciocavallo", "Ricotta", "Formaggio Stagionato"])
        prezzo = st.number_input("Importo (€)", min_value=0.0, step=0.50)
        if st.button("REGISTRA VENDITA"):
            st.session_state.cassa_totale += prezzo
            ora = datetime.now().strftime("%H:%M")
            nuova_v = {'Orario': ora, 'Prodotto': prod, 'Importo': prezzo}
            st.session_state.vendite_log = pd.concat([st.session_state.vendite_log, pd.DataFrame([nuova_v])], ignore_index=True)
            st.success("Vendita salvata!")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_b:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.write("#### Storico Operazioni Odierne")
        st.table(st.session_state.vendite_log)
        st.markdown("</div>", unsafe_allow_html=True)

elif sel == "JD-Link":
    st.title("🚜 Telemetria John Deere")
    st.info("Piattaforma pronta per la connessione. Domani inseriremo i dati API.")
