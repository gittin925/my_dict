import streamlit as st
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

USER_FILE = "users_dict/users.txt"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        lines = f.readlines()
    return {u: p for u, p in (line.strip().split(",") for line in lines)}

def save_user(username, password_hash):
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password_hash}\n")

st.title("🔐 ログイン / 新規登録")

users = load_users()

if "username" not in st.session_state:
    st.session_state.username = None

if st.session_state.username:
    st.success(f"ログイン中: {st.session_state.username}")
    if st.button("ログアウト"):
        st.session_state.username = None
        st.rerun()
else:
    tab1, tab2 = st.tabs(["ログイン", "新規登録"])

    with tab1:
        username = st.text_input("ユーザー名")
        password = st.text_input("パスワード", type="password")
        if st.button("ログイン"):
            if username in users and users[username] == hash_password(password):
                st.session_state.username = username
                st.success("ログイン成功！")
                st.rerun()
            else:
                st.error("ユーザー名またはパスワードが間違っています。")

    with tab2:
        new_username = st.text_input("新しいユーザー名")
        new_password = st.text_input("新しいパスワード", type="password")
        if st.button("登録"):
            if new_username in users:
                st.warning("このユーザー名はすでに使われています。")
            else:
                save_user(new_username, hash_password(new_password))
                open(f"users_dict/{new_username}.txt", "a").close()  # 空ファイル作成
                st.success("登録成功！ログインしてください。")
