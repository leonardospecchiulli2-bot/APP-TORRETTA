import streamlit as st

# --- CONFIGURAZIONE ESTETICA ---
st.set_page_config(page_title="App Torretta", page_icon="🚜", layout="centered")

# CSS personalizzato per cambiare colori e stile
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f2;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }
    h1 {
        color: #2e7d32;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #e8f5e9;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INIZIO APP ---
st.title("🚜 Azienda Agricola Torretta")
st.markdown("---")

# Menu laterale con icone
with st.sidebar:
    st.image("https://img.icons8.com/color/96/farm.png", width=100)
    st.title("Gestione")
    opzione = st.radio("Scegli cosa fare:", 
                       ["🏠 Dashboard", "🐄 Registro Stalla", "🧀 Punto Vendita", "🌦️ Meteo Radar"])

# 🏠 DASHBOARD
if opzione == "🏠 Dashboard":
    st.subheader("Situazione Generale")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🐄 Capi in Stalla: **45**")
    with col2:
        st.success("💰 Vendite oggi: **120 €**")
    
    st.markdown("### 🚜 Stato Mezzi (John Deere)")
    st.warning("🔗 Collegamento API in attesa...")

# 🐄 STALLA
elif opzione == "🐄 Registro Stalla":
    st.header("🐄 Registro Latte")
    with st.container():
        st.write("Inserisci la produzione del mattino o della sera")
        specie = st.segmented_control("Animale", ["Mucca", "Pecora"])
        litri = st.number_input("Litri totali:", min_value=0.0, step=0.5)
        note = st.text_input("Note (es. mungitura sera)")
        
        if st.button("Registra Produzione"):
            st.balloons() # Fa volare i palloncini quando salvi
            st.success(f"Registrati {litri} litri per {specie}!")

# 🧀 VENDITE
elif opzione == "🧀 Punto Vendita":
    st.header("🧀 Registro Vendite")
    prodotto = st.selectbox("Seleziona Prodotto", ["Formaggio Primo Sale", "Caciocavallo", "Carne", "Uova"])
    euro = st.number_input("Incasso totale (€):", min_value=0.0)
    
    if st.button("Conferma Vendita"):
        st.success(f"Hai venduto {prodotto} per {euro}€")

# 🌦️ METEO
elif opzione == "🌦️ Meteo Radar":
    st.header("🌦️ Monitoraggio Pioggia")
    st.markdown("### Radar in tempo reale")
    # Qui inseriamo un placeholder per il radar
    st.image("https://www.meteoam.it/images/radar/radar_nazionale.png", caption="Radar Meteo (Esempio)")
    st.info("Presto qui avrai i millimetri esatti dai tuoi sensori.")
