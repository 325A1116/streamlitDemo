
import streamlit as st
import random

# --------------------
# 初期設定
# --------------------
st.set_page_config(page_title="名称あてクイズ", page_icon="🎯")
st.title("🎯 名称あてクイズ")

# --------------------
# クイズデータ
# --------------------

QUIZ_DATA = [
    {"question": "日本で一番高い山の名前は？", "answer": "富士山"},
    {"question": "日本の首都は？", "answer": "東京"},
    {"question": "英語で「Apple」と呼ばれる果物は？", "answer": "りんご"},
    {"question": "Windowsを開発した会社名は？", "answer": "マイクロソフト"},
]

# --------------------
# セッションステート初期化
# --------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(QUIZ_DATA)
    st.session_state.feedback = ""
    st.session_state.answered = False

# --------------------
# 問題表示
# --------------------
st.subheader("問題")
st.write(st.session_state.quiz["question"])

# --------------------
# 回答入力
# --------------------
answer = st.text_input("答えを入力してください", key="answer_input")

# --------------------
# 答え合わせ
# --------------------
if st.button("答え合わせ"):
    if answer.strip() == "":
        st.warning("答えを入力してください。")
    elif answer.strip() == st.session_state.quiz["answer"]:
        st.session_state.feedback = "正解！🎉"
        st.session_state.answered = True
    else:
        st.session_state.feedback = (
            f"不正解… 正しい答えは「{st.session_state.quiz['answer']}」です。"
        )
        st.session_state.answered = True

# 結果表示
if st.session_state.feedback:
    if "正解" in st.session_state.feedback:
        st.success(st.session_state.feedback)
    else:
        st.error(st.session_state.feedback)

# --------------------
# 次の問題
# --------------------
if st.session_state.answered:
    if st.button("次の問題へ"):
        st.session_state.quiz = random.choice(QUIZ_DATA)
        st.session_state.feedback = ""
        st.session_state.answered = False
        st.session_state.answer_input = ""
        st.rerun()
