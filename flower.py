import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 1. PREMIUM STYLING (HTML/CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }
    h1 {
        color: #f472b6 !important;
        font-weight: 800;
        text-align: center;
    }
    h2, h3 {
        color: #38bdf8 !important;
    }
    .profile-card, .predictor-card, .admin-card {
        background: rgba(255, 255, 255, 0.04);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    div[data-testid="stBlock"] {
        background: rgba(255, 255, 255, 0.04);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        max-width: 500px;
        margin: 0 auto;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #f472b6, #38bdf8);
        color: white;
        border: none;
        padding: 10px;
        font-weight: bold;
        border-radius: 8px;
    }
    /* Style for the internal form button */
    div[data-testid="stForm"] button {
        background: linear-gradient(90deg, #38bdf8, #f472b6) !important;
        color: white !important;
    }
    .stAlert {
        background-color: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid #10b981 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 2. INITIALIZE REGISTRY & SESSION STATES
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_role" not in st.session_state:
    st.session_state["user_role"] = None
if "prediction_history" not in st.session_state:
    st.session_state["prediction_history"] = [{"Type": "System Test", "Result": "SETOSA", "Inputs/Data": "5.1, 3.5, 1.4, 0.2"}]

# Custom Account Database Storage Setup
if "user_database" not in st.session_state:
    st.session_state["user_database"] = {
        "admin": {"password": "admin123", "role": "admin"},
        "user": {"password": "user123", "role": "user"}
    }

# Load Iris Dataset and Train standard model
iris = load_iris()
X = iris.data
y = iris.target
feature_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 3. LOGIN & SIGN-UP GATEWAY INTERFACE
if not st.session_state["logged_in"]:
    st.title("🔐 Secure AI Portal")
    
    auth_mode = st.radio("Choose Action:", ["Sign In to Account", "Create New Account (Sign Up)"], horizontal=True)
    
    with st.container():
        if auth_mode == "Sign In to Account":
            st.subheader("🔑 Sign In")
            username = st.text_input("Username").strip().lower()
            password = st.text_input("Password", type="password")
            login_button = st.button("Log In")
            
            if login_button:
                if username in st.session_state["user_database"]:
                    stored_password = st.session_state["user_database"][username]["password"]
                    stored_role = st.session_state["user_database"][username]["role"]
                    
                    if password == stored_password:
                        st.session_state["logged_in"] = True
                        st.session_state["user_role"] = stored_role
                        st.rerun()
                    else:
                        st.error("Incorrect password. Please try again.")
                else:
                    st.error("Username not found. Click 'Create New Account' above to sign up!")
                    
        else:
            st.subheader("📝 Register New Account")
            new_username = st.text_input("Choose a Username").strip().lower()
            new_password = st.text_input("Choose a Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            register_button = st.button("Register Account")
            
            if register_button:
                if not new_username or not new_password:
                    st.warning("Username and Password fields cannot be empty.")
                elif new_username in st.session_state["user_database"]:
                    st.error("That username is already taken! Try another one.")
                elif new_password != confirm_password:
                    st.error("Passwords do not match. Re-
