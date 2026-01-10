import streamlit as st
import random


# 初期設定
st.set_page_config(page_title="顔文字名称あてクイズ", page_icon="🤔")
st.title("顔文字の名称を当てるクイズ")
def hira_to_kata(text: str) -> str:
    result = ""
    for c in text:
        if "ぁ" <= c <= "ゖ":
            result += chr(ord(c) + 0x60)
        else:
            result += c
    return result

def normalize(text: str) -> str:
    return hira_to_kata(text.strip().replace(" ", "").replace("　", ""))

# 上にスクロール
def scroll_to_top():
    st.markdown(
        """
        <script>
            window.scrollTo(0, 0);
        </script>
        """,
        unsafe_allow_html=True
    )


# クイズデータ
QUIZ_DATA = [
    {"image_url": "1f600", "answer": "にこやかな笑顔"},
    {"image_url": "1f604", "answer": "目もにこやかな笑顔"},
    {"image_url": "1f603", "answer": "大きい目の笑顔"},
    {"image_url": "1f601", "answer": "輝く笑顔"},
    {"image_url": "1f606", "answer": "大笑いの顔"},
    {"image_url": "1f605", "answer": "汗をかいた笑顔"},
    {"image_url": "1f923", "answer": "笑い転げる顔"},
    {"image_url": "1f602", "answer": "目もにこやかな笑顔"},
    {"image_url": "1f642", "answer": "控え目な笑顔"},
    {"image_url": "1f643", "answer": "逆さまの顔"},
    {"image_url": "1f609", "answer": "ウィンクの顔"},
    {"image_url": "1fae0", "answer": "溶ける顔"},
    {"image_url": "1f60a", "answer": "微笑む目の笑顔"},
    {"image_url": "1f607", "answer": "天使の輪がついた笑顔"},
    {"image_url": "1f637", "answer": "マスク顔"},
    {"image_url": "1f914", "answer": "試行中の顔"},
    {"image_url": "1f917", "answer": "ハグの顔"},
    {"image_url": "1f92b", "answer": "静かにの顔"},
    {"image_url": "1f913", "answer": "オタク顔"},
    {"image_url": "1f60e", "answer": "サングラスの笑顔"},
    {"image_url": "1f60c", "answer": "ほっとした顔"},
    {"image_url": "1f614", "answer": "物思いの顔"},
    {"image_url": "1f62a", "answer": "眠い顔"},
    {"image_url": "1f924", "answer": "よだれ顔"},
    {"image_url": "1f634", "answer": "寝てる顔"},
    {"image_url": "1f615", "answer": "混乱した顔"},
    {"image_url": "1f979", "answer": "涙をこらえている顔"},
    {"image_url": "1f622", "answer": "泣き顔"},
    {"image_url": "1f62d", "answer": "大声で泣いている顔"},
    {"image_url": "1f631", "answer": "恐怖で叫ぶ顔"},
    
    
]

# 問題数設定（クイズ開始前）
available_counts = [n for n in [10, 20, 30] if n <= len(QUIZ_DATA)]

num_questions = st.radio(
    "出題する問題数を選んでください",
    available_counts,
    horizontal=True
)


# ランダム出題
if "quiz_list" not in st.session_state or st.session_state.get("num_questions") != num_questions:
    st.session_state.quiz_list = random.sample(QUIZ_DATA, num_questions)
    st.session_state.num_questions = num_questions

quiz_list = st.session_state.quiz_list

st.divider()


# 回答入力
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



# 採点
if st.button("まとめて答え合わせ"):
    score = 0
    st.subheader("結果")

    for i, quiz in enumerate(quiz_list):
        user = normalize(st.session_state.get(f"answer_{i}", ""))
        correct = normalize(quiz["answer"])

        if user == correct:
            st.success(f"問題 {i + 1}：正解")
            score += 1
        else:
            st.error(f"問題 {i + 1}：不正解（正解：{quiz['answer']}）")

    st.markdown(f"## 得点：{score} / {len(quiz_list)}")

    # もう一度出題
    if st.button("🔄 もう一度出題"):
        st.session_state.pop("quiz_list")
        scroll_to_top()
        st.experimental_rerun()
    
# --------------------
# 出典表記
# --------------------
st.caption(
    "画像提供：Twemoji © Twitter, Inc.（CC BY 4.0）｜"
    "名称・解説参考：Let's Emoji（https://lets-emoji.com/）"
)



