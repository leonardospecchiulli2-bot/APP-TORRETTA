import streamlit as st
import pandas as pd

# 1. Configurazione
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS - STILE
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

# 3. Sidebar
with st.sidebar:
    st.header("🛡️ TORRETTA PRO")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div style="background:white;padding:20px;border-radius:15px;text-align:center;border-top:5px solid #1B5E20;"><h4>🥛 LATTE</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div style="background:white;padding:20px;border-radius:15px;text-align:center;border-top:5px solid #1B5E20;"><h4>💰 EURO</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div style="background:white;padding:20px;border-radius:15px;text-align:center;border-top:5px solid #1B5E20;"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla Selettivo")
    tab1, tab2, tab3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])

    # Funzione per generare i box con opzioni diverse
    def crea_box_capo(cat_nome, opzioni, prefisso_cod):
        st.subheader(f"Elenco {cat_nome}")
        for i in range(1, 4):
            with st.container():
                c_dati, c_foto = st.columns([2, 1])
                with c_dati:
                    st.markdown('<div class="capo-box">', unsafe_allow_html=True)
                    cod = st.text_input(f"Codice", value=f"{prefisso_cod}{i}", key=f"c_{cat_nome}_{i}")
                    stato = st.selectbox(f"Destinazione/Stato", opzioni, key=f"s_{cat_nome}_{i}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with c_foto:
                    f = st.file_uploader(f"Foto {cod}", type=['jpg','png','jpeg'], key=f"f_{cat_nome}_{i}")
                    if f: st.image(f, width=150)
                st.write("---")

    with tab1:
        crea_box_capo("Mungitura", ["
