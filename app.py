import streamlit as st
import pandas as pd

# 1. SETUP - Pulizia totale
st.set_page_config(page_title="TORRETTA PRO", layout="wide", page_icon="🐄")

# 2. DATABASE INTERNO (Si svuota solo se riavvii il server, ma resta fisso durante l'uso)
if 'db_prodotti' not in st.session_state:
    st.session_state.db_prodotti = {"Latte": 0.0, "Caciocavallo": 0.0, "Ricotta": 0.0}
if 'db_vendite' not in st.session_state: st.session_state.db_vendite = []
if 'lt_munti' not in st.session_state: st.session_state.lt_munti = 1240
if 'c_m' not in st.session_state: st.session_state.c_m = 1
if 'c_v' not in st.session_state: st.session_state.c_v = 1
if 'c_t' not in st.session_state: st.session_state.c_t = 1

# 3. CSS - ALTA VISIBILITÀ (Niente sovrapposizioni)
st.markdown("""
<style>
    .stApp { background-color: #F4F7F6 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Menu laterale leggibile */
    div[role="radiogroup"] > label {
        background: #FFFFFF !important; border: 2px solid #D1D5DB !important;
        padding: 15px !important; border-radius: 12px !important;
        margin-bottom: 10px !important; color: #111827 !important; font-weight: bold !important;
    }
    div[role="radiogroup"] > label:has(input:checked) {
        background: #059669 !important; color: white !important; border: 2px solid #047857 !important;
    }

    /* Card Dashboard */
    .card-top {
        background: white; padding: 20px; border-radius: 15px;
        border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center; margin-bottom: 15px;
    }
    .valore-grande { color: #065F46; font-size: 32px; font-weight: 800; }
    
    /* Pulizia icone sovrapposte */
    .stExpander { border: none !important; background: #FFFFFF !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='color: #065F46; text-align: center;'>🛡️ TORRETTA PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("MENU", ["📊 DASHBOARD", "🐄 STALLA", "🛒 CASSA"], label_visibility="collapsed")
    st.write("---")
    st.info("Log: Operatore Pronto")

# --- PAGINA DASHBOARD ---
if scelta == "📊 DASHBOARD":
    st.markdown("<h1 style='color: #111827;'>📊 Centro di Controllo</h1>", unsafe_allow_html=True)
    
    # AZIONI RAPIDE (Senza icone che si sovrappongono)
    st.markdown("### ⚡ Azioni Rapide")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.expander("🥛 REGISTRA LATTE"):
            n_lt = st.number_input("Litri totali", value=st.session_state.lt_munti)
            if st.button("AGGIORNA"):
                st.session_state.lt_munti = n_lt
                st.rerun()
    
    with c2:
        with st.expander("📦 CARICO MAGAZZINO"):
            p_sel = st.selectbox("Cosa hai prodotto?", list(st.session_state.db_prodotti.keys()))
            q_add = st.number_input("Quantità prodotta", min_value=0.0)
            if st.button("CARICA"):
                st.session_state.db_prodotti[p_sel] += q_add
                st.rerun()

    with c3:
        with st.expander("✨ NUOVO TIPO PRODOTTO"):
            n_p = st.text_input("Nome (es. Scamorza)")
            if st.button("AGGIUNGI A LISTINO"):
                if n_p and n_p not in st.session_state.db_prodotti:
                    st.session_state.db_prodotti[n_p] = 0.0
                    st.rerun()

    st.write("---")
    
    # INDICATORI FISSI
    df_v = pd.DataFrame(st.session_state.db_vendite)
    tot_inc = df_v['Totale'].sum() if not df_v.empty else 0.0
    
    i1, i2, i3 = st.columns(3)
    with i1:
        st.markdown(f'<div class="card-top"><b>PRODUZIONE LATTE</b><div class="valore-grande">{st.session_state.lt_munti} L</div>
