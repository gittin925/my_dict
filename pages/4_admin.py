import streamlit as st
import os

st.title("👤 管理者ページ")

admin_user = "admin"  # 管理者ユーザー名を固定（パスワードも登録時に定義）

if st.session_state.get("username") != admin_user:
    st.warning("このページは管理者専用です。")
    st.stop()

user_files = [f for f in os.listdir("users_dict") if f.endswith(".txt") and f != "users.txt"]

for filename in user_files:
    st.subheader(f"📂 {filename.replace('.txt', '')} の辞書内容")
    with open(f"users_dict/{filename}", "r") as f:
        content = f.read()
    st.text_area("内容", content, height=150, key=filename)

    if st.button("削除", key="del_" + filename):
        os.remove(f"users_dict/{filename}")
        st.success(f"{filename} を削除しました。")
        st.experimental_rerun()
