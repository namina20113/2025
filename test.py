import streamlit as st
import random

st.title("📚 고등학교 공부 노래 추천 ")

# 1️⃣ 과목 선택
subject = st.selectbox("공부할 과목을 선택하세요:", [
    "국어", "영어", "수학", "물리", "화학", "생물", "지구과학",
    "한국사", "세계사", "지리", "생활과 윤리", "윤리", "정치와 법", "기타"
])

# 2️⃣ 책/자료 입력
book = st.text_input("읽을 책이나 공부하는 자료를 입력하세요 (선택 사항):")

# 3️⃣ 공부 분위기 선택
mood = st.selectbox("공부 분위기를 선택하세요:", [
    "집중", "편안함", "에너지", "감성", "차분함", "활기참", "긴장감", "몽환적", "상쾌함", "우울함"
])

# 과목별 추천곡 (K-팝/팝 위주)
base_songs = {
    "국어": ["아이유 - 밤편지", "태연 - Fine", "Ed Sheeran - Perfect", "Adele - Hello"],
    "영어": ["Taylor Swift - Lover", "Justin Bieber - Peaches", "BTS - Dynamite", "BLACKPINK - How You Like That"],
    "수학": ["Red Velvet - Psycho", "EXO - Love Shot", "Coldplay - Clocks", "Maroon 5 - Memories"],
    "물리": ["SHINee - View", "TWICE - Fancy", "Imagine Dragons - Believer", "The Weeknd - Blinding Lights"],
    "화학": ["BTS - Life Goes On", "SEVENTEEN - Left & Right", "Dua Lipa - Levitating", "Ariana Grande - Positions"],
    "생물": ["IU - Palette", "BLACKPINK - Lovesick Girls", "Ed Sheeran - Shape of You", "Billie Eilish - Ocean Eyes"],
    "지구과학": ["BTS - Spring Day", "Red Velvet - Red Flavor", "Coldplay - Higher Power", "Maroon 5 - Girls Like You"],
    "한국사": ["BIGBANG - BANG BANG BANG", "EXO - Call Me Baby", "Adele - Rolling in the Deep", "Bruno Mars - Just the Way You Are"],
    "세계사": ["BTS - Not Today", "TWICE - Yes or Yes", "Imagine Dragons - Radioactive", "Lady Gaga - Poker Face"],
    "지리": ["BLACKPINK - Kill This Love", "IU - Blueming", "Coldplay - Viva La Vida", "Ed Sheeran - Bad Habits"],
    "생활과 윤리": ["Red Velvet - Rookie", "BTS - Permission to Dance", "Dua Lipa - Don't Start Now", "Ariana Grande - 34+35"],
    "윤리": ["SHINee - Sherlock", "TWICE - Signal", "Maroon 5 - Sugar", "The Weeknd - Save Your Tears"],
    "정치와 법": ["BIGBANG - Fantastic Baby", "EXO - Power", "Coldplay - Fix You", "Adele - Send My Love"],
    "기타": ["BTS - Boy With Luv", "BLACKPINK - DDU-DU DDU-DU", "Ed Sheeran - Photograph", "Taylor Swift - Shake It Off"]
}

# 분위기별 추천곡 (K-팝/팝)
mood_songs = {
    "집중": ["BTS - Blue & Grey", "IU - Eight", "Coldplay - Adventure of a Lifetime", "Adele - Easy on Me"],
    "편안함": ["TWICE - What is Love?", "Red Velvet - One of These Nights", "Ed Sheeran - Perfect", "Billie Eilish - Everything I Wanted"],
    "에너지": ["BTS - Fire", "BLACKPINK - DDU-DU DDU-DU", "Dua Lipa - Physical", "Imagine Dragons - Thunder"],
    "감성": ["IU - Love Poem", "Taeyeon - 11:11", "Adele - Someone Like You", "Sam Smith - Stay With Me"],
    "차분함": ["EXO - Universe", "Red Velvet - Automatic", "Coldplay - The Scientist", "Ed Sheeran - Thinking Out Loud"],
    "활기참": ["BTS - Dynamite", "TWICE - Cheer Up", "Bruno Mars - Uptown Funk", "Taylor Swift - You Belong With Me"],
    "긴장감": ["BIGBANG - Loser", "BLACKPINK - Kill This Love", "Imagine Dragons - Believer", "Adele - Rolling in the Deep"],
    "몽환적": ["IU - Palette", "SHINee - Married to the Music", "Billie Eilish - Bury a Friend", "Coldplay - Midnight"],
    "상쾌함": ["TWICE - Alcohol-Free", "Red Velvet - Red Flavor", "Ed Sheeran - Shape of You", "Dua Lipa - Levitating"],
    "우울함": ["Taeyeon - Fine", "IU - Through the Night", "Adele - Hello", "Sam Smith - Too Good at Goodbyes"]
}

# 추천 함수
def recommend_songs(subject, book, mood):
    songs = base_songs.get(subject, base_songs["기타"]) + mood_songs.get(mood, [])
    if book:
        songs.append(f"{book} 테마 플레이리스트")
    return random.sample(songs, min(5, len(songs)))  # 최대 5곡 추천

# 추천 결과
if st.button("추천 노래 보기"):
    songs = recommend_songs(subject, book, mood)
    st.subheader("추천 노래 🎵")
    for song in songs:
        st.write(f"- {song}")


