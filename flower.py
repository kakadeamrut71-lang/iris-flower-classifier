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

# Core Local User Registry Map
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
                    st.error("Passwords do not match. Re-type carefully.")
                else:
                    st.session_state["user_database"][new_username] = {"password": new_password, "role": "user"}
                    st.success("🎉 Registration Complete! Select 'Sign In to Account' above to log in.")

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

    # --- PAGE 1: ABOUT US ---
    if page == "ℹ️ About Us":
        st.title("ℹ️ About the Project")
        st.image("https://images.unsplash.com/photo-1527489377706-5bf97e608852?auto=format&fit=crop&w=1200&q=80", 
                 caption="Data Science & Machine Learning in Botany", use_container_width=True)
        
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
        
    # --- PAGE 2: CORE AI PREDICTOR (FORM BUTTON FIX) ---
    elif page == "🌸 AI Predictor":
        st.title("🌸 AI Predictor Dashboard")
        tab1, tab2 = st.tabs(["🎚️ Measurement Sliders", "📸 Live Camera Scanner"])
        
        with tab1:
            with st.form("measurement_form"):
                st.write("Adjust the dimensions and click the button below to predict:")
                sepal_length = st.slider("Sepal Length (cm)", 4.3, 7.9, 5.8)
                sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.4, 3.0)
                petal_length = st.slider("Petal Length (cm)", 1.0, 6.9, 4.3)
                petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)
                
                submit_prediction = st.form_submit_button("🔍 Run AI Prediction")
            
            if submit_prediction:
                input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=feature_names)
                
                st.markdown('<div class="predictor-card">', unsafe_allow_html=True)
                st.subheader("📊 Evaluated Dimensions Frame")
                st.write(input_data)
                
                prediction = model.predict(input_data)
                predicted_species = iris.target_names[prediction[0]].upper()
                
                st.subheader("🎯 Classification Output")
                st.success(f"The AI thinks this flower is a **{predicted_species}**!")
                st.markdown('</div>', unsafe_allow_html=True)
                
                log_entry = {"Type": "Slider Input", "Result": predicted_species, "Inputs/Data": f"{sepal_length}, {sepal_width}, {petal_length}, {petal_width}"}
                st.session_state["prediction_history"].append(log_entry)
                st.toast("Result saved to admin system logs!")

        with tab2:
            st.write("Capture a raw botanical specimen image via camera:")
            picture = st.camera_input("Take a photo of an Iris flower")
            if picture:
                st.image(picture, caption="Uploaded Image Stream")
                st.info("✨ Image matrix captured successfully! CNN deep learning classification coming soon.")

    # --- PAGE 3: ADMIN DASHBOARD PANEL ---
    elif page == "🛠️ Admin Dashboard":
        st.title("🛠️ Private Admin System Panel")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Total Session Logs", value=len(st.session_state["prediction_history"]))
        with col2:
            st.metric(label="Registered Accounts Online", value=len(st.session_state["user_database"]))
            
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.subheader("👥 Registered Accounts Registry")
        users_df = pd.DataFrame.from_dict(st.session_state["user_database"], orient="index").reset_index()
        users_df.columns = ["Username", "Password (Plain)", "System Role"]
        st.dataframe(users_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.subheader("📋 Session Event Logging Tracking")
        if len(st.session_state["prediction_history"]) > 0:
            history_df = pd.DataFrame(st.session_state["prediction_history"])
            st.dataframe(history_df, use_container_width=True)
        else:
            st.info("Log index empty.")
        if st.button("Clear History Logs"):
            st.session_state["prediction_history"] = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
