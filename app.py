import streamlit as st
import pandas as pd

# 1. CONFIGURAZIONE E DESIGN
st.set_page_config(page_title="Torretta Pro", layout="wide", page_icon="🐄")

# CSS per eliminare pallini e mettere i tasti verdi
st.markdown("""
<style>
    .stApp { background-color: #F4F7F6 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background-color: #ffffff !important; border: 1px solid #d1d5db !important;
        padding: 12px 20px !important; border-radius: 10px !important;
        margin-bottom: 8px !important; font-weight: bold !important; display: flex !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #2E7D32 !important; color: white !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }
    .card-verde {
        background: white; padding: 20px; border-radius: 15px;
        border-left: 8px solid #2E7D32; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 2. RESET AUTOMATICO PER EVITARE SCRITTE ROSSE
# Se cambiamo struttura, resettiamo la memoria per non andare in errore
if 'versione' not in st.session_state or st.session_state.versione != "11.0":
    st.session_state.clear()
    st.session_state.versione = "11.0"

# 3. INIZIALIZZAZIONE DATI
if 'prodotti' not in st.session_state:
    st.session_state.prodotti = {"Latte": "1240 L", "Caciocavallo": "0 pezzi", "Ricotta": "0 vaschette"}
if 'vendite' not in st.session_state: st.session_state.vendite = []
if 'capi_stalla' not in st.session_state: st.session_state.capi_stalla = []

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #2E7D32;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("NAV", ["📊 DASHBOARD", "🐄 REGISTRO STALLA", "🛒 CASSA VENDITE"], label_visibility="collapsed")
    st.write("---")
    if st.button("🗑️ Reset Totale App"):
        st.session_state.clear()
        st.rerun()

# --- DASHBOARD ---
if menu == "📊 DASHBOARD":
    st.title("📊 Riepilogo Aziendale")
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.subheader("📝 Segna Produzione")
        for p in list(st.session_state.prodotti.keys()):
            st.session_state.prodotti[p] = st.text_input(f"Quantità {p}:", value=st.session_state.prodotti[p])
        nuovo = st.text_input("✨ Nuovo Prodotto:")
        if st.button("Aggiungi"):
            if nuovo: st.session_state.prodotti[nuovo] = "0"; st.rerun()
    with c2:
        st.subheader("📋 Promemoria")
        for p, q in st.session_state.prodotti.items():
            st.markdown(f'<div class="card-verde"><small>PRODOTTO</small><br><b style="font-size:20px;">{p}</b><br><span style="font-size:24px; color:#2E7D32; font-weight:bold;">{q}</span></div>', unsafe_allow_html=True)

# --- STALLA (COMPLETA) ---
elif menu == "🐄 REGISTRO STALLA":
    st.title("🐄 Registro Animali")
    with st.expander("➕ AGGIUNGI CAPO (Vacca, Vitello o Maschio)", expanded=True):
        col_a, col_b, col_c = st.columns(3)
        auricolare = col_a.text_input("Codice Auricolare")
        categoria = col_b.selectbox("Categoria", ["Vacca", "Vitello", "Maschio/Toro", "Manza"])
        stato_animale = col_c.selectbox("Stato", ["In Mungitura", "Asciutta", "Svezzamento", "Ingrasso"])
        if st.button("Registra"):
            st.session_state.capi_stalla.append({"Codice": auricolare, "Tipo": categoria, "Stato": stato_animale})
            st.rerun()
    
    st.write("### 📋 Elenco Capi")
    if st.session_state.capi_stalla:
        st.table(pd.DataFrame(st.session_state.capi_stalla))
        if st.button("Elimina Ultimo Inserito"):
            st.session_state.capi_stalla.pop(); st.rerun()

# --- CASSA ---
elif menu == "🛒 CASSA VENDITE":
    st.title("🛒 Cassa")
    cx, cy = st.columns([1, 1.2])
    with cx:
        st.subheader("Nuova Vendita")
        with st.form("cassa_form"):
            prod_v = st.selectbox("Prodotto", list(st.session_state.prodotti.keys()))
            euro_v = st.number_input("Euro Incassati", min_value=0.0, step=0.5)
            note_v = st.text_input("Note (Cliente)")
            if st.form_submit_button("✅ SALVA"):
                st.session_state.vendite.append({"Prodotto": prod_v, "Euro": euro_v, "Note": note_v})
                st.rerun()
    with cy:
        st.subheader("Storico")
        if st.session_state.vendite:
            df_v = pd.DataFrame(st.session_state.vendite)
            st.table(df_v)
            st.metric("TOTALE", f"{df_v['Euro'].sum():.2f} €")
            if st.button("🗑️ Azzera Cassa"):
                st.session_state.vendite = []; st.rerun()
