import streamlit as st

st.set_page_config(page_title="MBTI 테스트", page_icon="🧠", layout="centered")

st.title("🧠 나의 MBTI 테스트")
st.write("아래 질문에 답하면 당신의 MBTI를 예측해 드립니다!")

# 질문 리스트
questions = [
    ("파티에서 나는?", ["사람들과 어울리며 대화를 많이 한다", "조용히 몇몇 사람들과 이야기한다"]),
    ("계획은?", ["미리 계획을 세운다", "즉흥적으로 움직인다"]),
    ("결정할 때?", ["논리적으로 분석한다", "감정과 사람을 고려한다"]),
    ("정보를 받을 때?", ["사실과 세부사항에 집중한다", "아이디어와 가능성에 주목한다"])
]

# 점수 저장
scores = {"E": 0, "I": 0, "J": 0, "P": 0, "T": 0, "F": 0, "S": 0, "N": 0}

for idx, (q, options) in enumerate(questions):
    choice = st.radio(q, options, key=idx)
    if idx == 0:  # E / I
        if choice == options[0]:
            scores["E"] += 1
        else:
            scores["I"] += 1
    elif idx == 1:  # J / P
        if choice == options[0]:
            scores["J"] += 1
        else:
            scores["P"] += 1
    elif idx == 2:  # T / F
        if choice == options[0]:
            scores["T"] += 1
        else:
            scores["F"] += 1
    elif idx == 3:  # S / N
        if choice == options[0]:
            scores["S"] += 1
        else:
            scores["N"] += 1

if st.button("결과 확인하기"):
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    st.subheader(f"당신의 MBTI는 **{mbti}** 입니다!")
