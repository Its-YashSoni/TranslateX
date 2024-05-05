import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
from pydub import AudioSegment
def app(lang):
    st.title("Audio Translator")
    uploaded = st.file_uploader("Upload your Audio", type=["wav"], accept_multiple_files=False)
    translation=''
    def translate():
        r=sr.Recognizer()
        with sr.AudioFile(uploaded) as source:
            audio_data= r.record(source)
            text=r.recognize_google(audio_data)
            translated = GoogleTranslator(source='auto', target=lang).translate(text)
            myobj = gTTS(text=translated, lang=lang,slow=False)
            myobj.save("translated.mp3")
            # os.system("mpg321 translated.mp3")
            st.write("Translated Text")
            st.write(translated)
    
    if st.button("Translate"):
        import time
        with st.spinner('Wait for it we are translating.......'):
            translate()
            st.write("Translated Audio")
            audio_file = open('translated.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            st.success('Done!')

            audio = AudioSegment.from_mp3("translated.mp3")

    # Get the duration of the audio in milliseconds
            duration_ms = len(audio)

    # Print the timeline in seconds
            timeline_seconds = [t / 1000 for t in range(0, duration_ms, 1000)]
            print("Audio Timeline (seconds):", timeline_seconds)
        