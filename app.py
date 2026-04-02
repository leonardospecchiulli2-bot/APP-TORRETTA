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
    .cassa-box {
        background: #ffffff; padding: 20px; border-radius: 15px;
        border: 1px solid #e0e0e0; margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# INIZIALIZZAZIONE MEMORIA (DATABASE TEMPORANEO)
if 'prodotti' not in st.session_state:
    st.session_state.prodotti = ["Latte", "Caciocavallo", "Ricotta", "Formaggio Primo Sale"]
if 'storico_vendite' not in st.session_state:
    st.session_state.storico_vendite = []
if 'n_m' not in st.session_state: st.session_state.n_m = 1
if 'n_v' not in st.session_state: st.session_state.n_v = 1
if 'n_t' not in st.session_state: st.session_state.n_t = 1

with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Cassa e Vendite"], label_visibility="collapsed")

# --- PAGINA DASHBOARD ---
if scelta == "📊 Dashboard":
    st.title("📊 Analisi Aziendale")
    # Calcolo totali reali dalle vendite
    df_v = pd.DataFrame(st.session_state.storico_vendite)
    totale_incasso = df_v['Totale'].sum() if not df_v.empty else 0
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="metric-card"><h4>💰 INCASSO REALE</h4><h2>{totale_incasso:.2f} €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ METEO</h4><h2>Sereno</h2></div>', unsafe_allow_html=True)

    if not df_v.empty:
        st.write("---")
        st.subheader("🎯 Qual è il prodotto che rende di più?")
        # Raggruppa vendite per prodotto
        guadagni = df_v.groupby('Prodotto')['Totale'].sum().sort_values(ascending=False)
        st.bar_chart(guadagni, color="#1B5E20")
    else:
        st.info("Registra delle vendite in Cassa per vedere i grafici qui.")

# --- PAGINA REGISTRO STALLA ---
elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla")
    # ... (Codice della stalla della v4.1 rimane qui invariato)
    t1, t2, t3 = st.tabs(["🥛 Mungitura", "👶 Vitelli", "🐂 Maschi"])
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
        if st.button("➕ Aggiungi Capo (Mungitura)"):
            st.session_state.n_m += 1
            st.rerun()
    # (Vitelli e Maschi seguono la stessa logica...)

# --- PAGINA CASSA E VENDITE ---
elif scelta == "🧀 Cassa e Vendite":
    st.title("🧀 Cassa e Vendite")
    
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🛒 Nuova Vendita")
        with st.form("form_vendita"):
            prodotto = st.selectbox("Cosa stai vendendo?", st.session_state.prodotti)
            prezzo_un = st.number_input("Prezzo al kg/litro (€)", min_value=0.0, value=1.0)
            quantita = st.number_input("Quantità (kg o litri)", min_value=0.0, value=1.0)
            
            submit = st.form_submit_button("✅ Registra Vendita")
            if submit:
                tot = prezzo_un * quantita
                st.session_state.storico_vendite.append({
                    "Data": pd.Timestamp.now().strftime("%H:%M"),
                    "Prodotto": prodotto,
                    "Quantità": quantita,
                    "Totale": tot
                })
                st.success(f"Venduto {prodotto} per {tot:.2f} €")
        
        st.write("---")
        st.subheader("✨ Nuovo Prodotto?")
        nuovo_p = st.text_input("Nome Prodotto (es. Scamorza)")
        if st.button("➕ Aggiungi all'inventario"):
            if nuovo_p and nuovo_p not in st.session_state.prodotti:
                st.session_state.prodotti.append(nuovo_p)
                st.success(f"{nuovo_p} aggiunto!")
                st.rerun()

    with col2:
        st.subheader("📜 Storico Vendite Oggi")
        if st.session_state.storico_vendite:
            df_v = pd.DataFrame(st.session_state.storico_vendite)
            st.table(df_v)
            if st.button("🗑️ Cancella tutto lo storico"):
                st.session_state.storico_vendite = []
                st.rerun()
        else:
            st.info("Nessuna vendita registrata oggi.")
