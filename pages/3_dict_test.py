import streamlit as st
import random
import os

st.title("📝 単語テスト")

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

user_dict = load_dict()

if not user_dict:
    st.info("辞書に単語を登録してください。")
    st.stop()

word, answer = random.choice(list(user_dict.items()))
st.write(f"意味：「{answer}」に対応する単語は？")
user_input = st.text_input("単語を入力")

if user_input:
    if user_input.strip() == word:
        st.success("正解！")
    else:
        st.error(f"不正解… 正解は「{word}」でした。")
