import streamlit as st
import pandas as pd

# 1. Configurazione Pagina Professionale
st.set_page_config(
    page_title="Torretta Management System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Design Personalizzato (CSS)
st.markdown("""
    <style>
    /* Sfondo e font */
    .main { background-color: #0e1117; color: #fafafa; }
    
    /* Card per i dati */
    .stMetric {
        background-color: #1e2129;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #2e3139;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Bottoni */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #00c853;
        color: black;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #b9f6ca;
        transform: translateY(-2px);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Professionale
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #00c853;'>🛡️ TORRETTA v1.0</h2>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("SISTEMA DI GESTIONE", 
                    ["📊 Dashboard Aziendale", "🐄 Registro Zootecnico", "💰 Controllo Vendite", "📡 Radar & Meteo"])
    st.markdown("---")
    st.caption("Accesso Operatore: Leonardo")

# --- LOGICA DELLE SEZIONI ---

if menu == "📊 Dashboard Aziendale":
    st.title("Quadro Generale Operativo")
    
    # Riga Metriche Veloci
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Latte Totale (24h)", "1.240 L", "+12%")
    with col2:
        st.metric("Vendite Odierne", "450,00 €", "Stabile")
    with col3:
        st.metric("Capi in Produzione", "38", "-2")
    with col4:
        st.metric("Umidità Terreno", "22%", "Ottimale")

    st.markdown("---")
    st.subheader("🚜 Stato Mezzi John Deere")
    st.info("Sistema in attesa di autorizzazione API. Collegamento crittografato pronto.")

elif menu == "🐄 Registro Zootecnico":
    st.header("Gestione Produzione Latte")
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.markdown("### Inserimento Dati")
        tipo = st.selectbox("Seleziona Gruppo", ["Vacche Frisone", "Pecore Sarde", "Gruppo B"])
        quantita = st.number_input("Volume Munto (Litri)", min_value=0.0, format="%.2f")
        operatore = st.text_input("Note Tecniche / Operatore")
        
        if st.button("ARCHIVIA DATI"):
            st.toast("Dato inviato al database centrale...")
            st.success("Operazione completata con successo.")

    with col_b:
        st.markdown("### Storico Recente")
        dati_finti = pd.DataFrame({
            'Data': ['02/04', '01/04', '31/03'],
            'Litri': [120, 115, 122]
        })
        st.table(dati_finti)

elif menu == "💰 Controllo Vendite":
    st.header("Registro Transazioni Punto Vendita")
    
    col_x, col_y = st.columns(2)
    with col_x:
        prod = st.selectbox("Categoria", ["Formaggi Freschi", "Stagionati", "Carni", "Latticini"])
        prezzo = st.number_input("Importo Totale (€)", min_value=0.0)
    
    with col_y:
        metodo = st.selectbox("Metodo di Pagamento", ["Contanti", "POS / Carta", "Sospeso"])
    
    if st.button("REGISTRA TRANSAZIONE"):
        st.success(f"Transazione di {prezzo}€ registrata correttamente.")

elif menu == "📡 Radar & Meteo":
    st.header("Monitoraggio Ambientale")
    st.markdown("### Radar Precipitazioni (Tempo Reale)")
    
    # Inserimento Radar vero (Placeholder avanzato)
    st.image("https://www.meteoam.it/images/radar/radar_nazionale.png", use_container_width=True)
    
    st.markdown("---")
    st.subheader("Dati Pluviometrici Terreni")
    st.write("Aggiornamento ogni 15 minuti via satellite.")
