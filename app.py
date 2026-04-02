import streamlit as st
import pandas as pd

st.set_page_config(page_title="Torretta Pro", layout="wide")

# CSS - DASHBOARD E STILE SENZA PALLINI
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
    .capo-box {
        background: white; padding: 20px; border-radius: 15px;
        border-left: 8px solid #1B5E20; margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-card {
        background: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Memoria per i capi
if 'n_m' not in st.session_state: st.session_state.n_m = 1
if 'n_v' not in st.session_state: st.session_state.n_v = 1
if 'n_t' not in st.session_state: st.session_state.n_t = 1

with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Vendite"], label_visibility="collapsed")

if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 EURO OGGI</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ METEO</h4><h2>Sereno</h2></div>', unsafe_allow_html=True)
    
    st.write("##")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.subheader("🥛 Produzione Latte")
        st.bar_chart([1200, 1250, 1180, 1300, 1280], color="#2E7D32")
    with col_g2:
        st.subheader("💰 Incasso Vendite")
        st.bar_chart([350, 410, 320, 500, 460], color="#FFA000")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    t1, t2, t3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])

    with t1:
        for i in range(st.session_state.n_m):
            cd, cf = st.columns([2, 1])
            with cd:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Vacca {i}", key=f"mc_{i}", placeholder="Marca Auricolare")
                st.selectbox(f"Stato {i}", ["In Mungitura", "Asciutta"], key=f"ms_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with cf:
                f = st.file_uploader(f"Foto {i}", key=f"mf_{i}")
                if f: st.image(f, width=150)
        if st.button("➕ Aggiungi Capo (Mungitura)"):
            st.session_state.n_m += 1
            st.rerun()

    with t2:
        for i in range(st.session_state.n_v):
            cd, cf = st.columns([2, 1])
            with cd:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Vitello {i}", key=f"vc_{i}", placeholder="Marca Auricolare")
                st.selectbox(f"Stato {i}", ["Da Segnare", "Da Vendere"], key=f"vs_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with cf:
                f = st.file_uploader(f"Foto {i}", key=f"vf_{i}")
                if f: st.image(f, width=150)
        if st.button("➕ Aggiungi Capo (Vitelli)"):
            st.session_state.n_v += 1
            st.rerun()

    with t3:
        for i in range(st.session_state.n_t):
            cd, cf = st.columns([2, 1])
            with cd:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Toro {i}", key=f"tc_{i}", placeholder="Marca Auricolare")
                st.selectbox(f"Stato {i}", ["Toro", "Da Vendere"], key=f"ts_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with cf:
                f = st.file_uploader(f"Foto {i}", key=f"tf_{i}")
                if f: st.image(f, width=150)
        if st.button("➕ Aggiungi Capo (Maschi)"):
            st.session_state.n_t += 1
            st.rerun()

elif scelta == "🧀 Vendite":
    st.title("🧀 Gestione Vendite")
    st.number_input("Incasso totale €", min_value=0.0)
    st.button("Registra Vendita")
