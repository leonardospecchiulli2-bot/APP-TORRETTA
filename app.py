import streamlit as st
import pandas as pd

# 1. Configurazione
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS - STILE (Sempre pulito)
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
    # (Codice Dashboard - quello che funzionava)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div style="background:white;padding:20px;border-radius:15px;text-align:center;border-top:5px solid #1B5E20;"><h4>🥛 LATTE</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div style="background:white;padding:20px;border-radius:15px;text-align:center;border-top:5px solid #1B5E20;"><h4>💰 EURO</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div style="background:white;padding:20px;border-radius:15px;text-align:center;border-top:5px solid #1B5E20;"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla Fotografico")
    
    tab1, tab2, tab3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])

    def mostra_registro(categoria):
        st.subheader(f"Elenco {categoria}")
        # Creiamo 3 righe di esempio per ogni categoria
        for i in range(1, 4):
            with st.container():
                col_dati, col_foto = st.columns([2, 1])
                with col_dati:
                    st.markdown(f'<div class="capo-box">', unsafe_allow_html=True)
                    codice = st.text_input(f"Codice Capo {i}", value=f"IT00{i}", key=f"cod_{categoria}_{i}")
                    stato = st.selectbox(f"Stato", ["In Stalla", "In Mungitura", "Asciutta"], key=f"stat_{categoria}_{i}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with col_foto:
                    img = st.file_uploader(f"Foto Capo {codice}", type=['jpg','png','jpeg'], key=f"img_{categoria}_{i}")
                    if img:
                        st.image(img, width=150, caption="Miniatura (clicca per ingrandire)")
                st.write("---")

    with tab1: mostra_registro("Mungitura")
    with tab2: mostra_registro("Vitelli")
    with tab3: mostra_registro("Maschi")

elif scelta == "🧀 Vendite":
    st.title("🧀 Punto Vendita")
    st.number_input("Incasso (€)")
    st.button("Registra")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Radar")
    st.components.v1.iframe("https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isPlay=1&color=6", height=500)
