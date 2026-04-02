import streamlit as st
import pandas as pd

# 1. Configurazione
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS - MENU E STILE
st.markdown("""
<style>
    .stApp { background-color: #FDFCF5 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background-color: white !important; border: 1px solid #ddd !important;
        padding: 12px !important; border-radius: 12px !important; margin-bottom: 8px !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) { background-color: #1B5E20 !important; }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }
    .metric-card {
        background: white; padding: 15px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stButton > button {
        width: 100% !important; background-color: white !important; 
        color: #1B5E20 !important; border: 2px solid #1B5E20 !important; border-radius: 10px !important;
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
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 EURO</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)
    
    st.write("##")
    # GRAFICI SEPARATI
    col_l, col_e = st.columns(2)
    giorni = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
    
    with col_l:
        st.subheader("🥛 Latte Settimanale")
        df1 = pd.DataFrame({'Litri': [1200, 1250, 1180, 1300, 1280, 1350, 1240]}, index=giorni)
        st.bar_chart(df1, color="#2E7D32")
        
    with col_e:
        st.subheader("💰 Entrate Settimanali")
        df2 = pd.DataFrame({'Euro': [350, 410, 320, 500, 460, 620, 450]}, index=giorni)
        st.bar_chart(df2, color="#FFA000")

elif scelta == "🐄 Stalla":
    st.title("🐄 Registro Stalla")
    st.number_input("Litri", min_value=0.0)
    st.button("SALVA")

elif scelta == "🧀 Vendite":
