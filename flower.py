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
    /* Profile card container styling */
    .profile-card {
        background: rgba(255, 255, 255, 0.04);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    /* Login Form styling */
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
    </style>
""", unsafe_allow_html=True)

# 2. INITIALIZE SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_role" not in st.session_state:
    st.session_state["user_role"] = None

# 3. LOGIN INTERFACE
if not st.session_state["logged_in"]:
    st.title("🔐 Secure AI Portal Login")
    st.write("Please enter your credentials to unlock the Iris Predictor application.")
    
    with st.container():
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Log In")
        
        if login_button:
            if username == "admin" and password == "admin123":
                st.session_state["logged_in"] = True
                st.session_state["user_role"] = "admin"
                st.rerun()
            elif username == "user" and password == "user123":
                st.session_state["logged_in"] = True
                st.session_state["user_role"] = "user"
                st.rerun()
            else:
                st.error("Invalid Username or Password. Please try again.")

# 4. SECURE INNER FRAMEWORK
else:
    st.sidebar.title("Navigation Menu")
    if st.session_state["user_role"] == "admin":
        page = st.sidebar.radio("Go to:", ["ℹ️ About Us", "🌸 AI Predictor", "🛠️ Admin Dashboard"])
    else:
        page = st.sidebar.radio("Go to:", ["ℹ️ About Us", "🌸 AI Predictor"])
        
    if st.sidebar.button("Log Out"):
        st.session_state["logged_in"] = False
        st.session_state["user_role"] = None
        st.rerun()

    # --- BRAND NEW STYLISH ABOUT US PAGE ---
    if page == "ℹ️ About Us":
        st.title("ℹ️ About the Project")
        
        # Display a high-quality botanical data banner image
        st.image("https://images.unsplash.com/photo-1527489377706-5bf97e608852?auto=format&fit=crop&w=1200&q=80", 
                 caption="Data Science & Machine Learning in Botany", use_container_width=True)
        
        # Profile Card Section
        st.markdown("""
        <div class="profile-card">
            <h3>👨‍💻 Developer Profile</h3>
            <p style="font-size:18px; line-height:1.6; color:#cbd5e1;">
                Welcome to the <b>Iris Flower Species Predictor</b> web portal. This application was engineered 
                to showcase the practical deployment of Machine Learning models via cloud infrastructures.
            </p>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <p><b>Lead Developer:</b> Amrut Kakade</p>
            <p><b>Academic Track:</b> Master of Science (MSc) in Computer Science</p>
            <p><b>Institution:</b> Shivaji University, Kolhapur</p>
            <p><b>Core Stack:</b> Python, Scikit-Learn, Streamlit, Git, MySQL</p>
        </div>
        """, unsafe_allow_html=True)
        
    # --- PLACEHOLDERS FOR NEXT STEPS ---
    elif page == "🌸 AI Predictor":
        st.title("🌸 AI Predictor Dashboard")
        st.info("Step 3 will insert the multi-page Sliders and Live Camera tools right here!")
        
    elif page == "🛠️ Admin Dashboard":
        st.title("🛠️ Private Admin System panel")
        st.warning("Step 4 will insert your restricted administrative tracking frames right here!")
