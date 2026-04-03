import streamlit as st
import pandas as pd

# 1. SETUP E LOOK PROFESSIONALE
st.set_page_config(page_title="Torretta Pro v12", layout="wide", page_icon="🐄")

# Forza la pulizia di vecchi errori al primo avvio
if 'init_v12' not in st.session_state:
    st.session_state.clear()
    st.session_state.init_v12 = True

# 2. MEMORIA (Dati che non devono sparire)
if 'prod_note' not in st.session_state:
    st.session_state.prod_note = {"Latte": "1240 L", "Caciocavallo": "0 pezzi", "Ricotta": "0 vaschette"}
if 'v_registro' not in st.session_state: st.session_state.v_registro = []
if 'n_mung' not in st.session_state: st.session_state.n_mung = 1
if 'n_vit' not in st.session_state: st.session_state.n_vit = 1
if 'n_mas' not in st.session_state: st.session_state.n_mas = 1

# 3. CSS PER ELIMINARE I PALLINI E COLORARE TUTTO DI VERDE
st.markdown("""
<style>
    .stApp { background-color: #F4F7F6 !important; }
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Tasti Menu Laterale */
    div[role="radiogroup"] > label {
        background-color: white !important; border: 1px solid #d1d5db !important;
        padding: 15px 20px !important; border-radius: 10px !important;
        margin-bottom: 10px !important; font-weight: bold !important; display: flex !important;
    }
    div[role="radiogroup"] > label > div:first-child { display: none !important; }
    div[role="radiogroup"] > label:has(input:checked) {
        background-color: #1B5E20 !important; color: white !important; border: 1px solid #1B5E20 !important;
    }
    div[role="radiogroup"] > label:has(input:checked) p { color: white !important; }

    /* Card Verdi Dashboard */
    .card-verde {
        background: white; padding: 20px; border-radius: 15px;
        border-left: 10px solid #1B5E20; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #1B5E20; text-align: center;'>🛡️ TORRETTA PRO</h2>", unsafe_allow_html=True)
    st.write("---")
    scelta = st.radio("MENU", ["📊 DASHBOARD", "🐄 REGISTRO STALLA", "🛒 CASSA VENDITE"], label_visibility="collapsed")
    st.write("---")
    if st.button("🔄 Reset Totale"): st.session_state.clear(); st.rerun()

# --- PAGINA 1: DASHBOARD ---
if scelta == "📊 DASHBOARD":
    st.title("📊 Riepilogo Produzione")
    c_in, c_out = st.columns([1, 1.5])
    
    with c_in:
        st.subheader("📝 Aggiorna Appunti")
        for p in list(st.session_state.prod_note.keys()):
            st.session_state.prod_note[p] = st.text_input(f"Nota per {p}:", value=st.session_state.prod_note[p])
        
        nuovo_p = st.text_input("✨ Aggiungi nuovo prodotto:")
        if st.button("Inserisci"):
            if nuovo_p: st.session_state.prod_note[nuovo_p] = "0"; st.rerun()

    with c_out:
        st.subheader("📋 Dashboard Visiva")
        for p, q in st.session_state.prod_note.items():
            st.markdown(f"""
            <div class="card-verde">
                <small style='color: #666;'>PRODOTTO</small><br>
                <b style='font-size: 22px;'>{p}</b><br>
                <span style='font-size: 28px; color: #1B5E20; font-weight: bold;'>{q}</span>
            </div>
            """, unsafe_allow_html=True)

# --- PAGINA 2: STALLA (Con Vitelli e Maschi separati) ---
elif scelta == "🐄 REGISTRO STALLA":
    st.title("🐄 Registro Animali")
    tab1, tab2, tab3 = st.tabs(["🥛 MUNGITURA", "👶 VITELLI", "🐂 MASCHI"])

    with tab1:
        for i in range(st.session_state.n_mung):
            col1, col2 = st.columns(2)
            with col1: st.text_input(f"Marca Vacca {i+1}", key=f"m_{i}")
            with col2: st.selectbox("Stato", ["In Mungitura", "Asciutta"], key=f"ms_{i}")
        if st.button("➕ Aggiungi Vacca"): st.session_state.n_mung += 1; st.rerun()

    with tab2:
        for i in range(st.session_state.n_vit):
            col1, col2 = st.columns(2)
            with col1: st.text_input(f"Marca Vitello {i+1}", key=f"v_{i}")
            with col2: st.selectbox("Stato", ["Svezzamento", "Da Segnare"], key=f"vs_{i}")
        if st.button("➕ Aggiungi Vitello"): st.session_state.n_vit += 1; st.rerun()

    with tab3:
        for i in range(st.session_state.n_mas):
            col1, col2 = st.columns(2)
            with col1: st.text_input(f"Marca Maschio {i+1}", key=f"ma_{i}")
            with col2: st.selectbox("Stato", ["Ingrasso", "Toro"], key=f"mas_{i}")
        if st.button("➕ Aggiungi Maschio"): st.session_state.n_mas += 1; st.rerun()

# --- PAGINA 3: CASSA ---
elif scelta == "🛒 CASSA VENDITE":
    st.title("🛒 Cassa")
    cx, cy = st.columns([1, 1.5])
    
    with cx:
        st.subheader("Nuova Vendita")
        with st.form("vendita"):
            pv = st.selectbox("Cosa vendi?", list(st.session_state.prod_note.keys()))
            soldi = st.number_input("Incasso (€)", min_value=0.0)
            if st.form_submit_button("✅ REGISTRA"):
                st.session_state.v_registro.append({"Prodotto": pv, "Euro": soldi})
                st.rerun()

    with cy:
        st.subheader("Storico di oggi")
        if st.session_state.v_registro:
            df = pd.DataFrame(st.session_state.v_registro)
            st.table(df)
            st.metric("TOTALE INCASSATO", f"{df['Euro'].sum():.2f} €")
            if st.button("🗑️ Svuota"): st.session_state.v_registro = []; st.rerun()
