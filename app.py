import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# 1. CONFIGURAZIONE E STILE "APP MOBILE"
st.set_page_config(page_title="Torretta Pro", layout="wide", page_icon="🐄")

# CSS Esterno per rendere i bottoni enormi sul telefono
st.markdown("""
<style>
    .stButton>button {
        width: 100%; border-radius: 15px; height: 3em;
        background-color: #2E7D32; color: white; font-weight: bold;
        border: none; box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .main { background-color: #F0F2F5; }
    .stMetric { background-color: white; padding: 15px; border-radius: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

# 2. MENU ESTERNO (Molto più bello)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2304/2304779.png", width=100)
    selected = option_menu(
        menu_title="Torretta Menu",
        options=["Dashboard", "Stalla", "Cassa", "JD-Link"],
        icons=["house", "cow", "cart", "gear"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#1E3A34"},
            "icon": {"color": "#81C784", "font-size": "25px"}, 
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"5px", "color": "white"},
            "nav-link-selected": {"background-color": "#2E7D32"},
        }
    )

# 3. DATABASE
if 'prod' not in st.session_state: st.session_state.prod = {"Latte": "0", "Formaggio": "0"}
if 'v_reg' not in st.session_state: st.session_state.v_reg = []
if 'capi' not in st.session_state: st.session_state.capi = []

# --- LOGICA PAGINE ---

if selected == "Dashboard":
    st.markdown("### 📊 Produzione Odierna")
    cols = st.columns(len(st.session_state.prod))
    for i, (p, q) in enumerate(st.session_state.prod.items()):
        with cols[i]:
            st.metric(label=p, value=q)
    
    st.markdown("---")
    with st.expander("📝 Modifica Dati"):
        for p in list(st.session_state.prod.keys()):
            st.session_state.prod[p] = st.text_input(f"Aggiorna {p}", value=st.session_state.prod[p])

elif selected == "Stalla":
    st.title("🐄 Registro Animali")
    tipo = st.segmented_control("Categoria", ["Vacche", "Vitelli", "Maschi"], default="Vacche")
    
    with st.form("stalla_form"):
        c1, c2 = st.columns(2)
        m_aur = c1.text_input("Marca Auricolare")
        m_stato = c2.selectbox("Stato", ["Mungitura", "Asciutta", "Ingrasso", "Svezzamento"])
        if st.form_submit_button("REGISTRA CAPO"):
            st.session_state.capi.append({"Tipo": tipo, "Codice": m_aur, "Stato": m_stato})
            st.success("Registrato!")

    if st.session_state.capi:
        df_c = pd.DataFrame(st.session_state.capi)
        st.dataframe(df_c[df_c['Tipo'] == tipo], use_container_width=True)

elif selected == "Cassa":
    st.title("🛒 Terminale Vendita")
    with st.container():
        p_v = st.selectbox("Cosa stai vendendo?", list(st.session_state.prod.keys()))
        e_v = st.number_input("Prezzo (€)", min_value=0.0)
        if st.button("CONFERMA VENDITA"):
            st.session_state.v_reg.append({"Prod": p_v, "Euro": e_v})
            st.balloons() # Effetto grafico per la vendita!
    
    if st.session_state.v_reg:
        df_v = pd.DataFrame(st.session_state.v_reg)
        st.table(df_v)
        st.write(f"### Totale Incassato: {df_v['Euro'].sum():.2f} €")

elif selected == "JD-Link":
    st.title("🚜 Gestione Macchine")
    st.warning("Sezione Manutenzione Mezzi John Deere")
    mezzo = st.selectbox("Seleziona Mezzo", ["Trattore 6120", "Trattore 5050", "Mietitrebbia", "Altro"])
    ore = st.number_input("Ore attuali", min_value=0)
    if st.button("Salva Report Ore"):
        st.success(f"Ore del {mezzo} aggiornate a {ore}")
