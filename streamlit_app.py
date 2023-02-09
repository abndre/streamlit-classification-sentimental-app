import streamlit as st
import pandas as pd

st.write("""
# Projeto Integrador 4 - Interface Reativa
""")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)