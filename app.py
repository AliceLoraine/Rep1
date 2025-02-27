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

st.subheader("press wisely")
if st.button('press here to commit your eternal alliance to Shadow The Hedgehog'):
  st.write('Wonderful! He has forgiven all your sins')
else:
  st.write('Go on....Hes Waiting for you...you wont like him when hes mad...')

st.subheader("Seleccion")
in_mod = st.selectbox(
  "Choose....",
  ("Audio","Visual","Haptic"),
)
if in_mod == "Audio":
  set_mod = "Play Audio"
elif in_mod == "Visual":
  set_mod = "Play Video"
elif in_mod == "Haptic":
  set_mod = "Vibrate"
st.write("Now Doing:", set_mod)

  
