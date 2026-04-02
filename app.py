import streamlit as st
import pandas as pd

# 1. SETUP BASE
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. DATABASE FISSO (Non si cancella durante l'uso)
if 'magazzino' not in st.session_state:
    st.session_state.magazzino = {"Latte": 0.0, "Caciocavallo": 0.0, "Ricotta": 0.0}
if 'lista_vendite' not in st.session_state:
    st.session_state.lista_vendite = []
if 'produzione_latte' not in st.session_state:
    st.session_state.produzione_latte = 1240
if 'numero_capi' not in st.session_state:
    st.session_state.numero_capi = 1

# 3. MENU LATERALE
with st.sidebar:
    st.title("🛡️ TORRETTA PRO")
    menu = st.radio("VAI A:", ["DASHBOARD", "STALLA", "CASSA"])

# --- PAGINA DASHBOARD ---
if menu == "DASHBOARD":
    st.header("📊 Centro di Controllo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🥛 Latte Oggi")
        val_l = st.number_input("Litri munti:", value=st.session_state.produzione_latte)
        if st.button("Salva Produzione"):
            st.session_state.produzione_latte = val_l
            st.rerun()

    with col2:
        st.subheader("📦 Carico Magazzino")
        prodotto_da_caricare = st.selectbox("Scegli prodotto:", list(st.session_state.magazzino.keys()))
        quantita_da_aggiungere = st.number_input("Quantità aggiunta:", min_value=0.0)
        if st.button("Aggiorna Scorte"):
            st.session_state.magazzino[prodotto_da_caricare] += quantita_da_aggiungere
            st.rerun()

    with col3:
        st.subheader("✨ Nuovo Prodotto")
        nuovo_nome = st.text_input("Inserisci nome (es. Mozzarella):")
        if st.button("Aggiungi a Listino"):
            if nuovo_nome and nuovo_nome not in st.session_state.magazzino:
                st.session_state.magazzino[nuovo_nome] = 0.0
                st.success("Aggiunto!")
                st.rerun()

    st.write("---")
    
    # RIEPILOGO DATI
    st.subheader("📈 Riepilogo Attuale")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("LITRI LATTE", f"{st.session_state.produzione_latte} L")
    with m2:
        df_v = pd.DataFrame(st.session_state.lista_vendite)
        tot_soldi = df_v['Totale'].sum() if not df_v.empty else 0.0
        st.metric("INCASSO OGGI", f"{tot_soldi:.2f} €")
    with m3:
        st.write("**SCORTE IN MAGAZZINO:**")
        for k, v in st.session_state.magazzino.items():
            st.write(f"- {k}: {v}")

# --- PAGINA STALLA ---
elif menu == "STALLA":
    st.header("🐄 Registro Stalla")
    for i in range(st.session_state.numero_capi):
        with st.container():
            st.write(f"**Capo #{i+1}**")
            c_cod, c_stato = st.columns(2)
            with c_cod: st.text_input("Marca Auricolare", key=f"c_{i}")
            with c_stato: st.selectbox("Stato", ["In Mungitura", "Asciutta"], key=f"s_{i}")
    
    if st.button("➕ Aggiungi altro Capo"):
        st.session_state.numero_capi += 1
        st.rerun()

# --- PAGINA CASSA ---
elif menu == "CASSA":
    st.header("🛒 Cassa e Vendite")
    col_a, col_b = st.columns([1, 2])
    
    with col_a:
        st.subheader("Registra Vendita")
        v_prod = st.selectbox("Prodotto venduto:", list(st.session_state.magazzino.keys()))
        v_prezzo = st.number_input("Prezzo totale incassato (€):", min_value=0.0)
        v_quant = st.number_input("Quantità scalata dal magazzino:", min_value=0.0)
        if st.button("CONFERMA VENDITA"):
            st.session_state.lista_vendite.append({"Prodotto": v_prod, "Totale": v_prezzo})
            st.session_state.magazzino[v_prod] -= v_quant
            st.success("Vendita registrata!")
            st.rerun()

    with col_b:
        st.subheader("Storico di oggi")
        if st.session_state.lista_vendite:
            st.table(pd.DataFrame(st.session_state.lista_vendite))
            if st.button("Svuota Storico"):
                st.session_state.lista_vendite = []
                st.rerun()
