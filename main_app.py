import streamlit as st
from PIL import Image

st.title("アプリ")
st.caption("これはテストアプリです。")


# カレントディレクトをapp にしないとエラーになる
# 
image = Image.open("./data/iris.jpg")
st.image(image, width=200)