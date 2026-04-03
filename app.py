import streamlit as st
import pandas as pd

# 1. SETUP E DESIGN
st.set_page_config(page_title="Torretta Pro", layout="wide", page_icon="🐄")

# CSS Avanzato per eliminare i pallini e ripristinare il design verde
st.markdown("""
<style>
    .stApp { background-color: #F4F7F6 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Pulsanti Menu Quadrati e Verdi */
    div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
        padding: 12px 20px !important;
        border-radius: 10px !important;
        margin-bottom: 8px !important;
        font-weight: bold !important;
        color: #374151 !important;
        display: flex !important;
    }
    /* Nasconde il pallino radio */
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    
    /* Pulsante selezionato */
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #2E7D32 !important;
        color: white !important;
        border: 1px solid #1B5E20 !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }

    /* Card della Dashboard */
    .card-verde {
        background: white; padding: 20px; border-radius: 15px;
        border-left: 8px solid #2E7D32; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 2. GESTIONE DATI (State)
if 'prodotti' not in st.session_state:
    st.session_state.prodotti = {"Latte": "1240 L", "Caciocavallo": "0 pezzi", "Ricotta": "0 vaschette"}
if 'vendite' not in st.session_state: st.session_state.vendite = []
if 'capi' not in st.session_state: st.session_state.capi = []

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #2E7D32;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("Scegli Pagina:", ["📊 DASHBOARD", "🐄 REGISTRO STALLA", "🛒 CASSA VENDITE"], label_visibility="collapsed")
    st.write("---")
    st.info("Sistema Online")

# --- PAGINA 1: DASHBOARD (Card Verdi) ---
if menu == "📊 DASHBOARD":
    st.title("📊 Riepilogo Aziendale")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("📝 Aggiorna Scorte")
        for p in list(st.session_state.prodotti.keys()):
            st.session_state.prodotti[p] = st.text_input(f"Quantità {p}:", value=st.session_state.prodotti[p])
        
        nuovo = st.text_input("✨ Aggiungi Prodotto:")
        if st.button("Aggiungi"):
            if nuovo: st.session_state.prodotti[nuovo] = "0"; st.rerun()

    with col2:
        st.subheader("📋 Promemoria Visivo")
        for p, q in st.session_state.prodotti.items():
            st.markdown(f"""
            <div class="card-verde">
                <small style='color: #666;'>PRODOTTO</small><br>
                <b style='font-size: 22px;'>{p}</b><br>
                <span style='font-size: 28px; color: #2E7D32; font-weight: bold;'>{q}</span>
            </div>
            """, unsafe_allow_html=True)

# --- PAGINA 2: STALLA (Ripristinata Completa) ---
elif menu == "🐄 REGISTRO STALLA":
    st.title("🐄 Registro Animali")
    
    with st.expander("➕ AGGIUNGI NUOVO CAPO", expanded=True):
        c1, c2, c3 = st.columns(3)
        cod = c1.text_input("Codice Auricolare")
        tipo = c2.selectbox("Categoria", ["Vacca", "Vitello", "Torello/Maschio", "Manza"])
        stato = c3.selectbox("Stato", ["In Mungitura", "Asciutta", "Svezzamento", "Ingrasso"])
        if st.button("Registra Capo"):
            st.session_state.capi.append({"Codice": cod, "Tipo": tipo, "Stato": stato})
            st.rerun()

    st.write("### 📋 Elenco Capi in Stalla")
    if st.session_state.capi:
        df_capi = pd.DataFrame(st.session_state.capi)
        st.table(df_capi)
        if st.button("Elimina Ultimo"):
            st.session_state.capi.pop(); st.rerun()
    else:
        st.write("Nessun animale registrato.")

# --- PAGINA 3: CASSA (Funzionale) ---
elif menu == "🛒 CASSA VENDITE":
    st.title("🛒 Cassa e Vendite")
    
    col_a, col_b = st.columns([1, 1.2])
    
    with col_a:
        st.subheader("Nuova Vendita")
        with st.form("cassa_f"):
            p_sel = st.selectbox("Cosa vendi?", list(st.session_state.prodotti.keys()))
            prezzo = st.number_input("Incasso Totale (€)", min_value=0.0, step=0.50)
            note_v = st.text_input("Note vendita (es. Cliente Rossi)")
            if st.form_submit_button("✅ SALVA VENDITA"):
                st.session_state.vendite.append({"Prodotto": p_sel, "Euro": prezzo, "Note": note_v})
                st.rerun()

    with col_b:
        st.subheader("Storico Giornaliero")
        if st.session_state.vendite:
            df_v = pd.DataFrame(st.session_state.vendite)
            st.table(df_v)
            st.metric("TOTALE INCASSATO", f"{df_v['Euro'].sum():.2f} €")
            if st.button("🗑️ Svuota Cassa"):
                st.session_state.vendite = []; st.rerun()
