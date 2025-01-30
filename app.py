# app.py
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi App Moderna",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    h1 {
        color: #3498db;
    }
    </style>
    """, unsafe_allow_html=True)

# Título de la aplicación
st.title("Bienvenido a Mi App Moderna 🚀")

# Descripción
st.write("Esta es una aplicación multipágina con un diseño moderno y elegante.")

# Enlace a las páginas
st.sidebar.title("Navegación")
st.sidebar.markdown("Selecciona una página:")
st.sidebar.page_link("app.py", label="Inicio 🏠")
st.sidebar.page_link("pages/1_🏠_Inicio.py", label="Inicio 🏠")
st.sidebar.page_link("pages/2_📊_Analytics.py", label="Analytics 📊")
st.sidebar.page_link("pages/3_📝_Contacto.py", label="Contacto 📝")
