import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# SETUP
st.set_page_config(page_title="Torretta Smart", layout="wide")

# MEMORIA DATI
if 'storia_latte' not in st.session_state:
    st.session_state.storia_latte = pd.DataFrame({'Giorno': ['Lun', 'Mar', 'Mer'], 'Litri': [1200, 1250, 1240]})
if 'prodotti' not in st.session_state:
    st.session_state.prodotti = {"Latte": 1240, "Caciocavallo": 10, "Ricotta": 5}
if 'euro_oggi' not in st.session_state: st.session_state.euro_oggi = 0.0

# STILE
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {display: none;}
    .stMetric { background: white; padding: 15px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stButton>button { height: 60px; border-radius: 15px; font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

# MENU
with st.sidebar:
    st.markdown("## 🛡️ TORRETTA")
    scelta = option_menu(None, ["Home", "Stalla", "Cassa", "JD-Link"], 
        icons=['house', 'cow', 'cart', 'truck'], default_index=0)

if scelta == "Home":
    st.title("📊 Riepilogo Produzione")
    
    # METRICHE IN ALTO
    c1, c2, c3 = st.columns(3)
    c1.metric("Latte in Tanica", f"{st.session_state.prodotti['Latte']} L")
    c2.metric("Formaggi pronti", f"{st.session_state.prodotti['Caciocavallo']} pz")
    c3.metric("Incasso del Giorno", f"{st.session_state.euro_oggi} €")

    st.write("---")
    # GRAFICO SETTIMANALE
    st.subheader("📈 Andamento Produzione Latte")
    fig = px.line(st.session_state.storia_latte, x='Giorno', y='Litri', markers=True, color_discrete_sequence=['#2E7D32'])
    st.plotly_chart(fig, use_container_width=True)

elif scelta == "Cassa":
    st.title("🛒 Vendita Rapida")
    st.write("Tocca il prodotto per registrarne la vendita")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🥛 Vendi 1L Latte (1.50€)"):
            st.session_state.prodotti['Latte'] -= 1
            st.session_state.euro_oggi += 1.50
            st.toast("Latte venduto!")
    with col2:
        if st.button("🧀 Vendi 1 Caciocavallo (15€)"):
            st.session_state.prodotti['Caciocavallo'] -= 1
            st.session_state.euro_oggi += 15.0
            st.toast("Formaggio venduto!")

elif scelta == "JD-Link":
    st.title("🚜 Configurazione John Deere")
    st.info("Pausa: in attesa dell'autorizzazione del proprietario dell'account.")
    st.write("Quando tuo padre sarà disponibile, premeremo insieme il tasto 'Invia Richiesta' sul portale.")

# STALLA (Versione semplice per ora)
elif scelta == "Stalla": st.title("🐄 Registro Stalla")
