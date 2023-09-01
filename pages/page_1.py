import streamlit as st
from PIL import Image

code = '''
import streamlit as st

st.title("アプリ")

'''
st.code(code, language="python")

image = Image.open("./data/iris.jpg")
st.image(image, width=200)