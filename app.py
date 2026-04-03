import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Torretta Elite PRO", layout="wide", page_icon="🐄")

# --- STILE BEIGE & VERDE FORESTA ---
st.markdown("""
<style>
    .stApp { background-color: #FDFBF0; color: #1B3022; }
    [data-testid="stSidebar"] { background-color: #1B3022 !important; }
    [data-testid="stSidebar"] * { color: #FDFBF0 !important; }
    .main-card {
        background: #FFFFFF; border-radius: 15px; padding: 20px;
        border-left: 8px solid #2E7D32; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px; color: #1B3022;
    }
    .stat-val { font-size: 35px; font-weight: bold; color: #2E7D32; }
</style>
""", unsafe_allow_html=True)

# --- DATABASE ---
if 'stalla_db' not in st.session_state:
    st.session_state.stalla_db = pd.DataFrame([
        {'Marca': 'IT001', 'Nome': 'Regina', 'Sesso': 'Femmina', 'Categoria': 'Vacca', 'Stato': 'Lattazione', 'Litri': 32},
        {'Marca': 'IT005', 'Nome': 'Toro', 'Sesso': 'Maschio', 'Categoria': 'Torello', 'Stato': 'Ingrasso', 'Litri': 0}
    ])
if 'cassa' not in st.session_state: st.session_state.cassa = 0.0

# --- MENU ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    sel = option_menu(None, ["Dashboard", "Registro Stalla", "Cassa & Vendite", "JD-Link"], 
        icons=['speedometer2', 'clipboard2-pulse', 'cart4', 'truck'], 
        menu_icon="cast", default_index=0,
        styles={"nav-link": {"color": "#FDFBF0"}, "nav-link-selected": {"background-color": "#2E7D32"}})

# --- LOGICA ---
if sel == "Dashboard":
    st.title("📊 Riepilogo Aziendale")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f"<div class='main-card'><b>🥛 Latte Oggi</b><br><span class='stat-val'>{st.session_state.stalla_db['Litri'].sum()} L</span></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='main-card'><b>🐄 Capi Totali</b><br><span class='stat-val'>{len(st.session_state.stalla_db)}</span></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='main-card'><b>💰 Cassa</b><br><span class='stat-val'>{st.session_state.cassa:.2f} €</span></div>", unsafe_allow_html=True)

    fig = go.Figure(go.Scatter(x=['Lun','Mar','Mer','Gio','Ven','Sab','Dom'], y=[1100, 1250, 1220, 1300, 1280, 1350, 1400], fill='tozeroy', line_color='#2E7D32'))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300)
    st.plotly_chart(fig, use_container_width=True)

elif sel == "Registro Stalla":
    st.title("🐄 Gestione Professionale Mandria")
    t1, t2 = st.tabs(["📋 Elenco Capi", "➕ Nuovo Inserimento"])
    
    with t1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.dataframe(st.session_state.stalla_db, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with t2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        with st.form("form_stalla"):
            col1, col2 = st.columns(2)
            ma = col1.text_input("Marca Auricolare")
            no = col2.text_input("Nome")
            
            c3, c4, c5 = st.columns(3)
            sex = c3.selectbox("Sesso", ["Femmina", "Maschio"])
            cat = c4.selectbox("Categoria", ["Vacca", "Vitello", "Manza", "Torello", "Toro"])
            sta = c5.selectbox("Stato Fisiologico", ["Lattazione", "Asciutta", "Svezzamento", "Ingrasso"])
            
            li = st.number_input("Produzione Litri/Giorno", min_value=0, value=0)
            
            # IL PULSANTE DI INVIO (Risolve Foto 9)
            if st.form_submit_button("REGISTRA CAPO"):
                nuovo = {'Marca': ma, 'Nome': no, 'Sesso': sex, 'Categoria': cat, 'Stato': sta, 'Litri': li}
                st.session_state.stalla_db = pd.concat([st.session_state.stalla_db, pd.DataFrame([nuovo])], ignore_index=True)
                st.success("Registrato!")
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

elif sel == "Cassa & Vendite":
    st.title("🛒 Cassa Rapida")
    colA, colB = st.columns(2)
    with colA:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        prz = st.number_input("Importo Vendita (€)", min_value=0.0)
        if st.button("REGISTRA"):
            st.session_state.cassa += prz
            st.success("Salvato!")
        st.markdown("</div>", unsafe_allow_html=True)
    with colB:
        st.markdown(f"<div class='main-card' style='text-align:center;'>TOTALE OGGI<br><span class='stat-val'>{st.session_state.cassa:.2f} €</span></div>", unsafe_allow_html=True)

elif sel == "JD-Link":
    st.title("🚜 Controllo Flotta John Deere")
    st.info("Configurazione API in corso. Verifica i Redirect URIs sul portale Developer.")
