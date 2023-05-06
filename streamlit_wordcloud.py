import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.write("""
# Projeto Integrador 4 - Wordcloud
""")

df = pd.read_csv("data/imdb-reviews-pt-br.zip")

text = " ".join(i for i in df.text_pt)

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
