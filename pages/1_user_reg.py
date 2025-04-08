import streamlit as st
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

USER_FILE = "users_dict/users.txt"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return {u: p for u, p in (line.strip().split(",") for line in lines)}

def save_user(username, password_hash):
    os.makedirs("users_dict", exist_ok=True)
    with open(USER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username},{password_hash}\n")
    # ユーザー辞書ファイルも作成
    with open(f"users_dict/{username}.txt", "w", encoding="utf-8") as f:
        f.write("")

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
            elif new_username == "" or new_password == "":
                st.warning("ユーザー名とパスワードを入力してください。")
            else:
                save_user(new_username, hash_password(new_password))
                st.success("登録成功！ログインしてください。")

# ファイルの中身を表示（確認用）
if st.checkbox("ユーザー情報を確認する（開発用）"):
    if os.path.exists(USER_FILE):
        st.text("users.txt の内容：")
        with open(USER_FILE, "r", encoding="utf-8") as f:
            st.code(f.read())
