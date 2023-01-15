import streamlit as st
import os 
import cv2 
import pandas as pd
from io import BytesIO, StringIO
from PIL import Image

def main():
    upload_file = st.file_uploader("Choose a file: ")
    
    if upload_file: 
        size = upload_file.getvalue()
        st.write(size)




    # img = Image.open(upload_file)
    # st.image(upload_file)

