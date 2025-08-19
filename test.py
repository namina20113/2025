import streamlit as st
import random

st.title("🎧 고등학교 공부 분위기 노래 추천 앱")

# 과목 선택
subject = st.selectbox("공부할 과목을 선택하세요:", [
    "국어", "영어", "수학", "물리", "화학", "생물", "지구과학",
    "한국사", "세계사", "지리", "생활과 윤리", "윤리", "정치와 법", "기타"
])

# 책/자료 입력
book = st.text_input("공부할 책이나 자료를 입력하세요 (선택 사항):")

# 공부 분위기 선택
mood = st.selectbox("공부 분위기를 선택하세요:", [
    "집중", "편안함", "에너지", "감성", "차분함", "활기참", "긴장감", "몽환적", "상쾌함", "우울함"
])

# 색상/아이콘 매칭
subject_style = {
    "국어": ("📖", "#FFD700"),
    "영어": ("📝", "#1E90FF"),
    "수학": ("📐", "#00BFFF"),
    "물리": ("⚛️", "#7FFFD4"),
    "화학": ("🧪", "#FF69B4"),
    "생물": ("🌿", "#32CD32"),
    "지구과학": ("🌎", "#20B2AA"),
    "한국사": ("🏯", "#CD853F"),
    "세계사": ("🌍", "#8B4513"),
    "지리": ("🗺️", "#DAA520"),
    "생활과 윤리": ("🤔", "#FFB6C1"),
    "윤리": ("🕊️", "#9370DB"),
    "정치와 법": ("⚖️", "#DC143C"),
    "기타": ("🎵", "#808080")
}

icon, color = subject_style.get(subject, ("🎵", "#808080"))

# 추천곡 (가수+제목)
base_songs = {
    "국어": ["아이유 - 밤편지", "태연 - Fine", "Ed Sheeran - Perfect", "Adele - Hello"],
    "영어": ["Taylor Swift - Lover", "BTS - Dynamite", "BLACKPINK - How You Like That"],
    "수학": ["Red Velvet - Psycho", "EXO - Love Shot", "Coldplay - Clocks"],
    "물리": ["SHINee - View", "TWICE - Fancy", "Imagine Dragons - Believer"],
    "화학": ["BTS - Life Goes On", "SEVENTEEN - Left & Right", "Dua Lipa - Levitating"],
    "생물": ["IU - Palette", "BLACKPINK - Lovesick Girls", "Ed Sheeran - Shape of You"],
    "지구과학": ["BTS - Spring Day", "Red Velvet - Red Flavor", "Coldplay - Higher Power"],
    "한국사": ["BIGBANG - BANG BANG BANG", "EXO - Call Me Baby", "Adele - Rolling in the Deep"],
    "세계사": ["BTS - Not Today", "TWICE - Yes or Yes", "Imagine Dragons - Radioactive"],
    "지리": ["BLACKPINK - Kill This Love", "IU - Blueming", "Coldplay - Viva La Vida"],
    "생활과 윤리": ["Red Velvet - Rookie", "BTS - Permission to Dance", "Dua Lipa - Don't Start Now"],
    "윤리": ["SHINee - Sherlock", "TWICE - Signal", "Maroon 5 - Sugar"],
    "정치와 법": ["BIGBANG - Fantastic Baby", "EXO - Power", "Coldplay - Fix You"],
    "기타": ["BTS - Boy With Luv", "BLACKPINK - DDU-DU DDU-DU", "Ed Sheeran - Photograph"]
}

mood_songs = {
    "집중": ["BTS - Blue & Grey", "IU - Eight"],
    "편안함": ["TWICE - What is Love?", "Red Velvet - One of These Nights"],
    "에너지": ["BTS - Fire", "BLACKPINK - DDU-DU DDU-DU"],
    "감성": ["IU - Love Poem", "Taeyeon - 11:11"],
    "차분함": ["EXO - Universe", "Red Velvet - Automatic"],
    "활기참": ["BTS - Dynamite", "TWICE - Cheer Up"],
    "긴장감": ["BIGBANG - Loser", "BLACKPINK - Kill This Love"],
    "몽환적": ["IU - Palette", "SHINee - Married to the Music"],
    "상쾌함": ["TWICE - Alcohol-Free", "Red Velvet - Red Flavor"],
    "우울함": ["Taeyeon - Fine", "IU - Through the Night"]
}

def recommend_songs(subject, book, mood):
    songs = base_songs.get(subject, base_songs["기타"]) + mood_songs.get(mood, [])
    if book:
        songs.append(f"{book} 테마 플레이리스트")
    return random.sample(songs, min(5, len(songs)))

# 추천 결과
if st.button("추천 노래 보기"):
    songs = recommend_songs(subject, book, mood)
    st.markdown(f"### {icon} 오늘의 테마: {subject} + {mood} 🎨")
    for song in songs:
        # 간단한 창의적 설명 추가
        st.write(f"- {song} — '{mood} 분위기와 어울려요'")
