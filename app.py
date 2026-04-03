import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from datetime import datetime

# --- CONFIGURAZIONE E STILE ---
st.set_page_config(page_title="Torretta Management PRO", layout="wide", page_icon="🐄")

st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    [data-testid="stSidebar"] { background-color: #1b3d2f !important; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); border-top: 5px solid #2E7D32; }
    .stat-title { color: #666; font-size: 14px; text-transform: uppercase; font-weight: bold; }
    .stat-value { color: #2E7D32; font-size: 30px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- DATABASE INTERNO ---
if 'stalla_db' not in st.session_state:
    st.session_state.stalla_db = pd.DataFrame([
        {'Marca Auricolare': 'IT0192', 'Nome': 'Bella', 'Razza': 'Frisona', 'Stato': 'Lattazione', 'Litri/Giorno': 32.5},
        {'Marca Auricolare': 'IT0195', 'Nome': 'Stella', 'Razza': 'Bruna', 'Stato': 'Asciutta', 'Litri/Giorno': 0.0}
    ])

if 'cassa' not in st.session_state: st.session_state.cassa = 0.0

# --- MENU ---
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    selected = option_menu(None, ["Dashboard", "Registro Stalla", "Cassa Vendite", "JD-Link"], 
        icons=['speedometer2', 'clipboard-data', 'cart-check', 'truck'], 
        menu_icon="cast", default_index=0,
        styles={"nav-link": {"color": "white"}, "nav-link-selected": {"background-color": "#2E7D32"}})

# --- LOGICA PAGINE ---

if selected == "Dashboard":
    st.title("📊 Riepilogo Aziendale")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='card'><div class='stat-title'>Produzione Latte</div><div class='stat-value'>{st.session_state.stalla_db['Litri/Giorno'].sum()} L</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><div class='stat-title'>Capi Totali</div><div class='stat-value'>{len(st.session_state.stalla_db)}</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='card'><div class='stat-title'>Incasso Lordo</div><div class='stat-value'>{st.session_state.cassa:.2f} €</div></div>", unsafe_allow_html=True)

    st.write("---")
    st.subheader("📈 Andamento Latte")
    # Grafico dettagliato
    df_chart = pd.DataFrame({'Giorno': ['Lun','Mar','Mer','Gio','Ven','Sab','Dom'], 'Produzione': [1180, 1220, 1240, 1210, 1250, 1310, 1290]})
    fig = px.area(df_chart, x='Giorno', y='Produzione', line_shape='spline', color_discrete_sequence=['#2E7D32'])
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Registro Stalla":
    st.title("🐄 Gestione Mandria")
    
    tab1, tab2, tab3 = st.tabs(["📋 Elenco Capi", "➕ Nuovo Ingresso", "🩺 Salute/Produzione"])
    
    with tab1:
        st.write("### Anagrafica Attuale")
        st.dataframe(st.session_state.stalla_db, use_container_width=True)
        
    with tab2:
        st.write("### Registra Nuova Vacca")
        with st.form("form_stalla"):
            c1, c2 = st.columns(2)
            marca = c1.text_input("Marca Auricolare (Es. IT...)")
            nome = c2.text_input("Nome Capo")
            razza = c1.selectbox("Razza", ["Frisona", "Bruna", "Pezzata Rossa", "Jersey"])
            stato = c2.selectbox("Stato", ["Lattazione", "Asciutta", "Rimonta", "Infermeria"])
            litri = st.number_input("Litri medi al giorno", min_value=0.0)
            
            if st.form_submit_button("Aggiungi in Stalla"):
                nuova_v = {'Marca Auricolare': marca, 'Nome': nome, 'Razza': razza, 'Stato': stato, 'Litri/Giorno': litri}
                st.session_state.stalla_db = pd.concat([st.session_state.stalla_db, pd.DataFrame([nuova_v])], ignore_index=True)
                st.success(f"{nome} registrata correttamente!")
                st.rerun()

    with tab3:
        st.info("Qui aggiungeremo i grafici sulla salute e i giorni medi di lattazione.")

elif selected == "Cassa Vendite":
    st.title("🛒 Punto Vendita")
    c1, c2 = st.columns([1, 1])
    with c1:
        st.write("### Nuova Vendita")
        prod = st.selectbox("Seleziona Prodotto", ["Latte Crudo", "Caciocavallo", "Ricotta", "Primo Sale"])
        prezzo = st.number_input("Importo (€)", min_value=0.0)
        if st.button("Registra Incasso"):
            st.session_state.cassa += prezzo
            st.toast("Incasso salvato!")
            st.balloons()
    with c2:
        st.write("### Totale oggi")
        st.markdown(f"<div style='font-size:50px; color:#2E7D32; font-weight:bold;'>{st.session_state.cassa:.2f} €</div>", unsafe_allow_html=True)

elif selected == "JD-Link":
    st.title("🚜 Telemetria Macchine")
    st.warning("Pronto per il collegamento con l'account di papà.")
    st.markdown("""
        <div style='background:white; padding:20px; border-radius:10px; border:1px solid #eee;'>
            <h4>📡 Status API: In attesa</h4>
            <p>Appena avremo il <b>Client ID</b> e il <b>Secret</b>, qui vedremo la mappa dei terreni e lo stato dei trattori.</p>
        </div>
    """, unsafe_allow_html=True)
