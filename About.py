import streamlit as st
from PIL import Image


header = st.container()
intro1 = st.container()
intro2 = st.container()
intro3 = st.container()
symptoms = st.container()

image1 = Image.open('figure3.png')
image2 = Image.open('figure2.png')
image3 = Image.open('figure4.webp')
image4 = Image.open('figure7.jpg')
image5 = Image.open('breast-cancer-testing-screening-5204528_final3-d168aa62d78a4d3c93745dd056284c32.gif')

with header:
        st.title('Breast Cancer Detection')
    
with intro1:   
        st.subheader('World Breast Cancer Incidence Rates')
        st.write('According to a survey published by IARC, in 2010, the USA appears to have the highest incidence rate for breast cancer.')
        st.image(image1)
    

with intro2:
        st.subheader('Age increases the risk of breast cancer')
        st.write('The older we are, the more likely abnormal changes will occur in our cells. When many of these changes occur, cancer can develop.')
        st.image(image2)
    
with intro3:
        st.subheader('Breast Cancer Frequency')
        st.write('According to WHO Breast cancer is the most frequent cancer among women, impacting 2.1 million women each year, and also causes the greatest number of cancer-related deaths among women. In 2018, it is estimated that 627,000 women died from breast cancer – that is approximately 15% of all cancer deaths among women.')
        st.image(image3)
        
col1, col2 = st.columns(2)

with symptoms:
        with col1:
            st.subheader('Breast Cancer Symptoms')
            st.write('Breast cancer is a type of cancer that occurs when cells in the breast begin to grow uncontrollably. It can affect both women and men, although it is more common in women. One of the most important aspects of breast cancer is early detection, as this can greatly improve the chances of successful treatment and recovery. Knowing the symptoms of breast cancer is crucial for early detection, as it can help individuals identify any changes in their breasts or surrounding areas. Symptoms of breast cancer can include the presence of a lump or thickening in the breast or underarm area, changes in the size or shape of the breast, nipple changes such as nipple discharge or inversion, and skin changes such as redness, swelling, or dimpling. It is important to note that not all changes or lumps in the breast are cancerous, but it is always best to have any changes checked by a healthcare provider to ensure proper diagnosis and treatment.')

        with col2:
            st.image(image4)

st.image(image5)