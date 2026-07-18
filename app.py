import streamlit as st
import pandas as pd

# ---- Streamlit Config ----
st.set_page_config(page_title="Aprendizaje", layout="wide")
st.title("📚 Palabras y Frases")

# ---- Caricamento CSV ----

verbs = pd.read_csv("verbs.csv")
words = pd.read_csv("words.csv")

# ---- Menu con larghezza limitata ----
menu_container = st.container()
with menu_container:
    st.markdown(
        """
        <style>
        div.stSelectbox {max-width: 300px;}
        </style>
        """, 
        unsafe_allow_html=True
    )
    menu = st.selectbox("Elige la categorìa:", ["Palabras","Verbos"])

# ---- Funzione per mostrare tabella con traduzione nascosta ----
def show_table(df):
    for idx, row in df.iterrows():
        st.write(f"**{row['Italiano']}**")
        # Pulsante per mostrare la traduzione sotto la parola italiana
        key = f"{idx}-{row['Italiano']}"
        if st.button("▶️ Mostra traduciòn", key=key):
            st.info(row["Espanol"])

# ---- Mostra tabella in base al menu ----
if menu == "Palabras":
    show_table(words)
if menu == "Verbos":
    show_table(verbs)
