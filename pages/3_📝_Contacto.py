# pages/3_📝_Contacto.py
import streamlit as st

st.title("Contacto 📝")

# Formulario de contacto
with st.form("formulario_contacto"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    mensaje = st.text_area("Mensaje")
    enviado = st.form_submit_button("Enviar")
    
    if enviado:
        st.success(f"Gracias {nombre}, tu mensaje ha sido enviado.")
