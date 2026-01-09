import streamlit as st
import random
# from PIL import Image
# import os

# --------------------
# 初期設定
# --------------------
st.set_page_config(page_title="顔文字名称あてクイズ", page_icon="🖼️")
st.title("🖼️ 画像から名称を当てるクイズ（全10問）")

# --------------------
# クイズデータ（10問）
# ※ 画像と答えは自分用に変更してください
# --------------------
QUIZ_DATA = [
    {"image_url": "1f600", "answer": "にこやかな笑顔"},
    {"image_url": "1f601", "answer": "目もにこやかな笑顔"},
    {"image_url": "1f601", "answer": "目もにこやかな笑顔"}
    # {"image": "https://emojix.s3.ap-northeast-1.amazonaws.com/g3/svg/1f600.svg;", "answer": "笑い転げる顔"},
    # {"image": "https://emojix.s3.ap-northeast-1.amazonaws.com/g3/svg/1f600.svg;", "answer": "嬉し泣きの顔"},
    # {"image": "https://emojix.s3.ap-northeast-1.amazonaws.com/g3/svg/1f600.svg", "answer": "控え目な笑顔"},
    # {"image": "images/q6.jpg", "answer": "新幹線"},
    # {"image": "images/q7.jpg", "answer": "飛行機"},
    # {"image": "images/q8.jpg", "answer": "自転車"},
    # {"image": "images/q9.jpg", "answer": "カメラ"},
    # {"image": "images/q10.jpg", "answer": "時計"},
]
# --------------------
# 問題数設定（クイズ開始前）
# --------------------
max_questions = len(QUIZ_DATA)

num_questions = st.slider(
    "出題する問題数を選んでください",
    1,max_questions,max_questions
)

# --------------------
# ランダム出題（問題固定）
# --------------------
if "quiz_list" not in st.session_state or st.session_state.get("num_questions") != num_questions:
    st.session_state.quiz_list = random.sample(QUIZ_DATA, num_questions)
    st.session_state.num_questions = num_questions

quiz_list = st.session_state.quiz_list

st.divider()

# 選択された問題数だけ使う
# quiz_list = QUIZ_DATA[:num_questions]


# --------------------
# 回答入力欄
# --------------------
for i, quiz in enumerate(quiz_list):
    st.subheader(f"問題 {i + 1}")

    emoji_code = quiz["image_url"]
    twemoji_url = f"https://twemoji.maxcdn.com/v/latest/svg/{emoji_code}.svg"

    # Twemoji表示
    st.markdown(
        f'<img src="{twemoji_url}" width="200">',
        unsafe_allow_html=True
    )

    st.text_input(
        "この顔文字の名称は？",
        key=f"answer_{i}"
    )

    st.divider()


# --------------------
# 採点
# --------------------
if st.button("まとめて答え合わせ"):
    score = 0
    st.subheader("結果")

    for i, quiz in enumerate(quiz_list):
        correct = quiz["answer"]
        user_answer = st.session_state.get(f"answer_{i}", "").strip()

        if user_answer == correct:
            st.success(f"問題 {i + 1}：正解")
            score += 1
        else:
            st.error(f"問題 {i + 1}：不正解（正解：{correct}）")

    st.markdown(f"##  得点：{score} / {len(quiz_list)}")
    
# --------------------
# 出典表記
# --------------------
st.caption("画像出典：Twemoji（https://twemoji.twitter.com/）")

