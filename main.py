import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 성격 테스트", page_icon="🧠", layout="centered")

st.markdown(
    """
    <style>
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .result {
        font-size: 2em;
        color: #FF5722;
        text-align: center;
        font-weight: bold;
    }
    .desc {
        font-size: 1.2em;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🧠 나의 MBTI 성격 테스트</div>', unsafe_allow_html=True)
st.write("아래 8가지 질문에 답해 보세요! 당신의 성격 유형을 알려드립니다.")

# 질문 리스트 (8개)
questions = [
    ("파티에 가면 나는?", ["사람들과 활발히 어울린다", "몇 명과 조용히 이야기한다"]),
    ("휴일 계획은?", ["미리 계획을 세운다", "그때그때 정한다"]),
    ("결정할 때 더 중요한 것은?", ["논리와 사실", "감정과 관계"]),
    ("정보를 받을 때 나는?", ["세부사항과 사실에 집중한다", "아이디어와 가능성에 주목한다"]),
    ("친구와 대화할 때 나는?", ["대화를 주도한다", "경청하는 편이다"]),
    ("일을 처리할 때 나는?", ["정해진 규칙과 절차를 따른다", "상황에 맞게 유연하게 한다"]),
    ("문제를 해결할 때 나는?", ["객관적인 자료를 본다", "사람들의 기분을 고려한다"]),
    ("창의적인 활동에서 나는?", ["현실적으로 실행 가능한 것에 집중", "새로운 가능성을 상상"])
]

# MBTI 점수 초기화
scores = {"E": 0, "I": 0, "J": 0, "P": 0, "T": 0, "F": 0, "S": 0, "N": 0}

# 질문 표시
for idx, (q, options) in enumerate(questions):
    choice = st.radio(f"{idx+1}. {q}", options, key=idx)
    if idx in [0, 4]:  # E / I
        scores["E"] += choice == options[0]
        scores["I"] += choice == options[1]
    elif idx in [1, 5]:  # J / P
        scores["J"] += choice == options[0]
        scores["P"] += choice == options[1]
    elif idx in [2, 6]:  # T / F
        scores["T"] += choice == options[0]
        scores["F"] += choice == options[1]
    elif idx in [3, 7]:  # S / N
        scores["S"] += choice == options[0]
        scores["N"] += choice == options[1]

# MBTI 결과 설명
mbti_descriptions = {
    "ISTJ": "신중하고 책임감 있는 관리자형. 약속을 잘 지키고 체계적인 성격.",
    "ISFJ": "헌신적이고 배려심 깊은 수호자형. 주변 사람을 잘 돌봄.",
    "INFJ": "통찰력 있고 이상주의적인 옹호자형. 깊은 대화를 좋아함.",
    "INTJ": "계획적이고 전략적인 전략가형. 목표를 향해 차근차근 나아감.",
    "ISTP": "유연하고 분석적인 장인형. 문제 해결에 능숙함.",
    "ISFP": "따뜻하고 예술적인 예술가형. 조용하지만 감정이 깊음.",
    "INFP": "이상적이고 가치 지향적인 중재자형. 다른 사람을 돕는 것을 좋아함.",
    "INTP": "호기심 많고 분석적인 사색가형. 새로운 지식을 탐구함.",
    "ESTP": "활발하고 도전적인 사업가형. 즉흥적으로 문제 해결.",
    "ESFP": "사교적이고 긍정적인 연예인형. 즐거운 분위기를 만듦.",
    "ENFP": "창의적이고 열정적인 활동가형. 새로운 가능성을 탐험.",
    "ENTP": "논쟁을 즐기고 아이디어가 많은 발명가형.",
    "ESTJ": "체계적이고 실용적인 경영자형. 리더십이 뛰어남.",
    "ESFJ": "친절하고 협조적인 사교가형. 관계를 중요시함.",
    "ENFJ": "카리스마 있고 사교적인 지도자형. 타인을 이끄는 데 능숙.",
    "ENTJ": "결단력 있고 효율적인 지휘관형. 목표 달성에 집중."
}

# 결과 버튼
if st.button("📊 결과 확인하기"):
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    st.balloons()  # 풍선 효과
    st.markdown(f'<div class="result">당신의 MBTI는 {mbti} 입니다!</div>', unsafe_allow_html=True)

    if mbti in mbti_descriptions:
        st.markdown(f'<div class="desc">{mbti_descriptions[mbti]}</div>', unsafe_allow_html=True)

    # MBTI 이미지 표시 (구글 이미지 사용 가능)
    st.image(f"https://raw.githubusercontent.com/creotiv/mbti-icons/main/{mbti}.png", width=200)
