import streamlit as st
from img_classification import ultrasound_classification
from PIL import Image

image1 = Image.open(r'C:\Users\roaam\OneDrive\Desktop\brca\BreastCancerDetection main\app\pages\figure9.png')

detection = st.container()
with detection:
    st.subheader(' Detection using Ultrasound Screenings')
    st.image(image1)
    uploaded_file = st.file_uploader("Upload an ultrasound screening", type=("png","jpg", "jpeg"))
    if uploaded_file is not None:
           image = Image.open(uploaded_file).convert('RGB')
           st.image(image, caption='Uploaded Scan.', use_column_width=True)
           st.write("")
           st.write("Classifying...")
           label = ultrasound_classification(image, 'models/ultrasound/ultrasound_model.h5')
           if label == 0:
               st.write("The scan is normal and is free from any tumors")
           elif label == 1:
               st.write("The scan has a malignant tumor")
           else:
               st.write("The scan has a benign tumor")

