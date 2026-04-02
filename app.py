import streamlit as st
import pandas as pd

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Torretta Management Pro", layout="wide", page_icon="🐄")

# 2. INIZIALIZZAZIONE MEMORIA (Database dell'app)
if 'prodotti_list' not in st.session_state:
    # Qui aggiungi i prodotti base. Quelli nuovi che scriverai si aggiungeranno qui sotto.
    st.session_state.prodotti_list = {"Latte": 0, "Caciocavallo": 0, "Ricotta": 0}
if 'latte_di_oggi' not in st.session_state: st.session_state.latte_di_oggi = 1240
if 'registro_vendite' not in st.session_state: st.session_state.registro_vendite = []
if 'c_mung' not in st.session_state: st.session_state.c_mung = 1
if 'c_vit' not in st.session_state: st.session_state.c_vit = 1
if 'c_mas' not in st.session_state: st.session_state.c_mas = 1

# 3. CSS - DESIGN PROFESSIONALE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8F9FA !important; }
    
    /* Menu Laterale */
    [data-testid="stSidebarNav"] {display: none;}
    div[role="radiogroup"] > label {
        background: white !important; border: 1px solid #E0E0E0 !important;
        padding: 15px !important; border-radius: 10px !important;
        margin-bottom: 10px !important; font-weight: 600 !important;
    }
    div[role="radiogroup"] > label:has(input:checked) {
        background: #2E7D32 !important; color: white !important;
        border: 1px solid #1B5E20 !important; box-shadow: 0 4px 12px rgba(46,125,50,0.2) !important;
    }

    /* Card Statistiche */
    .stat-card {
        background: white; padding: 25px; border-radius: 15px;
        border: 1px solid #EAEAEA; border-bottom: 4px solid #2E7D32;
        text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .stat-val { color: #1B5E20; font-size: 28px; font-weight: 800; margin-top: 10px; }
    
    /* Box Capi e Cassa */
    .st-expander { border: 1px solid #E0E0E0 !important; border-radius: 12px !important; background: white !important; }
    .capo-container {
        background: #FFFFFF; padding: 15px; border-radius: 10px;
        border: 1px solid #E0E0E0; border-left: 5px solid #2E7D32; margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1B5E20;'>🏢 TORRETTA PRO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>v6.0 - Business Suite</p>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("NAVIGAZIONE", ["📊 Dashboard", "🐄 Registro Stalla", "🛒 Cassa e Vendite"], label_visibility="collapsed")
    st.write("---")
    if st.button("🔄 Reset Cache Sistema"):
        st.cache_data.clear()
        st.rerun()

# --- PAGINA DASHBOARD ---
if menu == "📊 Dashboard":
    st.title("📊 Dashboard Operativa")
    
    # Sezione Azioni Rapide
    with st.container():
        st.markdown("<div style='background: #E8F5E9; padding: 20px; border-radius: 15px; margin-bottom: 25px;'>", unsafe_allow_html=True)
        st.subheader("⚡ Azioni Veloci")
        col_r1, col_r2, col_r3 = st.columns(3)
        
        with col_r1:
            with st.expander("🥛 REGISTRA LATTE"):
                nuovo_latte = st.number_input("Litri totali oggi", value=st.session_state.latte_di_oggi)
                if st.button("Conferma Latte"):
                    st.session_state.latte_di_oggi = nuovo_latte
                    st.rerun()
        
        with col_r2:
            with st.expander("📦 CARICO MAGAZZINO"):
                p_carico = st.selectbox("Cosa hai prodotto?", list(st.session_state.prodotti_list.keys()))
                q_carico = st.number_input("Quantità aggiunta", min_value=0.0, step=0.5)
                if st.button("Carica Scorte"):
                    st.session_state.prodotti_list[p_carico] += q_carico
                    st.success(f"{p_carico} aggiornato!")
                    st.rerun()

        with col_r3:
            with st.expander("✨ NUOVO PRODOTTO"):
                nuovo_nome = st.text_input("Nome Prodotto (es. Scamorza)")
                if st.button("Aggiungi a Listino"):
                    if nuovo_nome and nuovo_nome not in st.session_state.prodotti_list:
                        st.session_state.prodotti_list[nuovo_nome] = 0
                        st.success("Aggiunto!")
                        st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Indicatori
    df_v = pd.DataFrame(st.session_state.registro_vendite)
    incasso_tot = df_v['Totale'].sum() if not df_v.empty else 0
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-card"><span>🥛 PRODUZIONE LATTE</span><div class="stat-val">{st.session_state.latte_di_oggi} L</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-card"><span>💰 INCASSO GIORNALIERO</span><div class="stat-val">{incasso_tot:.2f} €</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><span>📦 DISPONIBILITÀ</span>', unsafe_allow_html=True)
        for p, q in st.session_state.prodotti_list.items():
            st.markdown(f"<div style='display:flex; justify-content:space-between;'><b>{p}:</b> <span>{q}</span></div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGINA REGISTRO STALLA ---
elif menu == "🐄 Registro Stalla":
    st.title("🐄 Registro Stalla Fotografico")
    tab1, tab2, tab3 = st.tabs(["🥛 Mungitura", "👶 Vitelli / Giovani", "🐂 Maschi Adulti"])

    def crea_slot_capo(n, prefix, label):
        for i in range(n):
            with st.container():
                st.markdown(f'<div class="capo-container">', unsafe_allow_html=True)
                c_a, c_b, c_c = st.columns([2, 2, 1])
                with c_a: st.text_input(f"Codice {label}", key=f"{prefix}_c_{i}", placeholder="Es. IT001")
                with c_b: st.selectbox("Stato", ["In Produzione", "Asciutta", "In Vendita"], key=f"{prefix}_s_{i}")
                with c_c:
                    f = st.file_uploader("Foto", key=f"{prefix}_f_{i}", label_visibility="collapsed")
                    if f: st.image(f, width=80)
                st.markdown('</div>', unsafe_allow_html=True)

    with tab1:
        crea_slot_capo(st.session_state.c_mung, "m", "Vacca")
        if st.button("➕ AGGIUNGI VACCA"): st.session_state.c_mung += 1; st.rerun()
    with tab2:
        crea_slot_capo(st.session_state.c_vit, "v", "Vitello")
        if st.button("➕ AGGIUNGI VITELLO"): st.session_state.c_vit += 1; st.rerun()
    with tab3:
        crea_slot_capo(st.session_state.c_mas, "t", "Maschio")
        if st.button("➕ AGGIUNGI MASCHIO"): st.session_state.c_mas += 1; st.rerun()

# --- PAGINA CASSA ---
elif menu == "🛒 Cassa e Vendite":
    st.title("🛒 Terminale Vendite")
    col_vendita, col_storico = st.columns([1, 2])
    
    with col_vendita:
        st.subheader("Nuova Transazione")
        with st.form("vendita_form"):
            prod_sel = st.selectbox("Seleziona Prodotto", list(st.session_state.prodotti_list.keys()))
            prezzo_u = st.number_input("Prezzo (€)", min_value=0.0, step=0.5)
            quantita_v = st.number_input("Quantità", min_value=0.0, step=0.1)
            if st.form_submit_button("✅ REGISTRA VENDITA"):
                totale = prezzo_u * quantita_v
                st.session_state.registro_vendite.append({"Prodotto": prod_sel, "Totale": totale})
                st.session_state.prodotti_list[prod_sel] -= quantita_v
                st.rerun()

    with col_storico:
        st.subheader("Riepilogo Vendite")
        if st.session_state.registro_vendite:
            st.table(pd.DataFrame(st.session_state.registro_vendite))
            if st.button("🗑️ Svuota Registro"):
                st.session_state.registro_vendite = []
                st.rerun()
            
