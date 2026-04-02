import streamlit as st
import pandas as pd

# CONFIGURAZIONE BASE
st.set_page_config(page_title="TORRETTA PRO", layout="wide")

# INIZIALIZZAZIONE DATI (Database interno)
if 'prodotti' not in st.session_state:
    st.session_state.prodotti = {"Latte": 0.0, "Caciocavallo": 0.0, "Ricotta": 0.0}
if 'vendite' not in st.session_state: st.session_state.vendite = []
if 'litri' not in st.session_state: st.session_state.litri = 1240
if 'm' not in st.session_state: st.session_state.m = 1

# CSS SEMPLICE E PULITO (Per leggere bene tutto)
st.markdown("""
<style>
    .stApp { background-color: #F4F7F6; }
    [data-testid="stSidebarNav"] {display: none;}
    .css-17l6sh2 {border: 1px solid #ddd; padding: 20px; border-radius: 10px; background: white;}
    .big-font { font-size:25px !important; font-weight: bold; color: #065F46; }
</style>
""", unsafe_allow_html=True)

# MENU LATERALE
with st.sidebar:
    st.title("🛡️ TORRETTA PRO")
    scelta = st.radio("Scegli Pagina:", ["📊 DASHBOARD", "🐄 STALLA", "🛒 CASSA"])

# --- DASHBOARD ---
if scelta == "📊 DASHBOARD":
    st.header("📊 Centro di Controllo")
    
    # AZIONI RAPIDE
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🥛 Latte")
        nuovo_l = st.number_input("Litri oggi:", value=st.session_state.litri)
        if st.button("Salva Litri"):
            st.session_state.litri = nuovo_l
            st.rerun()

    with col2:
        st.subheader("📦 Magazzino")
        p_sel = st.selectbox("Cosa hai prodotto?", list(st.session_state.prodotti.keys()))
        q_add = st.number_input("Quantità da aggiungere:", min_value=0.0)
        if st.button("Carica scorte"):
            st.session_state.prodotti[p_sel] += q_add
            st.rerun()

    with col3:
        st.subheader("✨ Nuovo Prodotto")
        nuovo_p = st.text_input("Nome nuovo (es. Mozzarella):")
        if st.button("Aggiungi a Listino"):
            if nuovo_p and nuovo_p not in st.session_state.prodotti:
                st.session_state.prodotti[nuovo_p] = 0.0
                st.success("Aggiunto!")
                st.rerun()

    st.divider()

    # RIEPILOGO VISIBILE
    m1, m2, m3 = st.columns(3)
    with m1:
        st.write("🥛 **PRODUZIONE LATTE**")
        st.markdown(f"<p class='big-font'>{st.session_state.litri} L</p>", unsafe_allow_html=True)
    with m2:
        df_v = pd.DataFrame(st.session_state.vendite)
        incasso = df_v['Totale'].sum() if not df_v.empty else 0.0
        st.write("💰 **INCASSO OGGI**")
        st.markdown(f"<p class='big-font'>{incasso:.2f} €</p>", unsafe_allow_html=True)
    with m3:
        st.write("📦 **SCORTE ATTUALI**")
        for p, q in st.session_state.prodotti.items():
            st.write(f"**{p}**: {q}")

# --- STALLA ---
elif scelta == "🐄 STALLA":
    st.header("🐄 Registro Stalla")
    for i in range(st.session_state.m):
        with st.container():
            c_a, c_b = st.columns(2)
            with c_a: st.text_input(f"Codice Capo {i+1}", key=f"cod_{i}")
            with c_b: st.selectbox("Stato", ["In mungitura", "Asciutta"], key=f"st_{i}")
    if st.button("➕ Aggiungi Capo"):
        st.session_state.m += 1
        st.rerun()

# --- CASSA ---
elif scelta == "🛒 CASSA":
    st.header("🛒 Cassa e Vendite")
    col_c, col_s = st.columns([1, 2])
    
    with col_c:
        with st.form("vendita"):
            prod = st.selectbox("Prodotto", list(st.session_state.prodotti.keys()))
            prezzo = st.number_input("Prezzo (€)", min_value=0.0)
            quant = st.number_input("Quantità", min_value=0.0)
            if st.form_submit_button("REGISTRA VENDITA"):
                st.session_state.vendite.append({"Prodotto": prod, "Totale": prezzo * quant})
                st.session_state.prodotti[prod] -= quant
                st.rerun()

    with col_s:
        if st.session_state.vendite:
            st.table(pd.DataFrame(st.session_state.vendite))
            if st.button("Svuota Giornata"):
                st.session_state.vendite = []
                st.rerun()
