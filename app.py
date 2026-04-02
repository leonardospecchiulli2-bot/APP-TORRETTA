import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configurazione
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS - MENU E STILE (Aggiornato per rendere i moduli più belli)
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background-color: white !important; border: 1px solid #ddd !important;
        padding: 10px !important; border-radius: 10px !important; margin-bottom: 5px !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) { background-color: #1B5E20 !important; }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }
    
    .metric-card {
        background: white; padding: 15px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .form-container {
        background: white; padding: 30px; border-radius: 20px;
        border: 1px solid #eee; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.header("🛡️ TORRETTA PRO")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")

# 4. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 EURO OGGI</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    giorni = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
    col_l, col_e = st.columns(2)
    with col_l:
        st.subheader("🥛 Latte Settimanale")
        df_l = pd.DataFrame({'Litri': [1200, 1250, 1180, 1300, 1280, 1350, 1240]}, index=giorni)
        st.bar_chart(df_l, color="#2E7D32")
    with col_e:
        st.subheader("💰 Entrate Settimanali")
        df_e = pd.DataFrame({'Euro': [350, 410, 320, 500, 460, 620, 450]}, index=giorni)
        st.bar_chart(df_e, color="#FFA000")

elif scelta == "🐄 Stalla":
    st.title("🐄 Registro Mungitura")
    st.write(f"Data: **{datetime.now().strftime('%d/%m/%Y')}**")
    
    col_form, col_info = st.columns([2, 1])
    
    with col_form:
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        # Campi d'inserimento
        turno = st.selectbox("Seleziona Turno", ["Mattina", "Pomeriggio/Sera"])
        litri = st.number_input("Totale Litri Munti", min_value=0.0, step=0.1)
        capi = st.number_input("Numero Capi Munti", min_value=0, step=1)
        note = st.text_area("Note e Salute Animali", placeholder="Esempio: Vacca n.5 in asciutta, tutto ok...")
        
        if st.button("💾 SALVA REGISTRAZIONE"):
            # Per ora mostriamo solo un messaggio, poi lo collegheremo al database
            st.success(f"Registrazione {turno} salvata con successo!")
            st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_info:
        st.info("""
        **Consiglio del giorno:**
        Controlla sempre la temperatura del refrigeratore dopo la mungitura della mattina.
        """)
        st.metric("Media Litri/Capo", f"{round(litri/capi, 2) if capi > 0 else 0} L")

elif scelta == "🧀 Vendite":
    st.title("🧀 Punto Vendita")
    euro = st.number_input("Incasso", min_value=0.0)
    if st.button("Registra"):
        st.success(f"Registrati {euro} €")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Radar Meteo")
    url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isPlay=1&color=6"
    st.components.v1.iframe(url, height=500)
