import streamlit as st
from PIL import Image
import pytesseract
from deep_translator import GoogleTranslator
from tkinter.filedialog import *
import tkinter as tk

def app(lang):

    window = tk.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    st.title("Image Translator")
    # Upload = st.file_uploader("upload your file")a
    if st.button("Click to Upload file to Translate................."):

        img=askopenfilename(parent=window,title="Select File")
        
        image = Image.open(img)
        st.image(image,"Original Image")
        pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        result = pytesseract.image_to_string(image, lang='eng+hin')
        
         
        translated = GoogleTranslator(source='auto', target=lang).translate(text=result)
        st.write("Translated Text")
        st.write(translated)
    
    
        
