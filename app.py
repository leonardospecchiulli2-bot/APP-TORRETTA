import streamlit as st
import pandas as pd

# 1. CONFIGURAZIONE GRAFICA
st.set_page_config(page_title="Torretta Pro", layout="wide", page_icon="🐄")

# 2. MEMORIA DI SISTEMA
if 'note' not in st.session_state:
    st.session_state.note = {"Latte": "1240 L", "Caciocavallo": "0 pezzi", "Ricotta": "0 vaschette"}
if 'vendite' not in st.session_state: st.session_state.vendite = []
if 'capi' not in st.session_state: st.session_state.capi = 1

# 3. DESIGN PROFESSIONALE (CSS)
st.markdown("""
<style>
    .stApp { background-color: #F0F2F6; }
    /* Sidebar scura e professionale */
    [data-testid="stSidebar"] { background-color: #1E3A34 !important; color: white; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Pulsanti del Menu */
    div[role="radiogroup"] > label {
        background: #2D4F47 !important; border: 1px solid #3E665C !important;
        padding: 12px !important; border-radius: 8px !important;
        margin-bottom: 8px !important; color: white !important; font-weight: bold !important;
    }
    div[role="radiogroup"] > label:has(input:checked) {
        background: #4CAF50 !important; border: 1px solid #81C784 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    }
    
    /* Card Promemoria */
    .note-card {
        background: white; padding: 20px; border-radius: 12px;
        border-left: 6px solid #4CAF50; border-right: 1px solid #DDD;
        border-top: 1px solid #DDD; border-bottom: 1px solid #DDD;
        margin-bottom: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 4. NAVIGAZIONE SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='color: white; text-align: center;'>🛡️ TORRETTA PRO</h1>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("SEZIONI AZIENDALI:", ["📊 DASHBOARD PRO", "🐄 REGISTRO STALLA", "🛒 CASSA VENDITE"])
    st.write("---")
    st.markdown("<p style='text-align: center; color: #81C784;'>v8.0 Active</p>", unsafe_allow_html=True)

# --- PAGINA 1: DASHBOARD / PROMEMORIA ---
if scelta == "📊 DASHBOARD PRO":
    st.title("📊 Riepilogo Produzione")
    
    col_input, col_view = st.columns([1, 1.2])
    
    with col_input:
        st.subheader("✍️ Aggiorna Appunti")
        with st.container():
            for p in list(st.session_state.note.keys()):
                st.session_state.note[p] = st.text_input(f"Stato {p}:", value=st.session_state.note[p])
            
            st.write("---")
            nuovo = st.text_input("✨ Aggiungi nuovo prodotto:")
            if st.button("Aggiungi a Lista"):
                if nuovo:
                    st.session_state.note[nuovo] = "0"
                    st.rerun()

    with col_view:
        st.subheader("📋 Promemoria Scorte")
        for p, n in st.session_state.note.items():
            st.markdown(f"""
            <div class="note-card">
                <span style='color: #666; font-size: 14px;'>PRODOTTO</span><br>
                <b style='font-size: 20px;'>{p}</b><br>
                <span style='color: #4CAF50; font-size: 24px; font-weight: bold;'>{n}</span>
            </div>
            """, unsafe_allow_html=True)

# --- PAGINA 2: STALLA ---
elif scelta == "🐄 REGISTRO STALLA":
    st.title("🐄 Registro Capi")
    for i in range(st.session_state.capi):
        with st.container():
            st.markdown(f"<div style='background: white; padding: 15px; border-radius: 10px; border: 1px solid #DDD; margin-bottom: 10px;'>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns([2, 2, 1])
            with c1: st.text_input(f"Codice Capo {i+1}", key=f"c_{i}")
            with c2: st.selectbox("Stato", ["Mungitura", "Asciutta", "Vendita"], key=f"s_{i}")
            with c3:
                foto = st.file_uploader("📷", key=f"f_{i}")
                if foto: st.image(foto, width=60)
            st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("➕ AGGIUNGI RIGA"):
        st.session_state.capi += 1
        st.rerun()

# --- PAGINA 3: CASSA ---
elif scelta == "🛒 CASSA VENDITE":
    st.title("🛒 Terminale Cassa")
    ca, cb = st.columns([1, 1.5])
    
    with ca:
        st.subheader("Nuovo Incasso")
        with st.form("form_v"):
            p_v = st.selectbox("Cosa hai venduto?", list(st.session_state.note.keys()))
            prezzo = st.number_input("Soldi ricevuti (€)", min_value=0.0)
            if st.form_submit_button("✅ REGISTRA"):
                st.session_state.vendite.append({"Prodotto": p_v, "Incasso": prezzo})
                st.rerun()
    
    with cb:
        st.subheader("Storico Vendite")
        if st.session_state.vendite:
            df = pd.DataFrame(st.session_state.vendite)
            st.table(df)
            st.metric("TOTALE INCASSATO", f"{df['Incasso'].sum():.2f} €")
            if st.button("🗑️ Reset Giornata"):
                st.session_state.vendite = []
                st.rerun()
