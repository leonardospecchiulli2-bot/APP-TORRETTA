import streamlit as st
import pandas as pd

# 1. Configurazione Pagina e Stile
st.set_page_config(page_title="Torretta Smart Pro", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Sfondo e font generale */
    .main { background-color: #f0f2f6; }
    
    /* Card per i quadratoni della dashboard */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #2E7D32;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Bottoni stile Base44 */
    .stButton>button {
        height: 80px;
        font-size: 18px !important;
        border-radius: 12px;
        border: none;
        background-color: white;
        color: #2E7D32;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2E7D32;
        color: white;
        transform: translateY(-3px);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar (Menu Laterale Professionale)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/farm.png", width=80)
    st.title("Torretta Pro")
    st.markdown("---")
    scelta = st.radio("NAVIGAZIONE", ["📊 Dashboard", "🐄 Stalla", "🧀 Punto Vendita", "🌦️ Meteo", "🚜 Mezzi JD"])
    st.markdown("---")
    st.info("Operatore: Leonardo\n\nVersione: 1.2")

# --- LOGICA DELLE PAGINE ---

if scelta == "📊 Dashboard":
    st.title("📊 Riepilogo Aziendale")
    
    # Riga delle metriche (Quadretti professionali in alto)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h4>🥛 Latte Oggi</h4><h2>142 L</h2><p style="color:green;">+5% vs ieri</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h4>💰 Incasso</h4><h2>320 €</h2><p style="color:gray;">Punto Vendita</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h4>🌦️ Pioggia</h4><h2>12 mm</h2><p style="color:blue;">Ultimi 3 giorni</p></div>', unsafe_allow_html=True)

    st.markdown("### ⚡ Azioni Rapide")
    # Griglia di bottoni a quadretti
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("➕ Registra Latte"): st.toast("Caricamento sezione Stalla...")
    with c2:
        if st.button("🛒 Nuova Vendita"): st.toast("Caricamento Cassa...")
    with c3:
        if st.button("🛰️ Apri Radar"): st.toast("Collegamento Satellite...")

elif scelta == "🐄 Stalla":
    st.title("🐄 Registro Stalla")
    # Layout a quadretti per inserimento
    with st.container():
        st.markdown('<div style="background-color:white; padding:20px; border-radius:15px;">', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            tipo = st.selectbox("Specie", ["Vacche", "Pecore"])
            litri = st.number_input("Litri munti", min_value=0.0)
        with col_b:
            data = st.date_input("Data")
            st.write("---")
            if st.button("CONFERMA REGISTRAZIONE"):
                st.success("Dato salvato correttamente!")
        st.markdown('</div>', unsafe_allow_html=True)

elif scelta == "🧀 Punto Vendita":
    st.title("🧀 Gestione Vendite")
    col_x, col_y = st.columns(2)
    with col_x:
        prod = st.multiselect("Prodotti venduti", ["Formaggio", "Ricotta", "Uova", "Carne"])
        prezzo = st.number_input("Totale Incassato (€)", min_value=0.0)
    with col_y:
        if st.button("SALVA SCONTRINO"):
            st.balloons()
            st.success("Incasso registrato!")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Monitoraggio Meteo")
    st.image("https://www.meteoam.it/images/radar/radar_nazionale.png", use_container_width=True)
    st.write("Dati pluviometrici aggiornati.")

elif scelta == "🚜 Mezzi JD":
    st.title("🚜 Flotta John Deere")
    st.warning("Modulo di connessione API JD Link attivo. Inserire le credenziali per il primo avvio.")
