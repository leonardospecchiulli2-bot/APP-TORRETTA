import streamlit as st
import pandas as pd

# 1. SETUP INIZIALE
st.set_page_config(page_title="Torretta Pro v5.3", layout="wide")

# 2. INIZIALIZZAZIONE MEMORIA (Nomi nuovi per evitare AttributeError)
if 'stalla_m' not in st.session_state: st.session_state.stalla_m = 1
if 'stalla_v' not in st.session_state: st.session_state.stalla_v = 1
if 'stalla_t' not in st.session_state: st.session_state.stalla_t = 1
if 'latte_record' not in st.session_state: st.session_state.latte_record = 1240
if 'inv_prodotti' not in st.session_state: 
    st.session_state.inv_prodotti = {"Latte": 0, "Caciocavallo": 0, "Ricotta": 0}
if 'cassa_oggi' not in st.session_state: st.session_state.cassa_oggi = []

# 3. CSS - DESIGN PULITO
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
    .box-pro {
        background: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .box-capo {
        background: white; padding: 15px; border-radius: 12px;
        border-left: 6px solid #1B5E20; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 4. MENU LATERALE
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🛒 Cassa e Vendite"], label_visibility="collapsed")
    st.write("---")
    st.caption("v5.3 - Gestione Aziendale")

# --- PAGINA DASHBOARD ---
if menu == "📊 Dashboard":
    st.title("📊 Dashboard Operativa")
    
    # AZIONI RAPIDE
    st.subheader("⚡ Azioni Rapide")
    c_latte, c_mag = st.columns(2)
    
    with c_latte:
        with st.expander("🥛 REGISTRA PRODUZIONE LATTE"):
            val = st.number_input("Litri di oggi", min_value=0, value=st.session_state.latte_record)
            if st.button("Salva Produzione"):
                st.session_state.latte_record = val
                st.success("Dato aggiornato!")

    with c_mag:
        with st.expander("📦 CARICA PRODOTTI IN MAGAZZINO"):
            p_n = st.selectbox("Cosa hai prodotto?", list(st.session_state.inv_prodotti.keys()))
            p_q = st.number_input("Quantità aggiunta", min_value=0)
            if st.button("Aggiorna Magazzino"):
                st.session_state.inv_prodotti[p_n] += p_q
                st.rerun()

    st.write("---")
    
    # METRICHE IN EVIDENZA
    df_cassa = pd.DataFrame(st.session_state.cassa_oggi)
    tot_soldi = df_cassa['Totale'].sum() if not df_cassa.empty else 0
    
    m1, m2, m3 = st.columns(3)
    with m1: st.markdown(f'<div class="box-pro"><h4>🥛 LATTE OGGI</h4><h2>{st.session_state.latte_record} L</h2></div>', unsafe_allow_html=True)
    with m2: st.markdown(f'<div class="box-pro"><h4>💰 INCASSO</h4><h2>{tot_soldi:.2f} €</h2></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="box-pro"><h4>📦 MAGAZZINO</h4>', unsafe_allow_html=True)
        for k, v in st.session_state.inv_prodotti.items():
            st.write(f"**{k}:** {v}")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGINA REGISTRO STALLA ---
elif menu == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    t1, t2, t3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])

    with t1:
        for i in range(st.session_state.stalla_m):
            col_d, col_f = st.columns([2, 1])
            with col_d:
                st.markdown('<div class="box-capo">', unsafe_allow_html=True)
                st.text_input("Codice", key=f"m_c_{i}", placeholder="Marca Auricolare")
                st.selectbox("Stato", ["In Mungitura", "Asciutta"], key=f"m_s_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with col_f:
                f = st.file_uploader("Foto", key=f"m_f_{i}")
                if f: st.image(f, width=120)
        if st.button("➕ Aggiungi Capo (Mungitura)"):
            st.session_state.stalla_m += 1
            st.rerun()

    with t2:
        for i in range(st.session_state.stalla_v):
            col_d, col_f = st.columns([2, 1])
            with col_d:
                st.markdown('<div class="box-capo">', unsafe_allow_html=True)
                st.text_input("Codice", key=f"v_c_{i}", placeholder="Marca Auricolare")
                st.selectbox("Stato", ["Sotto Madre", "Svezzato"], key=f"v_s_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with col_f:
                f = st.file_uploader("Foto", key=f"v_f_{i}")
                if f: st.image(f, width=120)
        if st.button("➕ Aggiungi Capo (Vitelli)"):
            st.session_state.stalla_v += 1
            st.rerun()

    with t3:
        for i in range(st.session_state.stalla_t):
            col_d, col_f = st.columns([2, 1])
            with col_d:
                st.markdown('<div class="box-capo">', unsafe_allow_html=True)
                st.text_input("Codice", key=f"t_c_{i}", placeholder="Marca Auricolare")
                st.selectbox("Stato", ["Toro", "Ingrasso"], key=f"t_s_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with col_f:
                f = st.file_uploader("Foto", key=f"t_f_{i}")
                if f: st.image(f, width=120)
        if st.button("➕ Aggiungi Capo (Maschi)"):
            st.session_state.stalla_t += 1
            st.rerun()

# --- PAGINA CASSA ---
elif menu == "🛒 Cassa e Vendite":
    st.title("🛒 Cassa e Vendite")
    cl1, cl2 = st.columns([1, 2])
    
    with cl1:
        st.subheader("🛒 Nuova Vendita")
        with st.form("vendita_rapida"):
            p_selezionato = st.selectbox("Prodotto", list(st.session_state.inv_prodotti.keys()))
            p_prezzo = st.number_input("Prezzo unitario (€)", min_value=0.0, step=0.1)
            p_quantita = st.number_input("Quantità", min_value=0.0, step=0.1)
            if st.form_submit_button("Registra Vendita"):
                tot = p_prezzo * p_quantita
                st.session_state.cassa_oggi.append({"Prodotto": p_selezionato, "Totale": tot})
                st.session_state.inv_prodotti[p_selezionato] -= p_quantita
                st.success(f"Venduto {p_selezionato}!")
                st.rerun()
        
        st.write("---")
        nuovo_p = st.text_input("Aggiungi Prodotto a Listino")
        if st.button("Crea Prodotto"):
            if nuovo_p and nuovo_p not in st.session_state.inv_prodotti:
                st.session_state.inv_prodotti[nuovo_p] = 0
                st.rerun()

    with cl2:
        st.subheader("📜 Storico di Oggi")
        if st.session_state.cassa_oggi:
            st.table(pd.DataFrame(st.session_state.cassa_oggi))
            if st.button("Cancella Storico"):
                st.session_state.cassa_oggi = []
                st.rerun()
        else:
            st.info("Inizia a vendere per vedere qui lo storico.")
