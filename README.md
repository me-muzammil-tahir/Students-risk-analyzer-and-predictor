# 🎓 Students Risk Analyzer & Predictor

A Data Science Semeter project that analyzes and predicts student academic risk levels using machine learning.
This project is based on synthetic but realistic data from **Sarhad University of Science and Information Technology, Peshawar**.

---

## 📌 Project Overview

This project aims to identify students who are at academic risk by analyzing factors such as:

* Attendance
* Study hours
* GPA & CGPA
* Sleep patterns
* Social media usage
* Academic scores

The system predicts whether a student is at **Low, Medium, or High Risk** and helps in early intervention.

---

## 🎯 Objectives

* Analyze student performance trends
* Identify key factors affecting academic success
* Predict student risk levels using machine learning
* Provide an interactive dashboard for visualization

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Streamlit
* Joblib

---

## 📂 Project Structure

```
📁 project-folder
│
├── sarhdad_Uni_data1.csv        # Dataset
├── project.ipynb                # Data analysis & model training
├── dashboard.py                 # Streamlit dashboard
├── student_risk_model.pkl       # Trained ML model
├── label_encoder.pkl            # Label encoder
├── README.md                    # Project documentation
```

---

## 📊 Dataset Description

The dataset contains student records from multiple departments of Sarhad University.

### Key Columns

* department
* attendance_percentage
* study_hours_per_day
* previous_semester_gpa
* current_cgpa
* assignments_score
* midterm_marks
* final_exam_marks
* sleep_hours
* social_media_hours
* hostel_resident
* risk_level (Target Variable)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/student-risk-analyzer.git
cd student-risk-analyzer
```

---

### 2️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib streamlit scikit-learn joblib
```

---

## ▶️ How to Run the Project

Make sure all project files are in the same folder.

### Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser.

---

## 🖥️ Dashboard Features

* User inputs student data
* Predicts student risk level
* Displays performance insights
* Helps identify at-risk students


---

## 📈 Machine Learning Model

The project uses a **Random Forest Classifier** to predict student risk levels.

### Why Random Forest?

* Handles complex relationships
* Works well with mixed data
* High accuracy & robustness

---

## 🔍 Key Insights

* Low attendance strongly correlates with high risk
* Excessive social media usage impacts performance
* Higher GPA reduces academic risk
* Hostel residents show better attendance trends

---

## 🚀 Future Improvements

* Add real-time university data integration
* Department-wise dashboards
* Early warning notification system
* Mobile-friendly interface

---

## 👨‍💻 Author

**Muzammil Tahir**
Software Engineering Student
AI Engineering Enthusiast

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and share your feedback!
