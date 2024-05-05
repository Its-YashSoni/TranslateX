import streamlit as st
import PyPDF2
from tkinter.filedialog import *
import tkinter as tk
from deep_translator import GoogleTranslator

def app(lang):
    window = tk.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()
    texts=" "
    st.title("PDF Translator.........")
    if st.button("Click to upload PDF......."):
        pdf=askopenfilename(parent=window,title="Select File")

        file = open(pdf,'rb')
        reader = PyPDF2.PdfReader(file)
        num_pages = 2

        

        for p in range(num_pages):
            page = reader.pages[p]
            text = page.extract_text()
            texts = texts+text

        st.write(texts)

        translator = GoogleTranslator(source="auto", target=lang).translate(texts)


        st.write("Translated text")
        st.write(translator)
        
        
