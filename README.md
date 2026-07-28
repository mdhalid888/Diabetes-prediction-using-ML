🩺 Diabetes Prediction using Machine Learning

Live Model: https://diabetes-prediction-using-ml-h.streamlit.app/

A Machine Learning web application that predicts whether a patient is likely to have diabetes based on medical parameters. The application is built using **Python**, **Scikit-learn**, and **Streamlit**.

📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help doctors and patients take preventive measures and improve healthcare decisions.

This project uses the **Pima Indians Diabetes Dataset** to train multiple Machine Learning classification algorithms and predicts whether a patient is diabetic or non-diabetic.

🎯 Objectives

- Analyze the diabetes dataset.
- Perform data preprocessing and visualization.
- Train multiple Machine Learning models.
- Compare model performance.
- Select the best-performing model.
- Deploy the model using Streamlit.
- Provide an easy-to-use interface for diabetes prediction.

📂 Dataset

**Dataset Name:**
Pima Indians Diabetes Dataset

**Source:**
https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

Dataset Features

| Feature | Description |
|----------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes hereditary function |
| Age | Age of the patient |
| Outcome | 0 = Non-Diabetic, 1 = Diabetic |

⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

🧠 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Scaling using StandardScaler
5. Train-Test Split
6. Train Multiple Classification Models
7. Compare Accuracy
8. Select Best Model
9. Save Model
10. Deploy using Streamlit

🤖 Machine Learning Algorithms Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

🏆 Final Model

After evaluating all algorithms, **Random Forest Classifier** was selected because it provided the best overall performance and reliable predictions.

📊 Exploratory Data Analysis

The following visualizations were performed:

- Dataset Information
- Missing Value Analysis
- Statistical Summary
- Class Distribution
- Histograms
- Boxplots
- Correlation Heatmap

📁 Project Structure

```
Diabetes-Prediction/
│
├── app.py
├── diabetes.csv
├── diabetes_prediction.ipynb
├── random_forest_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Diabetes-Prediction.git
```

### Navigate to Project

```bash
cd Diabetes-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

💻 Application Features

- User-friendly interface
- Enter patient medical details
- Instant diabetes prediction
- Clean dashboard
- Fast prediction
- Machine Learning powered

📈 Model Input Features

The application accepts:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

🎯 Prediction Output

The application predicts:

- ✅ Non-Diabetic
- ⚠️ Diabetic

📷 Application Preview

(Add screenshots of your Streamlit application here.)

Example:

```
screenshots/home.png
screenshots/result.png
```

🔮 Future Enhancements

- Probability score for predictions
- PDF report generation
- Patient history management
- Cloud deployment
- Doctor dashboard
- Authentication system
- Mobile responsive interface

📚 Learning Outcomes

Through this project, I learned:

- Data preprocessing
- Feature scaling
- Data visualization
- Machine Learning model training
- Model evaluation
- Model deployment using Streamlit
- GitHub project management

👨‍💻 Author

**Mohamed Halid**

B.Tech Information Technology

📜 License

This project is developed for educational and academic purposes.
