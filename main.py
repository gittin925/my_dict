import streamlit as st

st.set_page_config(
    page_title="マイ辞書アプリ",
    page_icon="📚",
)

st.title("📚 マイ辞書アプリへようこそ！")

if "username" in st.session_state and st.session_state.username:
    st.success(f"こんにちは、{st.session_state.username} さん！")
else:
    st.info("まずは左のメニューから『ユーザー認証』に進んでください。")

st.markdown("""
### 🔧 このアプリでできること：

- ユーザー登録とログイン
- 自分だけの単語辞書を作成
- 登録した単語で自動テストを実行
- 管理者が全ユーザーの管理（登録内容の閲覧・削除）

---
**左側のサイドバーから各ページへ移動できます。**
""")
