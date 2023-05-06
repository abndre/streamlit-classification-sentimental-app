import streamlit as st
import pandas as pd
sentimento  = ""
st.write("""
# Projeto Integrador 4 - Análise de Sentimento com Modelo Treinado pelo Grupo
""")

import joblib
# Carrega o modelo e o vetorizador
clf = joblib.load("model//multinominalnb_model//model.pkl")
vectorizer = joblib.load("model//multinominalnb_model//vectorizer.pkl")


def prediction(text):

    # Dados de teste (texto)
    new_text = [text]

    # Transforma o novo texto em um vetor de recursos
    new_text_vector = vectorizer.transform(new_text)

    # Faz a previsão
    prediction = clf.predict(new_text_vector)

    #print("A previsão é:", prediction[0])
    return prediction[0]

title = st.text_input('Coloque o texto para avaliação de sentimento', 'Hoje foi um bom dia')
if st.button('Predição'):
    returno_predicao = prediction(title)
    if returno_predicao ==0:
        sentimento = "Negativo"
    else:
        sentimento = "Positivo"
    st.write(f"A previsão é: {returno_predicao} -> {sentimento}")

#st.write('A previsão é: ', title)