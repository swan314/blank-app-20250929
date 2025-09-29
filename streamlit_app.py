


import streamlit as st

st.set_page_config(page_title="스무고개 게임", layout="centered")
st.title("� 스무고개 게임")
st.markdown("## 내가 생각한 사물을 맞춰보세요!")

# 세션 상태 초기화
if "questions" not in st.session_state:
    st.session_state.questions = []  # [(질문, 답변)]
if "tries" not in st.session_state:
    st.session_state.tries = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "guess" not in st.session_state:
    st.session_state.guess = ""

MAX_TRIES = 20

if st.session_state.game_over:
    st.success("게임이 종료되었습니다!")
    st.write("질문 및 답변 기록:")
    for idx, (q, a) in enumerate(st.session_state.questions, 1):
        st.write(f"{idx}. Q: {q} / A: {a}")
    if st.session_state.guess:
        st.write(f"최종 정답 시도: {st.session_state.guess}")
    if st.button("다시 시작"):
        st.session_state.questions = []
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.session_state.guess = ""
    st.stop()

st.write(f"질문 가능 횟수: {MAX_TRIES - st.session_state.tries}회 남음")

with st.form(key="question_form"):
    question = st.text_input("예/아니오로 답할 수 있는 질문을 입력하세요")
    answer = st.radio("답변을 선택하세요", ["예", "아니오", "모름/해당없음"])
    submitted = st.form_submit_button("질문 등록")
    if submitted and question.strip():
        st.session_state.questions.append((question, answer))
        st.session_state.tries += 1
        if st.session_state.tries >= MAX_TRIES:
            st.session_state.game_over = True
        st.experimental_rerun()

if st.session_state.questions:
    st.write("### 질문 및 답변 기록")
    for idx, (q, a) in enumerate(st.session_state.questions, 1):
        st.write(f"{idx}. Q: {q} / A: {a}")

if st.session_state.tries > 0 and not st.session_state.game_over:
    st.markdown("---")
    st.write("정답을 맞출 준비가 되셨나요?")
    guess = st.text_input("정답을 입력하세요 (예: 사과, 자동차 등)")
    if st.button("정답 제출"):
        st.session_state.guess = guess
        st.session_state.game_over = True
        st.experimental_rerun()
