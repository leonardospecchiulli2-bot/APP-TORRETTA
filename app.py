import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime

# --- CONFIGURAZIONE E STILE AVANZATO ---
st.set_page_config(page_title="Torretta Command Center", layout="wide", page_icon="🌿")

# CSS PERSONALIZZATO PER UN LOOK MOZZAFIATO
st.markdown("""
<style>
    /* Sfondo sfumato */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
    }
    
    /* Sidebar stile moderno */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
    }
    
    /* Card Effetto Vetro */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }
    
    .stat-value {
        font-size: 40px;
        font-weight: 800;
        background: -webkit-linear-gradient(#00c853, #b2ff59);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Bottoni Premium */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(45deg, #2E7D32, #43a047);
        color: white;
        border: none;
        padding: 15px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(46, 125, 50, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- INIZIALIZZAZIONE DATI ---
if 'db_stalla' not in st.session_state:
    st.session_state.db_stalla = pd.DataFrame([
        {'ID': 'IT001', 'Nome': 'Regina', 'Stato': 'Lattazione', 'Salute': 'Ottima', 'Litri': 35},
        {'ID': 'IT002', 'Nome': 'Mora', 'Stato': 'Asciutta', 'Salute': 'Monitoraggio', 'Litri': 0}
    ])
if 'cassa_totale' not in st.session_state: st.session_state.cassa_totale = 0.0

# --- NAVIGAZIONE ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #00c853;'>TORRETTA PRO</h1>", unsafe_allow_html=True)
    menu = option_menu(None, ["Dashboard", "Gestione Stalla", "Cassa Smart", "JD-Link"], 
        icons=['cpu', 'activity', 'wallet2', 'truck'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "nav-link": {"color": "white", "font-size": "16px"},
            "nav-link-selected": {"background-color": "#2E7D32"}
        })

# --- PAGINA: DASHBOARD ---
if menu == "Dashboard":
    st.markdown("<h2 style='color: white;'>🚀 Command Center Aziendale</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='glass-card'><small>LATTE PRODOTTO</small><br><span class='stat-value'>{st.session_state.db_stalla['Litri'].sum()} L</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='glass-card'><small>CAPI ATTIVI</small><br><span class='stat-value'>{len(st.session_state.db_stalla)}</span></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='glass-card'><small>INCASSO GIORNALIERO</small><br><span class='stat-value'>{st.session_state.cassa_totale:.2f} €</span></div>", unsafe_allow_html=True)

    # Grafico High-Tech
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("📊 Flusso di Produzione")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'], y=[1100, 1250, 1220, 1300, 1280, 1350, 1400],
                    mode='lines+markers', name='Litri',
                    line=dict(color='#00c853', width=4),
                    fill='tozeroy', fillcolor='rgba(0, 200, 83, 0.1)'))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), margin=dict(l=0,r=0,t=20,b=0))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGINA: STALLA ---
elif menu == "Gestione Stalla":
    st.markdown("<h2 style='color: white;'>🐄 Registro Digitale Mandria</h2>", unsafe_allow_html=True)
    
    t1, t2 = st.tabs(["📋 Monitoraggio Capi", "➕ Nuovo Inserimento"])
    
    with t1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        # Tabella stilizzata
        st.dataframe(st.session_state.db_stalla, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with t2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        with st.form("add_cow"):
            col1, col2 = st.columns(2)
            id_c = col1.text_input("Codice Marca Auricolare")
            nome_c = col2.text_input("Nome Capo")
            stato_c = col1.selectbox("Stato Fisiologico", ["Lattazione", "Asciutta", "Rimonta"])
            salute_c = col2.selectbox("Stato Salute", ["Ottima", "Monitoraggio", "Trattamento"])
            litri_c = st.slider("Litri Giornalieri Stimati", 0, 50, 25)
            if st.form_submit_button("REGISTRA NEL SISTEMA"):
                new_row = {'ID': id_c, 'Nome': nome_c, 'Stato': stato_c, 'Salute': salute_c, 'Litri': litri_c}
                st.session_state.db_stalla = pd.concat([st.session_state.db_stalla, pd.DataFrame([new_row])], ignore_index=True)
                st.success("✅ Capo inserito con successo!")
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- PAGINA: CASSA ---
elif menu == "Cassa Smart":
    st.markdown("<h2 style='color: white;'>🛒 Terminale Punto Vendita</h2>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        prodotto = st.selectbox("Prodotto", ["Latte Crudo", "Caciocavallo", "Ricotta Fresca", "Primo Sale"])
        importo = st.number_input("Prezzo di Vendita (€)", min_value=0.0, step=0.5)
        if st.button("REGISTRA VENDITA"):
            st.session_state.cassa_totale += importo
            st.balloons()
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_b:
        st.markdown(f"<div class='glass-card' style='text-align: center;'><small>TOTALE CASSA OGGI</small><br><span style='font-size: 60px; font-weight: bold; color: #00c853;'>{st.session_state.cassa_totale:.2f} €</span></div>", unsafe_allow_html=True)

# --- PAGINA: JD-LINK ---
elif menu == "JD-Link":
    st.markdown("<h2 style='color: white;'>🚜 Integrazione JD-Link</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='glass-card' style='border-left: 5px solid #FFD700;'>
        <h3>📡 Collegamento Satellitare Pronto</h3>
        <p>In attesa della chiave API di John Deere per sincronizzare i mezzi.</p>
        <p style='color: #FFD700;'><i>Configurazione prevista: Domani mattina</i></p>
    </div>
    """, unsafe_allow_html=True)
