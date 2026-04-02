
import streamlit as st

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Torretta Pro", page_icon="🛡️", layout="wide")

# 2. CSS PROFESSIONALE (Menu a bottoni verdi e Dashboard)
st.markdown("""
<style>
    /* Sfondo generale */
    .stApp { background-color: #FDFCF5; }
    
    /* NASCONDE I PALLINI E LO STANDARD DEL MENU */
    [data-testid="stSidebarNav"] {display: none;}
    div.row-widget.stRadio > div[role="radiogroup"] > label [data-testid="stWidgetLabel"] { display: none; }
    
    /* TRASFORMA IL MENU IN BOTTONI CLICCABILI */
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: white;
        padding: 15px 20px !important;
        border-radius: 12px !important;
        border: 1px solid #E0E0E0 !important;
        margin-bottom: 10px !important;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    /* NASCONDE IL CERCHIETTO DEL RADIO */
    div.row-widget.stRadio > div[role="radiogroup"] > label div:first-child { display: none !important; }

    /* TESTO DEL MENU */
    div.row-widget.stRadio > div[role="radiogroup"] > label div[data-testid="st
