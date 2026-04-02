import streamlit as st

# 1. SETUP
st.set_page_config(page_title="Torretta Promemoria", layout="wide")

# 2. MEMORIA (Bigliettini segnati)
if 'note_produzione' not in st.session_state:
    st.session_state.note_produzione = {"Latte": "1240 L", "Caciocavallo": "0 pezzi", "Ricotta": "0 vaschette"}
if 'lista_capi' not in st.session_state:
    st.session_state.lista_capi = 1

# 3. INTERFACCIA
st.title("🛡️ Torretta: Gestione Semplice")

menu = st.sidebar.radio("Vai a:", ["📝 PROMEMORIA PRODUZIONE", "🐄 REGISTRO STALLA"])

# --- PAGINA PROMEMORIA ---
if menu == "📝 PROMEMORIA PRODUZIONE":
    st.header("📝 Appunti di Produzione")
    st.info("Qui puoi scrivere a mano le quantità prodotte oggi per ricordartele.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✍️ Modifica Note")
        for prodotto in list(st.session_state.note_produzione.keys()):
            # Creiamo un campo di testo per ogni prodotto
            nuova_nota = st.text_input(f"Quantità per {prodotto}:", value=st.session_state.note_produzione[prodotto])
            st.session_state.note_produzione[prodotto] = nuova_nota
            
        st.write("---")
        nuovo_p = st.text_input("✨ Aggiungi nuovo tipo (es. Mozzarella):")
        if st.button("Aggiungi alla lista"):
            if nuovo_p:
                st.session_state.note_produzione[nuovo_p] = "0"
                st.rerun()

    with col2:
        st.subheader("📋 Riepilogo da Ricordare")
        st.markdown("---")
        for p, n in st.session_state.note_produzione.items():
            st.markdown(f"### {p}: **{n}**")
        st.markdown("---")
        if st.button("🗑️ Cancella tutto e ricomincia"):
            st.session_state.note_produzione = {"Latte": "0", "Caciocavallo": "0", "Ricotta": "0"}
            st.rerun()

# --- PAGINA STALLA ---
elif menu == "🐄 REGISTRO STALLA":
    st.header("🐄 Registro Capi")
    for i in range(st.session_state.lista_capi):
        with st.container():
            c1, c2 = st.columns(2)
            with c1: st.text_input(f"Marca Capo {i+1}", key=f"capo_{i}")
            with c2: st.selectbox("Stato", ["In produzione", "Asciutta", "Vitello"], key=f"stato_{i}")
            st.write("---")
    
    if st.button("➕ Aggiungi riga"):
        st.session_state.lista_capi += 1
        st.rerun()
