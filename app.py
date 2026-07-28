import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

body{
    background-color:#F4F8FB;
}

.main{
    background-color:#F4F8FB;
}

.header{
    background:#0F4C81;
    padding:25px;
    border-radius:15px;
    color:white;
    text-align:center;
    box-shadow:0px 5px 15px rgba(0,0,0,0.2);
}

.header h1{
    color:white;
    font-size:40px;
}

.header p{
    color:white;
    font-size:18px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.1);
}

.result-card{
    background:#E8F5E9;
    padding:25px;
    border-radius:15px;
    text-align:center;
    color:#155724;
    border:2px solid #28A745;
}

.result-card h2,
.result-card h3{
    color:#155724;
    margin:10px 0;
}

.danger-card{
    background:#FDECEC;
    padding:25px;
    border-radius:15px;
    text-align:center;
    color:#B71C1C;
    border:2px solid #DC3545;
}

.danger-card h2,
.danger-card h3{
    color:#B71C1C;
    margin:10px 0;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
    width=90
)

st.sidebar.title("🏥 About Project")

st.sidebar.markdown("""
### 👨‍⚕️ Model
Random Forest Classifier

---

### 📂 Dataset
Pima Indians Diabetes Dataset

---

### 🎯 Accuracy
**85%+**

---

### 🧠 Machine Learning Algorithms

- Logistic Regression
- Decision Tree
- Random Forest ✅
- KNN
- SVM

---

### 👨‍💻 Developed By

**Mohamed Halid**

B.Tech Information Technology

2026
""")

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class='header'>

<h1>🩺 Diabetes Prediction System For Womens</h1>

<p>
AI Powered Healthcare Assistant using Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Medical Disclaimer
# -----------------------------
st.warning("""
This application is developed for educational purposes.

It predicts diabetes using the **Pima Indians Diabetes Dataset**.

This tool should **not** be used as a substitute for professional medical diagnosis.
""")

st.write("")

# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([2.5,1])

# -----------------------------
# LEFT COLUMN
# -----------------------------
with left:

    st.subheader("📝 Patient Information")

    pregnancies = st.number_input(
        "Pregnancies (0 = Never Pregnant)",
        min_value=0,
        max_value=17,
        value=1
    )

    glucose = st.number_input(
        "Glucose Level (mg/dL)",
        min_value=50,
        max_value=250,
        value=120
    )

    blood_pressure = st.number_input(
        "Blood Pressure (mmHg)",
        min_value=1,
        max_value=800,
        value=70
    )

    skin = st.number_input(
        "Skin Thickness (mm)",
        min_value=7,
        max_value=99,
        value=20
    )

    insulin = st.number_input(
        "Insulin (0 = Not Measured)",
        min_value=0,
        max_value=846,
        value=80
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=25.0,
        step=0.1
    )

    pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=2.5,
        value=0.5,
        step=0.01
    )

    age = st.number_input(
        "Age",
        min_value=21,
        max_value=100,
        value=30
    )

# -----------------------------
# RIGHT COLUMN
# -----------------------------
with right:

    st.subheader("📊 Health Summary")

    st.metric("Age", age)

    st.metric("BMI", bmi)

    st.metric("Glucose", glucose)

    st.metric("Blood Pressure", blood_pressure)

    st.metric("Insulin", insulin)
    
# ==========================================
# Prediction Section
# ==========================================

st.write("")
st.markdown("---")

if st.button("🔍 Predict Diabetes", use_container_width=True):

    # Collect input data
    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin,
        insulin,
        bmi,
        pedigree,
        age
    ]])

    # Scale data
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Prediction probability
    probability = model.predict_proba(input_scaled)

    confidence = np.max(probability) * 100

    st.write("")

    col1, col2 = st.columns([2,1])

    # ==========================================
    # LEFT COLUMN
    # ==========================================

    with col1:

        st.subheader("🩺 Prediction Result")

        if prediction[0] == 1:

            st.markdown("""
            <div class='danger-card'>

            <h2>🔴 High Risk</h2>

            <h3>Patient is likely Diabetic</h3>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class='result-card'>

            <h2>🟢 Low Risk</h2>

            <h3>Patient is Non-Diabetic</h3>

            </div>
            """, unsafe_allow_html=True)

        st.write("")

        st.subheader("📈 Prediction Confidence")

        st.progress(int(confidence))

        st.success(f"Confidence : {confidence:.2f}%")
        
    # ==========================================
    # RIGHT COLUMN
    # ==========================================

    with col2:

        st.subheader("📊 Health Status")

        # BMI Category

        if bmi < 18.5:
            bmi_status = "Underweight"

        elif bmi < 25:
            bmi_status = "Normal"

        elif bmi < 30:
            bmi_status = "Overweight"

        else:
            bmi_status = "Obese"

        st.metric("BMI Status", bmi_status)

        # Glucose Status

        if glucose < 70:
            glucose_status = "Low"

        elif glucose <= 140:
            glucose_status = "Normal"

        else:
            glucose_status = "High"

        st.metric("Glucose", glucose_status)

        # Blood Pressure

        if blood_pressure < 80:
            bp_status = "Low"

        elif blood_pressure <= 120:
            bp_status = "Normal"

        else:
            bp_status = "High"

        st.metric("Blood Pressure", bp_status)

        # Risk Level

        if confidence >= 90:

            risk = "Very High"

        elif confidence >= 75:

            risk = "High"

        elif confidence >= 60:

            risk = "Moderate"

        else:

            risk = "Low"

        st.metric("Risk Level", risk)
        
    st.write("")
    st.markdown("---")

    st.subheader("📋 Patient Report")

    report = pd.DataFrame({

        "Parameter":[

            "Pregnancies",
            "Glucose",
            "Blood Pressure",
            "Skin Thickness",
            "Insulin",
            "BMI",
            "Pedigree",
            "Age",
            "Prediction",
            "Confidence"

        ],

        "Value":[

            pregnancies,
            glucose,
            blood_pressure,
            skin,
            insulin,
            bmi,
            pedigree,
            age,
            "Diabetic" if prediction[0]==1 else "Non-Diabetic",
            f"{confidence:.2f}%"

        ]

    })

    st.dataframe(report, use_container_width=True)

    csv = report.to_csv(index=False)

    st.download_button(

        "📥 Download Patient Report",

        data=csv,

        file_name="Patient_Report.csv",

        mime="text/csv"

    )

