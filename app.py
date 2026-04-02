import streamlit as st

# 1. Configurazione Pagina
st.set_page_config(page_title="Torretta Smart Pro", page_icon="🛡️", layout="wide")

# 2. Design Personalizzato Avanzato (CSS)
st.markdown("""
    <style>
    /* Sfondo e font */
    .stApp { background-color: #FDFCF5; }
    
    /* ELIMINA I PALLINI DAL MENU LATERALE */
    [data-testid="stSidebarNav"] {display: none;} /* Nasconde nav standard se presente */
    
    /* Stile per il Radio Button (Menu) */
    div.row-widget.stRadio > div {
        background-color: transparent;
    }
    
    /* Trasforma le opzioni in rettangoli cliccabili */
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: white;
        padding: 15px 20px;
        border-radius: 10px;
        border: 1px solid #E0E0E0;
        margin-bottom: 8px;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s;
    }

    /* NASCONDE IL PALLINO ROSSO/BLU */
    div.row-widget.stRadio > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {
        font-size: 18px;
        font-weight: 500;
        margin-left: 10px;
    }
    
    div[data-testid="stWidgetLabel"] { display: none; } /* Nasconde etichetta menu */

    /* EFFETTO QUANDO CLICCHI (DIVENTA VERDE) */
    div.row-widget.
