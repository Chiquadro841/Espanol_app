import streamlit as st
import pandas as pd

# ---- Streamlit Config ----
st.set_page_config(page_title="Aprendizaje", layout="wide")
st.title("📚 Palabras y Frases")

# ---- Caricamento CSV ----
verbs = pd.read_csv("verbs.csv")
words = pd.read_csv("words.csv")

# ---- Menu ----
menu = st.selectbox(
    "Elige la categoría:",
    ["Palabras", "Verbos", "Insertar"]
)

# ---- Funzione per mostrare parole ----
def show_table(df):
    for idx, row in df.iterrows():
        st.write(f"**{row['Italiano']}**")
        key = f"{idx}-{row['Italiano']}"
        if st.button("▶️ Mostrar traducción", key=key):
            st.info(row["Espanol"])


# ---- Funzione inserimento ----
def insert_word():
    st.subheader("➕ Insertar nueva palabra")

    categoria = st.radio(
        "¿Dónde quieres añadirla?",
        ["Palabras", "Verbos"]
    )

    italiano = st.text_input("Italiano")
    espanol = st.text_input("Español")

    if st.button("Guardar"):
        if italiano and espanol:

            nuova_riga = pd.DataFrame(
                [{
                    "Italiano": italiano,
                    "Espanol": espanol
                }]
            )

            if categoria == "Palabras":
                words = pd.read_csv("words.csv")
                words = pd.concat([words, nuova_riga], ignore_index=True)
                words.to_csv("words.csv", index=False)

            else:
                verbs = pd.read_csv("verbs.csv")
                verbs = pd.concat([verbs, nuova_riga], ignore_index=True)
                verbs.to_csv("verbs.csv", index=False)

            st.success(
                f"✅ '{italiano}' añadido a {categoria}"
            )

        else:
            st.warning("Completa los dos campos")


# ---- Visualizzazione ----
if menu == "Palabras":
    show_table(words)

elif menu == "Verbos":
    show_table(verbs)

elif menu == "Insertar":
    insert_word()

