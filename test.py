import streamlit as st
import random
import urllib.parse

# 앱 제목 꾸미기
st.markdown("""
<div style="text-align:center;">
    <h1 style="color:#6C63FF;">📚 공부 분위기 맞춤 노래 추천 🎶</h1>
    <p style="font-size:18px; color:gray;">과목과 분위기에 맞는 K-POP & POP 음악을 추천해드려요 ✨</p>
</div>
""", unsafe_allow_html=True)

# 1️⃣ 과목 선택
subject = st.selectbox("📖 공부할 과목을 선택하세요:", [
    "국어", "영어", "수학", "물리", "화학", "생물", "지구과학",
    "한국사", "세계사", "지리", "생활과 윤리", "윤리", "정치와 법", "기타"
])

# 2️⃣ 책/자료 입력
book = st.text_input("📕 공부할 책이나 자료를 입력하세요 (선택 사항):")

# 3️⃣ 분위기 선택
mood = st.selectbox("🌈 공부 분위기를 선택하세요:", [
    "집중", "편안함", "에너지", "감성", "차분함", "활기참", 
    "긴장감", "몽환적", "상쾌함", "우울함"
])

# 곡 설명
song_descriptions = [
    "잔잔한 멜로디가 특징이에요 🎧",
    "리듬감이 돋보여요 🥁",
    "감성적인 가사가 돋보여요 💜",
    "폭발적인 후렴구가 있어요 🔥",
    "몽환적인 분위기가 매력적이에요 🌌",
    "밝고 신나는 에너지가 넘쳐요 ✨",
    "차분히 흘러가는 멜로디가 좋아요 🌿",
    "강렬한 비트가 인상적이에요 ⚡"
]

# 랜덤 가사
lyrics_snippets = [
    "🎵 Cause I-I-I'm in the stars tonight (BTS - Dynamite)",
    "🎵 We don’t need permission to dance (BTS - Permission to Dance)",
    "🎵 Hello from the other side (Adele - Hello)",
    "🎵 Love is nothing stronger (BTS - Boy With Luv)",
    "🎵 We found love in a hopeless place (Rihanna - We Found Love)",
    "🎵 Baby, you light up my world like nobody else (One Direction - What Makes You Beautiful)",
    "🎵 널 기다리던 순간처럼 (아이유 - 밤편지)",
    "🎵 난 너의 손을 잡고서 함께 걷고 싶어 (볼빨간사춘기 - 우주를 줄게)",
]

# 오늘의 운세
study_fortune = [
    "📚 오늘은 집중력이 최고조에 달할 거예요! 작은 목표를 이루기에 딱 좋은 날입니다.",
    "🌟 새로운 아이디어가 떠오르기 쉬운 하루예요. 메모를 잊지 마세요!",
    "💡 차분히 복습하기에 적합한 날이에요. 조급함보단 꾸준함이 힘입니다.",
    "🔥 의욕이 넘치지만 무리하면 금방 지칠 수 있어요. 중간중간 쉬어가세요.",
    "🍀 오늘은 예상치 못한 곳에서 힌트를 얻을 수 있어요. 열린 마음으로 공부해보세요.",
    "✨ 평소보다 더 깊게 몰입할 수 있는 하루예요. 어려운 문제에 도전해도 좋아요!",
    "🌙 감성이 풍부해지는 날이에요. 인문학적 과목 공부에 특히 잘 어울려요.",
]

# 과목별 곡 데이터 (일부 예시)
song_library = {
    "국어": ["아이유 - 밤편지", "태연 - Fine", "Ed Sheeran - Perfect", "볼빨간사춘기 - 우주를 줄게"],
    "영어": ["Taylor Swift - Lover", "BTS - Dynamite", "BLACKPINK - How You Like That", "Maroon 5 - Memories"],
    "수학": ["Red Velvet - Psycho", "EXO - Love Shot", "Coldplay - Clocks", "방탄소년단 - Black Swan"],
    "물리": ["Imagine Dragons - Believer", "SHINee - View", "TWICE - Fancy", "Ariana Grande - No Tears Left to Cry"],
    "화학": ["Dua Lipa - Levitating", "BTS - Life Goes On", "Ariana Grande - Positions", "세븐틴 - Left & Right"],
    "생물": ["IU - Palette", "BLACKPINK - Lovesick Girls", "Ed Sheeran - Shape of You", "AKMU - 어떻게 이별까지 사랑하겠어"],
    "지구과학": ["Coldplay - Higher Power", "BTS - Spring Day", "Red Velvet - Red Flavor", "태연 - Rain"],
    "한국사": ["BIGBANG - BANG BANG BANG", "EXO - Call Me Baby", "Adele - Rolling in the Deep", "방탄소년단 - Not Today"],
    "세계사": ["Imagine Dragons - Radioactive", "TWICE - Yes or Yes", "BTS - ON", "Shawn Mendes - Senorita"],
    "지리": ["Coldplay - Viva La Vida", "BLACKPINK - Kill This Love", "IU - Blueming", "Maroon 5 - Sugar"],
    "생활과 윤리": ["BTS - Permission to Dance", "Red Velvet - Rookie", "Dua Lipa - Don't Start Now", "아이유 - 이름에게"],
    "윤리": ["Maroon 5 - Beautiful Mistakes", "SHINee - Sherlock", "TWICE - Signal", "방탄소년단 - Epiphany"],
    "정치와 법": ["BIGBANG - Fantastic Baby", "EXO - Power", "Coldplay - Fix You", "BTS - ON"],
    "기타": ["BTS - Boy With Luv", "BLACKPINK - DDU-DU DDU-DU", "Ed Sheeran - Photograph", "TWICE - Dance the Night Away"]
}

# 추천 함수
def recommend_songs(subject, book):
    base = song_library.get(subject, song_library["기타"])
    picks = random.sample(base, min(random.randint(3, 5), len(base)))
    if book:
        picks.append(f"{book} 테마 플레이리스트")
    return picks

# 버튼 클릭 시 결과
if st.button("✨ 추천 노래 보기 ✨"):
    picks = recommend_songs(subject, book)

    # 제목 꾸미기
    st.markdown(f"""
    ---
    <div style="text-align:center; background-color:#F0F0FF; padding:15px; border-radius:10px;">
        <h2 style="color:#6C63FF;">🎶 오늘의 테마</h2>
        <h3>{subject} + {mood}</h3>
    </div>
    """, unsafe_allow_html=True)

    # 곡 출력
    for song in picks:
        sdesc = random.choice(song_descriptions)
        query = urllib.parse.quote(song)
        yt_link = f"https://www.youtube.com/results?search_query={query}"
        st.markdown(f"""
        <div style="padding:8px; margin:6px 0; border-left:5px solid #6C63FF; background:#FAFAFF;">
            <b><a href="{yt_link}" target="_blank" style="text-decoration:none; color:#333;">{song}</a></b><br>
            <span style="color:gray;">{sdesc}</span>
        </div>
        """, unsafe_allow_html=True)

    # 랜덤 가사
    st.markdown(f"""
    ---
    <div style="background:#FFF8E1; padding:10px; border-radius:8px; margin-top:15px;">
        <h4>🎵 랜덤 가사 한 줄</h4>
        <p style="font-style:italic;">{random.choice(lyrics_snippets)}</p>
    </div>
    """, unsafe_allow_html=True)

    # 오늘의 운세
    st.markdown(f"""
    <div style="background:#E8F5E9; padding:10px; border-radius:8px; margin-top:15px;">
        <h4>🔮 오늘의 공부 운세</h4>
        <p>{random.choice(study_fortune)}</p>
    </div>
    """, unsafe_allow_html=True)

