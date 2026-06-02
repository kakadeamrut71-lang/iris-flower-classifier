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
    .profile-card, .predictor-card {
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
    .stAlert {
        background-color: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid #10b981 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 2. INITIALIZE SESSION STATE & TRAIN MODEL DATA
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user_role" not in st.session_state:
    st.session_state["user_role"] = None
if "prediction_history" not in st.session_state:
    st.session_state["prediction_history"] = []

# Load Iris Dataset and Train standard model
iris = load_iris()
X = iris.data
y = iris.target
feature_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
model = LogisticRegression(max_iter=200)
model.fit(X, y)

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
        
    # --- PAGE 2: CORE AI PREDICTOR (SLIDERS & CAMERA) ---
    elif page == "🌸 AI Predictor":
        st.title("🌸 AI Predictor Dashboard")
        
        # Split options using tabs inside the dashboard
        tab1, tab2 = st.tabs(["🎚️ Measurement Sliders", "📸 Live Camera Scanner"])
        
        with tab1:
            st.write("Move the sliders to input custom dimensions:")
            sepal_length = st.slider("Sepal Length (cm)", 4.3, 7.9, 5.8)
            sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.4, 3.0)
            petal_length = st.slider("Petal Length (cm)", 1.0, 6.9, 4.3)
            petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)
            
            # Form processing
            input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=feature_names)
            
            st.markdown('<div class="predictor-card">', unsafe_allow_html=True)
            st.subheader("📊 Selected Dimensions Frame")
            st.write(input_data)
            
            # Predict
            prediction = model.predict(input_data)
            predicted_species = iris.target_names[prediction[0]].upper()
            
            st.subheader("🎯 Classification Output")
            st.success(f"The AI thinks this flower is a **{predicted_species}**!")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Save logs to history tracking state for Admin
            if st.button("Log Prediction to Logs"):
                log_entry = {"Type": "Slider Input", "Result": predicted_species, "Data": f"{sepal_length}, {sepal_width}, {petal_length}, {petal_width}"}
                st.session_state["prediction_history"].append(log_entry)
                st.toast("Saved to system logs!")

        with tab2:
            st.write("Capture a raw botanical specimen image via camera:")
            picture = st.camera_input("Take a photo of an Iris flower")
            
            if picture:
                st.image(picture, caption="Uploaded Image Stream")
                st.info("✨ Image matrix captured successfully! CNN deep learning classification coming soon.")
                
                # Save logs to history tracking state for Admin
                if st.button("Log Snapshot to Logs"):
                    log_entry = {"Type": "Camera Snapshot", "Result": "PENDING_CNN_IMAGE", "Data": "Raw Image Matrix"}
                    st.session_state["prediction_history"].append(log_entry)
                    st.toast("Saved photo event to logs!")
        
    # --- PLACEHOLDER FOR FINAL STEP ---
    elif page == "🛠️ Admin Dashboard":
        st.title("🛠️ Private Admin System panel")
        st.warning("Step 4 will insert your restricted administrative tracking frames right here!")
