import streamlit as st
import pandas as pd

st.set_page_config(page_title="Torretta Pro", layout="wide")

# CSS - STILE
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background-color: white !important; border: 1px solid #ddd !important;
        padding: 10px !important; border-radius: 10px !important; margin-bottom: 5px !important;
    }
    div[role="radiogroup"] > label:has(input:checked) { background-color: #1B5E20 !important; }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }
    .capo-box {
        background: white; padding: 15px; border-radius: 15px;
        border-left: 5px solid #1B5E20; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Gestione dello stato per aggiungere capi dinamicamente
if 'count_m' not in st.session_state: st.session_state.count_m = 1
if 'count_v' not in st.session_state: st.session_state.count_v = 1
if 'count_t' not in st.session_state: st.session_state.count_t = 1

with st.sidebar:
    st.header("🛡️ TORRETTA PRO")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")

if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("🥛 LATTE OGGI: 1.240 L")
    with c2: st.success("💰 EURO OGGI: 450 €")
    with c3: st.warning("🌦️ PIOGGIA: 12 mm")
    st.write("---")
    col_l, col_e = st.columns(2)
    with col_l: st.bar_chart(pd.DataFrame({'Litri': [1200, 1250, 1180, 1300, 1280]}, index=['L','M','M','G','V']), color="#2E7D32")
    with col_e: st.bar_chart(pd.DataFrame({'Euro': [350, 410, 320, 500, 460]}, index=['L','M','M','G','V']), color="#FFA000")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    t1, t2, t3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])

    with t1:
        st.subheader("Capi in Mungitura")
        for i in range(st.session_state.count_m):
            c_d, c_f = st.columns([2, 1])
            with c_d:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Vacca", key=f"m_cod_{i}", placeholder="Inserisci Marca Auricolare")
                st.selectbox(f"Stato", ["In Mungitura", "Asciutta"], key=f"m_stat_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with c_f:
                f = st.file_uploader(f"Foto {cod}", type=['jpg','png'], key=f"m_foto_{i}")
                if f: st.image(f, width=150)
        if st.button("➕ Aggiungi Capo (Mungitura)"):
            st.session_state.count_m += 1
            st.rerun()

    with t2:
        st.subheader("Vitelli")
        for i in range(st.session_state.count_v):
            c_d, c_f = st.columns([2, 1])
            with c_d:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Vitello", key=f"v_cod_{i}", placeholder="Inserisci Marca Auricolare")
                st.selectbox(f"Stato", ["Da Segnare", "Da Vendere"], key=f"v_stat_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with c_f:
                f = st.file_uploader(f"Foto {cod}", type=['jpg','png'], key=f"v_foto_{i}")
                if f: st.image(f, width=150)
        if st.button("➕ Aggiungi Capo (Vitelli)"):
            st.session_state.count_v += 1
            st.rerun()

    with t3:
        st.subheader("Maschi Adulti")
        for i in range(st.session_state.count_t):
            c_d, c_f = st.columns([2, 1])
            with c_d:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Toro", key=f"t_cod_{i}", placeholder="Inserisci Marca Auricolare")
                st.selectbox(f"Stato", ["Toro", "Da Vendere"], key=f"t_stat_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with c_f:
                f = st.file_uploader(f"Foto {cod}", type=['jpg','png'], key=f"t_foto_{i}")
                if f: st.image(f, width=150)
        if st.button("➕ Aggiungi Capo (Maschi)"):
            st.session_state.count_t += 1
            st.rerun()

elif scelta == "🧀 Vendite":
    st.title("🧀 Cassa")
    st.number_input("Incasso totale (€)")
    st.button("Salva Vendita")

elif scelta == "🌦️ Meteo":
    st.components.v1.iframe("https://www.rainviewer.com/map.html?loc=41.46,15.54,8&isPlay=1&color=6", height=500)
