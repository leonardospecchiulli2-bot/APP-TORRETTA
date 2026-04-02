import streamlit as st

# Configurazione Pagina
st.set_page_config(page_title="Torretta Smart", page_icon="🚜", layout="centered")

# CSS per imitare lo stile "App a bottoni" di Base44
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .main-button {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #E0E0E0;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .stButton>button {
        height: 100px;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 15px;
        border: 2px solid #2E7D32;
        background-color: white;
        color: #2E7D32;
    }
    .stButton>button:hover {
        background-color: #2E7D32;
        color: white;
    }
    h1 { color: #1B5E20; text-align: center; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚜 Torretta Smart")
st.markdown("<p style='text-align: center;'>Gestione Aziendale Semplificata</p>", unsafe_allow_html=True)

# Creazione della Griglia tipo App
col1, col2 = st.columns(2)

with col1:
    if st.button("🐄\nSTALLA"):
        st.session_state.page = "stalla"
    if st.button("🌦️\nMETEO"):
        st.session_state.page = "meteo"

with col2:
    if st.button("🧀\nVENDITE"):
        st.session_state.page = "vendite"
    if st.button("🚜\nMEZZI"):
        st.session_state.page = "mezzi"

st.markdown("---")

# Gestione delle pagine (Sottosezioni)
if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "stalla":
    st.header("Registro Stalla")
    tipo = st.radio("Seleziona:", ["Mucche", "Pecore"], horizontal=True)
    litri = st.number_input("Litri munti:", min_value=0.0)
    if st.button("SALVA DATO"):
        st.success("Dato registrato!")
    if st.button("⬅️ Torna Indietro"):
        st.session_state.page = "home"
        st.rerun()

elif st.session_state.page == "vendite":
    st.header("Punto Vendita")
    prod = st.selectbox("Prodotto:", ["Formaggio", "Carne", "Altro"])
    prezzo = st.number_input("Euro:", min_value=0.0)
    if st.button("CONFERMA"):
        st.success("Vendita salvata!")
    if st.button("⬅️ Torna Indietro"):
        st.session_state.page = "home"
        st.rerun()

elif st.session_state.page == "meteo":
    st.header("Meteo Radar")
    st.image("https://www.meteoam.it/images/radar/radar_nazionale.png")
    if st.button("⬅️ Torna Indietro"):
        st.session_state.page = "home"
        st.rerun()

elif st.session_state.page == "mezzi":
    st.header("John Deere Link")
    st.info("Connessione ai trattori in corso...")
    if st.button("⬅️ Torna Indietro"):
        st.session_state.page = "home"
        st.rerun()
