import streamlit as st
import os

st.title("📘 あなただけの辞書")

if "username" not in st.session_state or not st.session_state.username:
    st.warning("ログインしてください。")
    st.stop()

username = st.session_state.username
dict_path = f"users_dict/{username}.txt"

def load_dict():
    if not os.path.exists(dict_path):
        return {}
    with open(dict_path, "r") as f:
        lines = f.readlines()
    return {w.split(":")[0]: w.split(":")[1].strip() for w in lines}

def save_dict(dic):
    with open(dict_path, "w") as f:
        for word, meaning in dic.items():
            f.write(f"{word}:{meaning}\n")

user_dict = load_dict()

word = st.text_input("単語を入力")
if word:
    if word in user_dict:
        st.info(f"意味: {user_dict[word]}")
    else:
        meaning = st.text_input("この単語の意味を登録してください")
        if meaning and st.button("登録"):
            user_dict[word] = meaning
            save_dict(user_dict)
            st.success("登録しました！")
