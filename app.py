import streamlit as st
from PIL import Image

st.title("My First App")

st.header("Here is Shadow The Hedgehog")
st.write("He is the ultimate lifeform")
image = Image.open('shads.png')

st.image(image, caption = 'youre welcome')
