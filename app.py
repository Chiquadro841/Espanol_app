import streamlit as st
import pandas as pd

# ---- Streamlit Config ----
st.set_page_config(page_title="English Learning App", layout="wide")
st.title("📚 English Phrasal Verbs & Vocabulary")

# ---- Caricamento CSV ----
# Assumiamo che i file siano phrasal_verbs.csv e words_adjectives.csv con colonne: Italian, English
phrasal_verbs = pd.read_csv("phrasal_verbs.csv")
words_adjectives = pd.read_csv("words_adjectives.csv")
miscellaneous = pd.read_csv("words2.csv")

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
    menu = st.selectbox("Scegli categoria:", ["Phrasal Verbs", "Words & Adjectives","words2"])

# ---- Funzione per mostrare tabella con traduzione nascosta ----
def show_table(df):
    for idx, row in df.iterrows():
        st.write(f"**{row['Italian']}**")
        # Pulsante per mostrare la traduzione sotto la parola italiana
        key = f"{idx}-{row['Italian']}"
        if st.button("▶️ Mostra traduzione", key=key):
            st.info(row["English"])

# ---- Mostra tabella in base al menu ----
if menu == "Phrasal Verbs":
    show_table(phrasal_verbs)
if menu == "Words & Adjectives":
    show_table(words_adjectives)
elif menu=="miscellaneous":
    show_table(miscellaneous)

