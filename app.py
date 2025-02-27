import streamlit as st
from PIL import Image

st.title("My First App")

st.header("Here is Shadow The Hedgehog")
st.write("He is the ultimate lifeform")
image = Image.open('shads.png')

st.image(image, caption = 'youre welcome')

text = st.text_input('write something', 'this is my text')
st.write('the text that has been written is:', text)

st.subheader('now, we use 2 columns')

col1, col2 = st.columns(2)

with col1:
  st.subheader("This is a column")
  st.write("Shadow is my Religion")
  resp = st.checkbox('I concur')
  if resp:
    st.write('Good...Very Good...')
