

import streamlit as st
import random
st.set_page_config(page_title="구구단 게임", layout="centered")
st.title("🧮 구구단 게임")
st.markdown("## 구구단을 외자! 구구단을 외자!")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "tries" not in st.session_state:
    st.session_state.tries = 0
if "a" not in st.session_state or "b" not in st.session_state:
    st.session_state.a = random.randint(2, 9)
    st.session_state.b = random.randint(1, 9)
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

def new_problem():
    st.session_state.a = random.randint(2, 9)
    st.session_state.b = random.randint(1, 9)
    st.session_state.feedback = ""

st.write(f"문제: {st.session_state.a} × {st.session_state.b} = ?")
answer = st.text_input("정답을 입력하세요", key="answer_input")

col1, col2 = st.columns(2)
with col1:
    if st.button("제출"):
        st.session_state.tries += 1
        try:
            if int(answer) == st.session_state.a * st.session_state.b:
                st.session_state.score += 1
                st.session_state.feedback = "✅ 정답입니다!"
            else:
                st.session_state.feedback = "❌ 오답입니다. 다시 시도하세요."
        except:
            st.session_state.feedback = "숫자를 입력해주세요."
with col2:
    if st.button("새 문제"):
        new_problem()

st.write(st.session_state.feedback)
st.metric("점수", st.session_state.score)
st.metric("시도 횟수", st.session_state.tries)
