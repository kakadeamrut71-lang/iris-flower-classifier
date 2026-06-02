import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Set up the web page title and description
st.set_page_config(page_title="Iris Flower Classifier", layout="centered")
st.title("🌸 Iris Flower Species Predictor")
st.write("Adjust the sliders below to input flower measurements and see the AI predict the species in real-time!")

# Load the data and train the model in the background
@st.cache_resource
def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model, iris.target_names

model, target_names = train_model()

# Create Sidebar Sliders for user input
st.sidebar.header("Input Features (in cm)")
sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.8)
sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 4.3)
petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 1.3)

# Display the user's inputs on the main page
st.subheader("Your Input Measurements:")
input_df = pd.DataFrame({
    'Sepal Length': [sepal_length],
    'Sepal Width': [sepal_width],
    'Petal Length': [petal_length],
    'Petal Width': [petal_width]
})
st.table(input_df)

# Make the prediction
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)
predicted_species = target_names[prediction[0]]

# Show the result proudly!
st.subheader("AI Prediction:")
st.success(f"The AI thinks this flower is a **{predicted_species.upper()}**!")
