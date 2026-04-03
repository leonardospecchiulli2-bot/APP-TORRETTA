import streamlit as st
import pandas as pd

# 1. CONFIGURAZIONE PAGINA (Look Professionale)
st.set_page_config(page_title="Torretta Pro", layout="wide", page_icon="🐄")

# 2. INIZIALIZZAZIONE DATI
if 'note_prod' not in st.session_state:
    st.session_state.note_prod = {"Latte": "1240 L", "Caciocavallo": "0 pezzi", "Ricotta": "0 vaschette"}
if 'vendite_giorno' not in st.session_state: st.session_state.vendite_giorno = []
if 'n_capi' not in st.session_state: st.session_state.n_capi = 1

# 3. CSS PER ELIMINARE I PALLINI E COLORARE IL MENU (Come piace a te)
st.markdown("""
<style>
    .stApp { background-color: #F8F9FA !important; }
    
    /* Nasconde il menu standard di Streamlit e i pallini */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Stile pulsanti menu laterale */
    div[role="radiogroup"] > label {
        background-color: white !important;
        border: 2px solid #E0E0E0 !important;
        padding: 15px 20px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        display: flex !important;
        cursor: pointer !important;
        font-weight: bold !important;
        color: #333 !important;
    }
    
    /* Nasconde il pallino tondo della scelta */
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    
    /* Quando il tasto è selezionato diventa VERDE TORRETTA */
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important;
        color: white !important;
        border: 2px solid #1B5E20 !important;
        box-shadow: 0 4px 12px rgba(27,94,32,0.3) !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }

    /* Card per la Dashboard */
    .card-dash {
        background: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #1B5E20; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 4. MENU LATERALE (Pulito e senza pallini)
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    # Qui le icone sono integrate nel testo per evitare sovrapposizioni
    scelta = st.radio("NAV", ["📊 DASHBOARD", "🐄 STALLA", "🛒 CASSA"], label_visibility="collapsed")
    st.write("---")
    st.success("Sistema Online")

# --- PAGINA 1: DASHBOARD ---
if scelta == "📊 DASHBOARD":
    st.title("📊 Riepilogo Aziendale")
    
    col_sx, col_dx = st.columns([1, 1.5])
    
    with col_sx:
        st.subheader("📝 Segna Produzione")
        for p in list(st.session_state.note_prod.keys()):
            st.session_state.note_prod[p] = st.text_input(f"Quanto {p} oggi?", value=st.session_state.note_prod[p])
        
        st.write("---")
        nuovo = st.text_input("➕ Aggiungi nuovo tipo:")
        if st.button("Aggiungi"):
            if nuovo:
                st.session_state.note_prod[nuovo] = "0"
                st.rerun()

    with col_dx:
        st.subheader("📋 Promemoria Scorte")
        for p, n in st.session_state.note_prod.items():
            st.markdown(f"""
            <div class="card-dash">
                <b style='font-size: 18px; color: #666;'>{p}</b><br>
                <span style='font-size: 26px; font-weight: bold; color: #1B5E20;'>{n}</span>
            </div>
            """, unsafe_allow_html=True)

# --- PAGINA 2: STALLA ---
elif scelta == "🐄 STALLA":
    st.title("🐄 Registro Stalla")
    for i in range(st.session_state.n_capi):
        with st.container():
            st.markdown("<div style='background: white; padding: 15px; border-radius: 12px; margin-bottom: 10px; border: 1px solid #DDD;'>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns([2, 2, 1])
            with c1: st.text_input(f"Codice Auricolare", key=f"capo_{i}")
            with c2: st.selectbox("Stato", ["Mungitura", "Asciutta", "Vitello"], key=f"stato_{i}")
            with c3:
                foto = st.file_uploader("📷", key=f"foto_{i}")
                if foto: st.image(foto, width=60)
            st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("➕ AGGIUNGI RIGA"):
        st.session_state.n_capi += 1
        st.rerun()

# --- PAGINA 3: CASSA ---
elif scelta == "🛒 CASSA":
    st.title("🛒 Cassa e Vendite")
    c_form, c_list = st.columns([1, 1.5])
    
    with c_form:
        st.subheader("Registra Vendita")
        with st.form("vendita_form"):
            p_v = st.selectbox("Prodotto", list(st.session_state.note_prod.keys()))
            soldi = st.number_input("Incasso (€)", min_value=0.0, step=1.0)
            if st.form_submit_button("✅ SALVA VENDITA"):
                st.session_state.vendite_giorno.append({"Prodotto": p_v, "Totale": soldi})
                st.rerun()

    with c_list:
        st.subheader("Incassi di Oggi")
        if st.session_state.vendite_giorno:
            df = pd.DataFrame(st.session_state.vendite_giorno)
            st.table(df)
            st.markdown(f"### TOTALE: {df['Totale'].sum():.2f} €")
            if st.button("🗑️ Svuota Registro"):
                st.session_state.vendite_giorno = []
                st.rerun()
