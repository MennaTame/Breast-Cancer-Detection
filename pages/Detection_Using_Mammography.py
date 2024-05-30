import streamlit as st
from img_classification import mammography_classification
from PIL import Image      

image1 = Image.open(r'C:\Users\roaam\OneDrive\Desktop\brca\BreastCancerDetection main\app\pages\figure8.png') 
st.subheader(' Detection using Mammography Screenings')
st.image(image1)
uploaded_file = st.file_uploader("Upload an mammography screening", type="jpeg")
if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Scan.', use_column_width=True)
            st.write("")
            st.write("Classifying...")
            label = mammography_classification(image, 'models/mammogram/mamography_model.h5')
            if label == 0:
                st.write("The scan has a benign tumor")
            elif label == 1:
                st.write("The scan has a malignant tumor")
            else:
                st.write("Couldn't verify image.")