# pages/2_📊_Analytics.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("Analytics 📊")

# Generar datos de ejemplo
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randn(100).cumsum()
})

# Mostrar gráfico
st.line_chart(data, x='x', y='y')
