import streamlit as st
import pandas as pd

st.set_page_config(page_title="Torretta Pro", layout="wide")

# CSS - STILE MENU
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
        border-left: 5px solid #1B5E20; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("🛡️ TORRETTA PRO")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")

if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("🥛 LATTE OGGI: 1.240 L")
    with c2: st.success("💰 EURO OGGI: 450 €")
    with c3: st.warning("🌦️ PIOGGIA: 12 mm")
    
    col_l, col_e = st.columns(2)
    with col_l: st.bar_chart(pd.DataFrame({'Litri': [1200, 1250, 1180, 1300, 1280]}, index=['L','M','M','G','V']), color="#2E7D32")
    with col_e: st.bar_chart(pd.DataFrame({'Euro': [350, 410, 320, 500, 460]}, index=['L','M','M','G','V']), color="#FFA000")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla Fotografico")
    t1, t2, t3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])

    with t1:
        st.subheader("Capi in Mungitura")
        for i in range(1, 3):
            c_d, c_f = st.columns([2, 1])
            with c_d:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Vacca {i}", value=f"IT-M0{i}", key=f"m_{i}")
                st.selectbox(f"Stato {cod}", ["In Mungitura", "Asciutta"], key=f"sm_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with c_f:
                f = st.file_uploader(f"Foto {cod}", type=['jpg','png'], key=f"fm_{i}")
                if f: st.image(f, width=150)

    with t2:
        st.subheader("Vitelli")
        for i in range(1, 3):
            c_d, c_f = st.columns([2, 1])
            with c_d:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Vitello {i}", value=f"IT-V0{i}", key=f"v_{i}")
                st.selectbox(f"Stato {cod}", ["Da Segnare", "Da Vendere"], key=f"sv_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with c_f:
                f = st.file_uploader(f"Foto {cod}", type=['jpg','png'], key=f"fv_{i}")
                if f: st.image(f, width=150)

    with t3:
        st.subheader("Maschi Adulti")
        for i in range(1, 2):
            c_d, c_f = st.columns([2, 1])
            with c_d:
                st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                cod = st.text_input(f"Codice Toro {i}", value=f"IT-T0{i}", key=f"t_{i}")
                st.selectbox(f"Stato {cod}", ["Toro", "Da Vendere"], key=f"st_{i}")
                st.markdown('</div>', unsafe_allow_html=True)
            with c_f:
                f = st.file_uploader(f"Foto {cod}", type=['jpg','png'], key=f"ft_{i}")
                if f: st.image(f, width=150)

elif scelta == "🧀 Vendite":
    st.title("🧀 Cassa")
    st.number_input("Incasso totale (€)")
    st.button("Salva Vendita")

elif scelta == "🌦️ Meteo":
    st.components.v1.iframe("https://www.rainviewer.com/map.html?loc=41.46,15.54,8&isPlay=1&color=6", height=500)
