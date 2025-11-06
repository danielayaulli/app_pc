import streamlit as st
import random

st.title("Práctica Calificada de Cloud Computing")

st.write("Presiona el botón para generar tu nota demo de examen (del 5 al 20).")

if st.button("Generar Nota"):
    nota = random.randint(5, 20)
    st.success(f"Tu nota es: {nota}")
