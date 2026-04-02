import streamlit as st
import pandas as pd

st.set_page_config(page_title="Torretta Pro", layout="wide")

# CSS - STILE
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background-color: white !important; border: 1px solid #e0e0e0 !important;
        padding: 12px 20px !important; border-radius: 12px !important;
        margin-bottom: 8px !important; display: flex !important; cursor: pointer !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important; color: white !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }
    .metric-card {
        background: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3em; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# INIZIALIZZAZIONE MEMORIA
if 'prodotti' not in st.session_state:
    st.session_state.prodotti = {"Latte": 0, "Caciocavallo": 0, "Ricotta": 0}
if 'latte_storico' not in st.session_state:
    st.session_state.latte_storico = 1240
if 'storico_vendite' not in st.session_state:
    st.session_state.storico_vendite = []
if 'n_m' not in st.session_state: st.session_state.n_m = 1
if 'n_v' not in st.session_state: st.session_state.n_v = 1
if 'n_t' not in st.session_state: st.session_state.n_t = 1

with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🛒 Cassa e Vendite"], label_visibility="collapsed")

# --- PAGINA DASHBOARD ---
if scelta == "📊 Dashboard":
    st.title("📊 Dashboard Operativa")
    
    # AZIONI RAPIDE
    st.subheader("⚡ Azioni Rapide")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🥛 REGISTRA PRODUZIONE LATTE"):
            nuovo_latte = st.number_input("Litri munti oggi", min_value=0)
            if st.button("Salva Latte"):
                st.session_state.latte_storico = nuovo_latte
                st.success("Produzione aggiornata!")
    with col_b:
        with st.expander("📦 CARICA PRODOTTI IN MAGAZZINO"):
            p_scelto = st.selectbox("Prodotto da caricare", list(st.session_state.prodotti.keys()))
            q_aggiunta = st.number_input("Quantità prodotta", min_value=0)
            if st.button("Aggiorna Scorte"):
                st.session_state.prodotti[p_scelto] += q_aggiunta
                st.success(f"Magazzino aggiornato: {p_scelto} ora a {st.session_state.prodotti[p_scelto]}")

    st.write("---")
    
    # METRICHE
    df_v = pd.DataFrame(st.session_state.storico_vendite)
    totale_incasso = df_v['Totale'].sum() if not df_v.empty else 0
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>{st.session_state.latte_storico} L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="metric-card"><h4>💰 INCASSO VENDITE</h4><h2>{totale_incasso:.2f} €</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><h4>📦 MAGAZZINO</h4>', unsafe_allow_html=True)
        for p, q in st.session_state.prodotti.items():
            st.write(f"**{p}:** {q}")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGINA REGISTRO STALLA ---
elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    t1, t2, t3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])
    # (Logica stalla v4.1...)
    with t1:
        for i in range(st.session_state.n_m):
            cd, cf = st.columns([2, 1])
            with cd:
                st.markdown('<div style="background:white;padding:15px;border-radius:10px;border-left:5px solid #1B5E20;margin-bottom:10px;">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Vacca {i}", key=f"mc_{i}")
                st.selectbox(f"Stato {i}", ["In Mungitura", "Asciutta"], key=f"ms_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with cf:
                f = st.file_uploader(f"Foto {i}", key=f"mf_{i}")
                if f: st.image(f, width=100)
        if st.button("➕ Aggiungi Capo"):
            st.session_state.n_m += 1
            st.rerun()

# --- PAGINA CASSA E VENDITE ---
elif scelta == "🛒 Cassa e Vendite":
    st.title("🛒 Cassa e Vendite")
    # ... (Codice cassa v5.0...)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("🛒 Nuova Vendita")
        with st.form("form_vendita"):
            prod = st.selectbox("Prodotto", list(st.session_state.prodotti.keys()))
            prezzo = st.number_input("Prezzo (€)", min_value=0.0, value=1.0)
            quant = st.number_input("Quantità", min_value=0.0, value=1.0)
            if st.form_submit_button("✅ Registra"):
                st.session_state.storico_vendite.append({"Prodotto": prod, "Totale": prezzo*quant})
                st.session_state.prodotti[prod] -= quant # Scarica dal magazzino
                st.success("Vendita registrata!")
