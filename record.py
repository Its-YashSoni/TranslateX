import streamlit as st
from streamlit_mic_recorder import mic_recorder,speech_to_text
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

def app(lang):
    
    state=st.session_state

    if 'text_received' not in state:
        state.text_received=[]
    c1,c2=st.columns(2)
    with c1:
        st.write("Convert speech to text:")
    with c2:
        
        text=speech_to_text(language='eng+hin',use_container_width=True,just_once=True,key='STT')

    if text:
        state.text_received.append(text)

    for text in state.text_received:
        st.write("Original text")
        st.text(text)
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
        myobj = gTTS(text=translated, tld='co.in', lang=lang,slow=False)
        myobj.save("translated.mp3")
            # os.system("mpg321 translated.mp3")
        st.write("Translated Text")
        st.write(translated)
        with st.spinner('Wait for it we are translating.......'):
            st.write("Translated Audio")
            audio_file = open('translated.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            st.success('Done!')


    st.write("Record your voice, and play the recorded audio:")
    audio=mic_recorder(start_prompt="⏺️",stop_prompt="⏹️",key='recorder')

    if audio:       
        st.audio(audio['bytes'])