import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 1. INJECT CUSTOM CSS FOR STYLING
st.markdown("""
    <style>
    /* Change background color of the main app */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }
    
    /* Style the main headings */
    h1 {
        color: #f472b6 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        text-shadow: 0px 4px 12px rgba(244, 114, 182, 0.3);
    }
    
    h3 {
        color: #38bdf8 !important;
        font-weight: 600;
    }
    
    /* Style the selection radio buttons */
    .stRadio [data-testid="stMarkdownContainer"] p {
        font-size: 18px;
        font-weight: bold;
        color: #e2e8f0;
    }
    
    /* Create a beautiful custom card design for inputs and results */
    div[data-testid="stBlock"] {
        background: rgba(255, 255, 255, 0.04);
        padding: 25px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(8px);
        margin-bottom: 20px;
    }
    
    /* Custom design for the prediction success box */
    .stAlert {
        background-color: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid #10b981 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 2. APP LOGIC
st.title("🌸 Iris Flower Species Predictor")
st.write("An elegant, AI-powered web tool to classify Iris flower species instantly.")

# Input method toggle
input_method = st.radio("Choose Input Method:", ("Use Sliders", "Take a Photo with Camera"))

# Load dataset and train the model
iris = load_iris()
X = iris.data
y = iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

if input_method == "Use Sliders":
    st.subheader("🎚️ Adjust Flower Dimensions")
    sepal_length = st.slider("Sepal Length (cm)", 4.3, 7.9, 5.8)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.4, 3.0)
    petal_length = st.slider("Petal Length (cm)", 1.0, 6.9, 4.3)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)
    
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], 
                              columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
    
    st.subheader("📊 Your Input Measurements")
    st.write(input_data)
    
    prediction = model.predict(input_data)
    predicted_species = iris.target_names[prediction[0]]
    
    st.subheader("🎯 AI Prediction Result")
    st.success(f"The AI thinks this flower is a **{predicted_species.upper()}**!")

elif input_method == "Take a Photo with Camera":
    st.subheader("📸 Camera Capture")
    picture = st.camera_input("Take a picture of an Iris flower")
    
    if picture:
        st.image(picture, caption="Uploaded Image")
        st.info("✨ Image received successfully! Deep learning computer vision pipeline coming soon.")
