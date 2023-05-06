import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.write("""
# Projeto Integrador 4 - Wordcloud
""")

with open('data/clean_txt.txt', 'r') as file:
    result_list = file.read().splitlines()

text = " ".join(i for i in result_list)
wordcloud = WordCloud(background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


st.pyplot()
