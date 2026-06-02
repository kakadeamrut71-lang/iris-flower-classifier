import streamlit as st

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

# 2. INITIALIZE SESSION STATE (To remember if you are logged in)
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_role" not in st.session_state:
    st.session_state["user_role"] = None

# 3. LOGIN INTERFACE
if not st.session_state["logged_in"]:
    st.title("🔐 Secure AI Portal Login")
    st.write("Please enter your credentials to unlock the Iris Predictor application.")
    
    # Login Form Box
    with st.container():
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Log In")
        
        if login_button:
            # Check for Admin
            if username == "admin" and password == "admin123":
                st.session_state["logged_in"] = True
                st.session_state["user_role"] = "admin"
                st.rerun()
            # Check for Regular User
            elif username == "user" and password == "user123":
                st.session_state["logged_in"] = True
                st.session_state["user_role"] = "user"
                st.rerun()
            else:
                st.error("Invalid Username or Password. Please try again.")

# 4. SUCCESS STATE (WHAT HAPPENS AFTER LOGIN)
else:
    st.sidebar.title("Navigation Menu")
    
    # Dynamic navigation based on role
    if st.session_state["user_role"] == "admin":
        page = st.sidebar.radio("Go to:", ["ℹ️ About Us", "🌸 AI Predictor", "🛠️ Admin Dashboard"])
    else:
        page = st.sidebar.radio("Go to:", ["ℹ️ About Us", "🌸 AI Predictor"])
        
    # Logout button at the bottom of the sidebar
    if st.sidebar.button("Log Out"):
        st.session_state["logged_in"] = False
        st.session_state["user_role"] = None
        st.rerun()

    # Placeholders for our next steps
    if page == "ℹ️ About Us":
        st.title("ℹ️ About Us")
        st.write("Login successful! This is where your stylish profile page will go.")
        
    elif page == "🌸 AI Predictor":
        st.title("🌸 AI Predictor")
        st.write("This is where your sliders and camera scanner will live.")
        
    elif page == "🛠️ Admin Dashboard":
        st.title("🛠️ Private Admin Dashboard")
        st.write("Welcome, Boss! This page is hidden from regular users and belongs only to you.")
