import streamlit as st

st.title("Control de acceso")

edad=st.number_input(
    "Edad:",
    min_value=0,
    value=18
)

tiene_identificacion = st.checkbox(
    "Tiene identificación"
)


if Edad >18:
    st.write("Puede ingresar.")
else:
    st.write("No puede ingresar.")
