import streamlit as st
import moviepy.editor
from tkinter.filedialog import *
import tkinter as tk
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from moviepy.editor import *


def app(lang):
    
    window = tk.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    st.title("Video Translator")
    if st.button("Click to select & Translate"):
        vid=askopenfilename(parent=window,title="Select File")
        with st.spinner('Wait for it we are translating.......'):
            video = moviepy.editor.VideoFileClip(vid)
            video.audio.write_audiofile("vid_aud.wav")
            audio_file = "vid_aud.wav"
            r=sr.Recognizer()
            with sr.AudioFile("vid_aud.wav") as source :
                audio_data= r.record(source)
                text=r.recognize_google(audio_data)
                translated = GoogleTranslator(source='auto', target=lang).translate(text)
                myobj = gTTS(text=translated, lang=lang,slow=False)
                myobj.save("translated.mp3")
            
                audio_file = open('translated.mp3', 'rb')
        
                videoclip = VideoFileClip(vid)
                audioclip = AudioFileClip("translated.mp3")
        
                new_audioclip = CompositeAudioClip([audioclip])
                videoclip.audio = new_audioclip
                videoclip.write_videofile("new_filename.mp4")

                video_file = open("new_filename.mp4", 'rb')
                video_bytes = video_file.read()

                st.video(video_bytes)
                st.write(translated)
  
        

        st.success("Done")
        
