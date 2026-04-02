
import streamlit as st

# 1. Configurazione Pagina
st.set_page_config(page_title="Torretta Pro", page_icon="🛡️", layout="wide")

# 2. CSS Avanzato per Menù Professionale e Dashboard
st.markdown("""
<style>
    /* Sfondo e font generale */
    .stApp { background-color: #FDFCF5; }
    
    /* NASCONDI I PALLINI DEL MENU */
    [data-testid="stSidebarNav"] {display: none;}
    div.row-widget.stRadio > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {
        font-size: 18px !important;
        font-weight: 600 !important;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label [data-testid="stWidgetLabel"] { display: none; }
    
    /* TRASFORMA RADIO IN BOTTONI NEL MENU */
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: white;
        padding: 12px 20px !important;
        border-radius: 12px !important;
        border: 1px solid #E0E0E0 !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease !important;
    }
    
    /* NASCONDE IL CERCHIETTO FISICO */
    div.row-widget.stRadio > div[role="radiogroup"] > label div:first-child { display: none !important; }

    /* EFFETTO SELEZIONE VERDE */
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important;
    }
    
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) p {
        color: white !important;
    }

    /* CARD DASHBOARD */
    .metric-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border-top: 6px solid #1B5E20;
        box-shadow: 0 6px 12px rgba(0,0,0,0.05);
        text-align: center;
    }

    /* BOTTONI AZIONI RAPIDE */
    .stButton>button {
        height: 90px;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 15px;
        background-color: #2E7D32 !important;
        color: white !important;
        border: none;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar con Menu a Rettangoli
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20;'>🛡️ Torretta Pro</h2>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("SISTEMA", ["📊 Dashboard", "🐄 Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")
    st.write("---")
    st.caption("Operatore: Leonardo")

# 4. Logica Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Riepilogo Operativo")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="metric-card"><h4>🥛 Latte</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 Vendite</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ Pioggia</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)

    st.write("##")
    st.markdown("### ⚡ Azioni Rapide")
    b1, b2, b3 = st.columns(3)
    with b1: 
        if st.button("➕\nLATTE"): st.toast("Caricamento Stalla...")
    with b2: 
        if st.button("🛒\nCASSA"): st.toast("Caricamento Vendite...")
    with b3: 
        if st.button("📡\nRADAR"): st.toast("Caricamento Meteo...")

elif scelta == "🐄 Stalla":
    st.title("🐄 Registro Stalla")
    st.number
