import streamlit as st
from PIL import Image

st.title("My First App")

st.header("Here is Shadow The Hedgehog")
st.write("He is the ultimate lifeform")
image = Image.open('shads.png')

st.image(image, caption = 'youre welcome')

text = st.text_input('write something', 'this is my text')
st.write('the text that has been written is:', text)

st.subheader('Now,The Questioning Begins...')

col1, col2 = st.columns(2)

with col1:
  st.subheader("This is a column")
  st.write("Shadow is my Religion")
  resp = st.checkbox('I concur')
  if resp:
    st.write('Good...Very Good...')
with col2:
  st.subheader("hey, another column!")
  mode = st.radio("How would you like to experience Shadow?",('Visual','Audio','Touch'))
  if mode == 'Visual':
    st.write('ofcourse, witnessing Shadow is One of the Greatest Pleasures')
  if mode == 'Audio':
    st.write('Why yes, he does have a stellar voice, we all enjoy listening to him')
  if mode == 'Touch':
    st.write('Naughty Naughty!!! he might bite! >D')
  
