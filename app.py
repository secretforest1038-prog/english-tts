import streamlit as st
from gtts import gTTS
import base64

st.set_page_config(page_title="중학교 영어 발음 도우미", page_icon="🔊")

# 스타일링 (선택 사항: 학교 느낌 나게 배경색 등 조절 가능)
st.title("🏫 English Pronunciation Helper")
st.write("문장을 입력하고 아래 재생 버튼을 눌러보세요!")

text = st.text_input("Enter English sentences here:", placeholder="Hello, I'm glad to see you.")

if text:
    with st.spinner('발음을 생성 중입니다...'):
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        
        with open("speech.mp3", "rb") as f:
            audio_bytes = f.read()
        
        st.audio(audio_bytes, format="audio/mp3")
        st.balloons() # 축하 효과 (학생들이 좋아합니다!)