import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# 한글 폰트 설정: fonts 폴더의 NanumGothic-Regular.ttf 사용
font_path = "./fonts/NanumGothic-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

st.title("📊 예시 성적 데이터 분석")

# 예시 성적 데이터 생성
np.random.seed(929)
subjects = ["국어", "영어", "수학", "과학", "사회"]
students = [f"학생{i+1}" for i in range(20)]
data = {subj: np.random.randint(60, 101, size=len(students)) for subj in subjects}
df = pd.DataFrame(data, index=students)

st.subheader("원본 성적 데이터")
st.dataframe(df)

# 과목별 평균 계산
mean_df = pd.DataFrame({"과목별 평균": df.mean()})

st.subheader("과목별 평균 점수 표")
st.table(mean_df)

# 그래프 시각화
st.subheader("과목별 평균 점수 그래프")
fig, ax = plt.subplots()
bars = ax.bar(mean_df.index, mean_df["과목별 평균"], color="skyblue")
ax.set_ylabel("평균 점수", fontproperties=fontprop)
ax.set_ylim(0, 100)
ax.set_title("과목별 평균 점수", fontproperties=fontprop)
ax.set_xticks(range(len(mean_df.index)))
ax.set_xticklabels(mean_df.index, fontproperties=fontprop)
# 각 막대 위에 점수 표시 (한글 폰트 적용)
for bar, value in zip(bars, mean_df["과목별 평균"]):
	ax.text(bar.get_x() + bar.get_width()/2, value + 1, f"{value:.1f}", ha='center', va='bottom', fontproperties=fontprop)
st.pyplot(fig)
