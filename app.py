import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configurazione
st.set_page_config(page_title="Torretta Pro", layout="wide")

# 2. CSS - STILE GENERALE
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
    with c1: st.markdown('<div class="metric-card"><h4>🥛 LATTE OGGI</h4><h2>1.240 L</h2></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-card"><h4>💰 EURO OGGI</h4><h2>450 €</h2></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-card"><h4>🌦️ PIOGGIA</h4><h2>12 mm</h2></div>', unsafe_allow_html=True)
    st.markdown("---")
    col_l, col_e = st.columns(2)
    giorni = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']
    with col_l:
        st.subheader("🥛 Latte Settimanale")
        st.bar_chart(pd.DataFrame({'Litri': [1200, 1250, 1180, 1300, 1280, 1350, 1240]}, index=giorni), color="#2E7D32")
    with col_e:
        st.subheader("💰 Entrate Settimanali")
        st.bar_chart(pd.DataFrame({'Euro': [350, 410, 320, 500, 460, 620, 450]}, index=giorni), color="#FFA000")

elif scelta == "🐄 Registro Stalla":
    st.title("🐄 Registro Anagrafica e Mungitura")
    
    # Dati di esempio iniziali
    if 'stalla_db' not in st.session_state:
        st.session_state.stalla_db = pd.DataFrame([
            {"Codice Capo": "IT001", "Sesso": "Femmina", "Tipo": "Adulto", "In Mungitura": True, "Note": "Ottima produzione"},
            {"Codice Capo": "IT002", "Sesso": "Maschio", "Tipo": "Vitello", "In Mungitura": False, "Note": "-"},
            {"Codice Capo": "IT003", "Sesso": "Femmina", "Tipo": "Vitello", "In Mungitura": False, "Note": "Svezzamento"}
        ])

    # Sezione Filtri Rapidi
    c1, c2, c3 = st.columns(3)
    with c1:
        filtro_sesso = st.multiselect("Filtra Sesso", ["Maschio", "Femmina"], default=["Maschio", "Femmina"])
    with c2:
        filtro_tipo = st.multiselect("Filtra Categoria", ["Vitello", "Adulto"], default=["Vitello", "Adulto"])
    with c3:
        solo_mungitura = st.checkbox("Mostra solo in mungitura")

    # Applichiamo i filtri al database
    df_filtrato = st.session_state.stalla_db[
        (st.session_state.stalla_db["Sesso"].isin(filtro_sesso)) & 
        (st.session_state.stalla_db["Tipo"].isin(filtro_tipo))
    ]
    if solo_mungitura:
        df_filtrato = df_filtrato[df_filtrato["In Mungitura"] == True]

    st.write("### 📝 Lista Capi in Stalla")
    
    # IL VERO REGISTRO A COLONNE EDITABILE
    edited_df = st.data_editor(
        df_filtrato,
        num_rows="dynamic", # Permette di aggiungere/eliminare righe con il tasto +
        column_config={
            "Codice Capo": st.column_config.TextColumn("Codice Capo", help="Inserisci marca auricolare", required=True),
            "Sesso": st.column_config.SelectboxColumn("Sesso", options=["Maschio", "Femmina"], required=True),
            "Tipo": st.column_config.SelectboxColumn("Categoria", options=["Vitello", "Adulto"], required=True),
            "In Mungitura": st.column_config.CheckboxColumn("In Mungitura", help="Seleziona se la vacca è in produzione", default=False),
            "Note": st.column_config.TextColumn("Note")
        },
        use_container_width=True,
        hide_index=True
    )

    if st.button("💾 AGGIORNA REGISTRO"):
        st.session_state.stalla_db = edited_df
        st.success("Registro salvato correttamente!")

elif scelta == "🧀 Vendite":
    st.title("🧀 Punto Vendita")
    euro = st.number_input("Incasso", min_value=0.0)
    if st.button("Registra"): st.success(f"Registrati {euro} €")

elif scelta == "🌦️ Meteo":
    st.title("🌦️ Radar")
    url = "https://www.rainviewer.com/map.html?loc=41.46,15.54,8&type=radar&isPlay=1&color=6"
    st.components.v1.iframe(url, height=500)
