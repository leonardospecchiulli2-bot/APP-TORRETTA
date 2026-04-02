import streamlit as st

# Impostazioni base
st.set_page_config(page_title="App Torretta", layout="centered")

st.title("🚜 Azienda Agricola Torretta")
st.sidebar.title("Menu")

opzione = st.sidebar.radio("Seleziona:", ["Home", "🐄 Stalla", "🧀 Vendite", "⛈️ Meteo"])

if opzione == "Home":
    st.write("Benvenuto nell'app della Torretta! Da qui gestisci tutto gratis.")

elif opzione == "🐄 Stalla":
    st.header("Produzione Latte")
    litri = st.number_input("Litri munti oggi:", min_value=0.0)
    if st.button("Salva"):
        st.success(f"Registrati {litri} litri!")

elif opzione == "🧀 Vendite":
    st.header("Punto Vendita")
    prodotto = st.selectbox("Cosa hai venduto?", ["Formaggio", "Carne", "Uova"])
    euro = st.number_input("Incasso (€):", min_value=0.0)
    if st.button("Registra"):
        st.success(f"Vendita di {prodotto} per {euro}€ salvata!")

elif opzione == "⛈️ Meteo":
    st.header("Meteo Radar")
    st.write("Qui collegheremo il radar della tua zona.")
