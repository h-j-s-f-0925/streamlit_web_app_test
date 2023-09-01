import streamlit as st


with st.form(key="profile_form_text_box_button"):
    # テキストボックス
    name = st.text_input("名前")
    address = st.text_input("住所")
    
    # ボタン: st.form_submit_button
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
    
if submit_btn:
    st.text(f"ようこそ!{name}さん!{address}に書類を送りました。")