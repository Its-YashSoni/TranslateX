import streamlit as st
from streamlit_option_menu import option_menu
import video
import audio
import image
import pdf
import record

from deep_translator import GoogleTranslator

st.set_page_config(
        page_title="Translator",
        layout="centered"
)

class MultiApp:
    translated=""

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })
 


    def run():
        # app = st.sidebar(
        translated=""
        
        
        with st.sidebar:        
            app = option_menu(
                menu_title='MENU',
                options=['Text','Audio','Video','Image','pdf',"Record"],
                default_index=0,
                
                )
            lang = st.radio(
                "Select Language",
                 ["English", "Hindi", "Gujrati","Telugu","Bengali"],horizontal=True)
            
          
            
            if lang=="English":
                    lang='en'
            elif lang=="Hindi":
                    lang='hi'
            elif lang=="Gujrati":
                    lang='gu'
            elif lang=="Telugu":
                    lang='te'
            elif lang=="Bengali":
                 lang="bn"

         
            
            
    

            
        if app=="Text":

            st.title("Text Translator")
            input_text = st.text_area("Enter your text", height=180)

            if st.button("Translate", type="primary"):
                
                 
                translated = GoogleTranslator(source='auto', target=lang).translate(input_text)
        
            st.write("\n\nTranslated Text\n\n")
            st.write(translated)                
        
            
        if app=="Audio":
            audio.app(lang)
        if app=="Video":
            video.app(lang)
        if app=="Image":
            image.app(lang)
        if app=="pdf":
             pdf.app(lang)
        if app=="Record":
             record.app(lang)
             
                            
    run()