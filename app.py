import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# --- 1. CONFIGURAZIONE ---
st.set_page_config(page_title="Torretta Elite", layout="wide", page_icon="🌿")

# --- 2. STILE PROFESSIONALE BEIGE & VERDE ---
st.markdown("""
<style>
    .stApp { background-color: #FDFBF0; color: #1B3022; }
    [data-testid="stSidebar"] { background-color: #1B3022 !important; }
    [data-testid="stSidebar"] * { color: #FDFBF0 !important; }
    .stat-card {
        background: #FFFFFF;
        border-radius: 15px;
        padding: 25px;
        border: 1px solid #E0E0C0;
        border-top: 8px solid #2E7D32;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        text-align: center;
    }
    .stat-val { font-size: 42px; font-weight: bold; color: #2E7D32; margin-bottom: 0; }
    .stat-lab { font-size: 14px; color: #5D6D5F; text-transform: uppercase; font-weight: bold; }
    .stButton>button {
        background-color: #2E7D32; color: #FDFBF0; border-radius: 10px;
        font-weight: bold; height: 3em; border: none; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. DATABASE ---
if 'db_stalla' not in st.session_state:
    st.session_state.db_stalla = pd.DataFrame([
        {'Marca': 'IT001', 'Nome': 'Regina', 'Stato': 'Lattazione', 'Litri': 35},
        {'Marca': 'IT002', 'Nome': 'Mora', 'Stato': 'Asciutta', 'Litri': 0}
    ])
if 'cassa' not in st.session_state: st.session_state.cassa = 0.0

# --- 4. MENU ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>AZ. AGR.<br>TORRETTA</h2>", unsafe_allow_html=True)
    sel = option_menu(None, ["Dashboard", "Registro Stalla", "Cassa Smart", "JD-Link"], 
        icons=['grid-1x2', 'clipboard-heart', 'cart3', 'geo-alt'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"background-color": "transparent"},
            "nav-link": {"color": "#FDFBF0", "font-size": "16px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#2E7D32"}
        })

# --- 5. LOGICA ---
if sel == "Dashboard":
    st.markdown("<h1>🌿 Centro di Controllo</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='stat-card'><p class='stat-lab'>Latte Oggi</p><p class='stat-val'>{st.session_state.db_stalla['Litri'].sum()} L</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='stat-card'><p class='stat-lab'>Capi Totali</p><p class='stat-val'>{len(st.session_state.db_stalla)}</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='stat-card'><p class='stat-lab'>Incasso Totale</p><p class='stat-val'>{st.session_state.cassa:.2f} €</p></div>", unsafe_allow_html=True)

    st.write("---")
    st.markdown("<div class='stat-card'>", unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'], y=[1180, 1220, 1240, 1210, 1250, 1310, 1290],
                    mode='lines+markers', line=dict(color='#2E7D32', width=4), fill='tozeroy', fillcolor='rgba(46, 125, 50, 0.05)'))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif sel == "Registro Stalla":
    st.markdown("<h1>🐄 Gestione Mandria</h1>", unsafe_allow_html=True)
    st.markdown("<div class='stat-card'>", unsafe_allow_html=True)
    st.dataframe(st.session_state.db_stalla, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    with st.expander("➕ AGGIUNGI CAPO"):
        with st.form("new_cow"):
            col1, col2 = st.columns(2)
            ma = col1.text_input("Marca")
            no = col2.text_input("Nome")
            st_c = col1.selectbox("Stato", ["Lattazione", "Asciutta", "Rimonta"])
            li = col2.number_input("Litri", 0)
            if st.form_submit_button("REGISTRA"):
                new = {'Marca': ma, 'Nome': no, 'Stato': st_c, 'Litri': li}
                st.session_state.db_stalla = pd.concat([st.session_state.db_stalla, pd.DataFrame([new])], ignore_index=True)
                st.rerun()

elif sel == "Cassa Smart":
    st.markdown("<h1>🛒 Punto Vendita</h1>", unsafe_allow_html=True)
    colA, colB = st.columns(2)
    with colA:
        st.markdown("<div class='stat-card'>", unsafe_allow_html=True)
        importo = st.number_input("Prezzo (€)", min_value=0.0, step=1.0)
        if st.button("CONFERMA VENDITA"):
            st.session_state.cassa += importo
            st.toast("Incasso registrato!")
        st.markdown("</div>", unsafe_allow_html=True)
    with colB:
        st.markdown(f"<div class='stat-card'><p class='stat-lab'>Totale Odierno</p><p class='stat-val'>{st.session_state.cassa:.2f} €</p></div>", unsafe_allow_html=True)

elif sel == "JD-Link":
    st.markdown("<h1>🚜 Telemetria John Deere</h1>", unsafe_allow_html=True)
    st.info("Piattaforma pronta per la sincronizzazione con JD-Link.")
