import streamlit as st
import random

result_to_pic = {"Esprit":"exprit.png", "Hex":"hex.png", "Janus":"janus.png"}
st.title('Diceroller')
hexdice = st.text_input("Anzahl Hexxen-Würfel", value=5)
jandice = st.text_input("Bonus/Malus", value=0)


if st.button('Würfeln'):
    hexresults = [random.choice(["Leer", "Leer", "leer", "Esprit", "Hex", "Hex"]) for i in range(int(hexdice))]
    for r in hexresults:
        if r.lower() != "leer":
            st.image(result_to_pic[r], width=30)
    janresults = [random.choice(["Leer", "Janus"]) for i in range(int(jandice))]
    for r in janresults:
        if r.lower() != "leer":
            st.image(result_to_pic[r], width=30)

    st.write("Hexxen-Würfel Ergebnisse:")
    st.write(hexresults)
    st.write("Janus-Würfel Ergebnisse:")
    st.write(janresults)
st.text("Icons Credit: Raven - Freepik, Zeus - Eucalyp, Star - Freepik")