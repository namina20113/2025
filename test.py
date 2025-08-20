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
     "📚 집중에 딱 맞는 곡이에요.",
    "🌙 마음이 편안해지는 노래예요.",
    "🔥 에너지가 필요할 때 좋아요.",
    "💡 머리를 맑게 해주는 음악이에요.",
    "☕ 책상에 앉아 있을 때 흐르면 좋은 노래예요.",
    "🎧 리듬이 공부 흐름을 깨우지 않아요.",
    "🌊 잔잔하게 흘러가면서 집중을 돕습니다.",
    "⚡ 열정이 필요할 때 기운을 주는 곡이에요.",
    "🎶 가사보다 멜로디에 빠져드는 음악이에요.",
    "🌌 새벽 공부와 어울리는 분위기예요.",
    "🏞️ 마치 카페에서 공부하는 느낌을 줘요.",
    "😌 긴장을 풀어주면서 몰입할 수 있게 해줍니다.",
    "🕰️ 공부의 리듬을 만들어 주는 곡이에요.",
    "🌱 차분하면서도 힘을 주는 노래예요.",
    "✍️ 듣고 있으면 글이 더 잘 읽혀요.",
    "🔒 혼자만의 집중 공간을 만들어줍니다.",
    "🎼 배경 음악처럼 흘러가기에 좋아요.",
    "📖 단어 암기할 때 집중을 유지하기 딱이에요.",
    "✨ 오늘 분위기와 잘 어울리는 곡이에요.",
    "🍀 지루함을 달래주는 상쾌한 음악이에요."
]

# 랜덤 가사
lyrics_snippets = [
     "BTS - Dynamite: 🎶 'Cause I, I, I'm in the stars tonight...",
    "Adele - Hello: 🎵 내 마음을 가득 채운 Story",
    "Ed Sheeran - Shape of You: 🎧 Love is all, love is you",
    "Imagine Dragons - Believer: 🎶 We could be heroes, just for one day",
    "아이유 - 밤편지: 🎵 밤하늘에 별빛처럼 스며드는 Melody",
    "Taylor Swift - Lover: 🎧 You make me feel like I'm living a teenage dream",
    "볼빨간사춘기 - 우주를 줄게: 🎶 너의 목소리가 내 하루를 비춰줘",
    "Coldplay - Viva La Vida: 🎵 Shining like the sun, you light up my world",
    "BLACKPINK - How You Like That: 🎧 흐르는 바람처럼 자유로운 순간",
    "Maroon 5 - Memories: 🎶 I just called to say I love you"
]

# 오늘의 운세
study_fortune = [
    "🎯 오늘은 집중력이 최고예요!",
    "🌟 작은 성취가 큰 기쁨으로 다가올 거예요.",
    "🎵 음악과 함께라면 효율이 배가됩니다.",
    "🚀 지금 시작하면 놀라운 몰입을 경험할 거예요.",
    "📈 꾸준히 하면 성적도 꾸준히 오를 거예요.",
    "💡 좋은 아이디어가 번뜩 떠오를 하루예요.",
    "🧠 오늘은 암기력이 특히 좋아질 거예요.",
    "⚡ 생각보다 빨리 진도를 나갈 수 있어요.",
    "🏆 힘들어도 끝까지 가면 성취감이 큽니다.",
    "🔎 새로운 관점으로 문제를 이해하게 돼요.",
    "✅ 작은 목표를 세우면 반드시 달성할 수 있습니다.",
    "🌈 노력의 결실이 조금씩 드러날 거예요.",
    "✍️ 오늘은 실수가 줄고 정답이 많아질 거예요.",
    "🛋️ 휴식과 공부의 균형이 잘 맞을 거예요.",
    "💪 자신감이 성적에 긍정적인 영향을 줄 거예요.",
    "🌞 오늘의 노력이 내일의 성과로 이어집니다.",
    "🔔 조금만 더 하면 원하는 만큼 해낼 수 있어요.",
    "🎉 공부가 의외로 재미있게 느껴질 수 있어요.",
    "🍀 운도 따라주니 실력이 더 잘 발휘돼요.",
    "⏳ 집중의 흐름이 오래 이어질 거예요."
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

