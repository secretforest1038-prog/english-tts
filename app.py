import streamlit as st
from gtts import gTTS
import base64

st.set_page_config(page_title="중학교 영어 발음 도우미", page_icon="🔊")

st.title("🏫 Kumgok Middle School English Class")
st.write("문장을 입력하고 아래 재생 버튼을 눌러보세요!")

text = st.text_input("Enter English sentences here:", placeholder="Hello, I'm glad to see you.")

if text:
    with st.spinner('발음을 생성 중입니다...'):
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        
        with open("speech.mp3", "rb") as f:
            audio_bytes = f.read()
        
        st.audio(audio_bytes, format="audio/mp3")
        st.balloons()