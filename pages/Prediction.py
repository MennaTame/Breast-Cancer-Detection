import streamlit as st
import pandas as pd 
import seaborn as sn 
import numpy as np 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt



st.header("Prediction Using Biopsy Results")
st.write("With advancements in artificial intelligence and machine learning, researchers aim to unlock intricate patterns within biopsy data, offering a more nuanced understanding of breast cancer subtypes, prognosis, and treatment responses. This intersection of medicine and technology holds promise for personalized and targeted approaches, ultimately paving the way for a future where early detection becomes a life-saving reality.")
radius_mean = st.slider("Radius mean", min_value=5.0, max_value=30.0, step=0.01)
texture_mean = st.slider("Texture mean", min_value=5.0, max_value=30.0, step=0.01)
perimeter_mean = st.slider("Perimeter mean", min_value=50.0, max_value=150.0, step=0.1)
area_mean = st.slider("Area mean", min_value=100.0, max_value=1500.0, step=0.5)
smoothness_mean = st.slider("Smoothness mean", min_value=0.0, max_value=1.0, step=0.00001)
compactness_mean = st.slider("Compactness mean", min_value=0.0, max_value=1.0, step=0.00001)
concavity_mean = st.slider("Concavity mean", min_value=0.0, max_value=1.0, step=0.00001)
concave_points_mean = st.slider("Concave points mean", min_value=0.0,  max_value=1.0, step=0.00001)
symmetry_mean = st.slider("Symmetry mean", min_value=0.0, max_value=1.0, step=0.00001)
fractal_dim_mean = st.slider("Fractal dimension mean", min_value=0.0, max_value=1.0, step=0.00001)

smoothness_mean = float(smoothness_mean)
compactness_mean = float(compactness_mean)
concavity_mean = float(concavity_mean)
concave_points_mean = float(concave_points_mean)
symmetry_mean = float(symmetry_mean)
fractal_dim_mean = float(fractal_dim_mean)

df = pd.read_csv('brca.csv')

lb = LabelEncoder()

df.iloc[:, 31] = lb.fit_transform(df.iloc[:, 31].values)

X = df.iloc[:, 1:11]
Y = df['y']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
Y_train = Y_train.astype(float)




ss = StandardScaler()

X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

svm_model = SVC(random_state=42)
svm_model.fit(X_train, Y_train)
svm_predictions = svm_model.predict(X_test)
Y_test = Y_test.astype(float)
svm_accuracy = accuracy_score(Y_test, svm_predictions)
svm_report = classification_report(Y_test, svm_predictions)

def predict_cancer_svm(model, sample):
    sample = ss.transform(sample.reshape(1, -1))
    prediction = model.predict(sample)
    probability = model.decision_function(sample)
    return prediction, probability

user_input_svm = []
user_input_svm.append(radius_mean)
user_input_svm.append(texture_mean)
user_input_svm.append(perimeter_mean)
user_input_svm.append(area_mean)
user_input_svm.append(smoothness_mean)
user_input_svm.append(compactness_mean)
user_input_svm.append(concavity_mean)
user_input_svm.append(concave_points_mean)
user_input_svm.append(symmetry_mean)
user_input_svm.append(fractal_dim_mean)

user_input_svm = np.array(user_input_svm)

prediction_svm, probability_svm = predict_cancer_svm(svm_model, user_input_svm)

if prediction_svm[0] == 0:
    result_svm = "Benign"
else:
    result_svm = "Malignant"

if st.button('Predict'):
    st.write(result_svm)