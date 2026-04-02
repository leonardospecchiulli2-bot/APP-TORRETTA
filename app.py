import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configurazione
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS - STILE (Pulito, senza pallini)
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
    .metric-card {
        background: white; padding: 15px; border-radius: 15px;
        border-top: 5px solid #1B5E20; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stTabs [aria-selected="true"] { background-color: #1B5E20 !important; color: white !important; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.header("🛡️ TORRETTA PRO")
    scelta = st.radio("NAV", ["📊 Dashboard", "🐄 Registro Stalla", "🧀 Vendite", "🌦️ Meteo"], label_visibility="collapsed")
    st.write("---")
    st.caption("Leonardo | v3.0")

# 4. Logica Database Fotografico (Simulata)
# Usiamo un dizionario di dizionari per simulare il caricamento riga per riga.
# In una versione reale, questi verrebbero caricati/salvati in un database vero.
if 'db_foto' not in st.session_state:
    st.session_state.db_foto = {
        'mungitura': pd.DataFrame([
            {"Codice": "IT001", "Sesso": "Femmina", "Stato": "In Mungitura"},
            {"Codice": "IT002", "Sesso": "Femmina", "Stato": "In Mungitura"}
        ]),
        'vitelli': pd.DataFrame([
            {"Codice": "IT003", "Sesso": "Femmina", "Stato": "In Stalla"},
            {"Codice": "IT004", "Sesso": "Maschio", "Stato": "In Stalla"}
        ]),
        'maschi': pd.DataFrame([
            {"Codice": "IT005", "Sesso": "Maschio", "Stato": "In Stalla"}
        ])
    }

# 5. Pagine
if scelta == "📊 Dashboard":
    st.title("📊 Centro di Controllo")
    # ... (Codice dashboard invariato)

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla Fotografico Riga per Riga")
    
    # Divisione in TAB (Schede)
    tab1, tab2, tab3 = st.tabs(["🥛 Femmine in Mungitura", "👶 Vitelli / Giovani", "🐂 Maschi Adulti"])
    
    # Dizionario per mappare i gruppi alle chiavi del database simulato
    mappa_tabs = {tab1: 'mungitura', tab2: 'vitelli', tab3: 'maschi'}

    for tab, chiave_db in mappa_tabs.items():
        with tab:
            st.subheader(f"Gestione Capi: {chiave_db.capitalize()}")
            df = st.session_state.db_foto[chiave_db]

            # LA NUOVA TABELLA CON COLONNA FOTO INCORPORATA
            edited_df = st.data_editor(
                df,
                use_container_width=True,
                num_rows="dynamic",
                column_config={
                    "Codice": st.column_config.TextColumn("Codice Capo", help="Inserisci marca auricolare", required=True),
                    "Sesso": st.column_config.SelectboxColumn("Sesso", options=["Maschio", "Femmina"], required=True),
                    "Stato": st.column_config.TextColumn("Stato"),
                    # COLONNA FOTO INCORPORATA
                    "Foto": st.column_config.ImageColumn(
                        "Foto (Click p. ingrandire)",
                        help="Carica o scatta la foto. Clicca sulla miniatura per ingrandire.",
                        required=False
                    )
                },
                hide_index=True,
                key=f"editor_{chiave_db}" # Chiave unica per ogni tabella
            )
            
            # Pulsante per salvare le modifiche a questa tabella
            if st.button(f"💾 SALVA REGISTRO {chiave_db.upper()}"):
                st.session_state.db_foto[chiave_db] = edited_df
                st.success(f"Registro {chiave_db} aggiornato con successo!")
                st.balloons()

elif scelta == "🧀 Vendite":
    # ... (Codice vendite invariato)
    pass

elif scelta == "🌦️ Meteo":
    # ... (Codice meteo invariato)
    pass
