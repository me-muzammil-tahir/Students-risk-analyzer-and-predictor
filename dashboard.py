import streamlit as st
import joblib
import pandas as pd
import numpy as np

# page config
st.set_page_config(page_title="Student Risk Counselor", page_icon="🎓", layout="wide")

# Loading the model and encoder
@st.cache_resource
def load_assets():
    model = joblib.load('student_risk_model.pkl')
    le = joblib.load('label_encoder.pkl')
    return model, le

try:
    model, le = load_assets()
except:
    st.error("Error: Model files not found! Please run the training script first.")

# sidebar inputs
st.sidebar.header("Student Data Input")
st.sidebar.write("Enter the details below:")

att = st.sidebar.slider("Attendance Percentage", 0, 100, 85)
std = st.sidebar.slider("Study Hours Per Day", 0, 15, 5)
prev_gpa = st.sidebar.number_input("Previous Semester GPA", 0.0, 4.0, 3.2)
curr_gpa = st.sidebar.number_input("Current CGPA", 0.0, 4.0, 3.4)
slp = st.sidebar.slider("Sleep Hours", 0, 12, 7)
soc = st.sidebar.slider("Social Media Usage (Hours)", 0, 15, 2)

# main page
st.title("AI Student Success Dashboard")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Analysis Result")

    if st.button("Predict Risk Level"):

        # Prediction Logic
        inputs = [[att, std, prev_gpa, curr_gpa, slp, soc]]
        res = model.predict(inputs)
        risk = le.inverse_transform(res)[0]

        # Display Result
        if risk == 'High Risk':
            st.error(f"### Result: {risk}")
        elif risk == 'Medium Risk':
            st.warning(f"### Result: {risk}")
        else:
            st.success(f"### Result: {risk}")

        # Critical GPA alert
        if curr_gpa < 2.5:
            st.error("⚠️ Critical GPA Level: Immediate improvement required!")

        # suggestions logic
        st.subheader("Suggestions")

        if risk == 'High Risk':
            st.write("**Urgent:** Consult with your academic advisor immediately.")
        elif risk == 'Medium Risk':
            st.write("**Warning:** You need to focus more on your weak areas.")
        else:
            st.write("**Great Job:** Maintain this consistency!")

        # Detailed Recommendations
        with st.expander("Show Detailed Recommendations"):

            if att < 75:
                st.write("- **Attendance:** Your attendance is below 75%. Try to attend more classes to avoid missing concepts.")

            if std < 4:
                st.write("- **Study Habits:** Increase your study time to at least 5 hours for better grades.")

            if soc > 4:
                st.write("- **Social Media:** Reduce screen time; it might be affecting your focus.")

            if slp < 6:
                st.write("- **Health:** You need more sleep. Aim for 7-8 hours to stay mentally sharp.")

            # GPA-based academic recommendations
            if prev_gpa < 2.7 or curr_gpa < 2.7:
                st.write("- **Academic Focus:** Your GPA is below optimal level. Focus on conceptual study instead of rote learning.")
                st.write("- **Revision Strategy:** Revise topics weekly and practice past papers.")
                st.write("- **Teacher Support:** Don't hesitate to ask teachers when concepts are unclear.")

            # Performance drop detection
            if curr_gpa < prev_gpa:
                st.write("- **Performance Drop Alert:** Your GPA has decreased. Analyze weak subjects and allocate more time to them.")

            # High GPA motivation
            if curr_gpa >= 3.5:
                st.write("- **Excellent Performance:** Maintain your strategy and consider helping peers to strengthen concepts.")

    # AI Study Plan Generator
    st.markdown("---")
    if st.button("Generate AI Study Plan"):
        st.subheader("Personalized Study Plan")

        plan = []

        # GPA-based planning
        if curr_gpa < 2.7:
            plan.append("• Focus on conceptual learning instead of memorization.")
            plan.append("• Spend extra time on core subjects daily.")

        if curr_gpa < prev_gpa:
            plan.append("• Review weak subjects from last semester.")
            plan.append("• Solve past papers to identify mistakes.")

        # Attendance improvement
        if att < 75:
            plan.append("• Revise topics covered in missed classes.")
            plan.append("• Borrow notes from classmates.")

        # Study hours improvement
        if std < 4:
            plan.append("• Increase study time to at least 5–6 hours daily.")
            plan.append("• Use Pomodoro technique (25 min study + 5 min break).")

        # Social media control
        if soc > 4:
            plan.append("• Limit social media to 1 hour per day.")
            plan.append("• Use app blockers during study time.")

        # Sleep improvement
        if slp < 6:
            plan.append("• Maintain a fixed sleep schedule (7–8 hours).")
            plan.append("• Avoid screens 30 minutes before bed.")

        # High performers
        if curr_gpa >= 3.5:
            plan.append("• Maintain consistency and revise weekly.")
            plan.append("• Help classmates — teaching strengthens concepts.")

        # Default plan if everything good
        if not plan:
            plan.append("• Maintain your current routine.")
            plan.append("• Revise weekly and set new academic goals.")

        # Display plan
        for item in plan:
            st.write(item)

        # Suggested daily schedule
        st.markdown("### 🗓 Suggested Daily Routine")
        st.write("""
        **Morning**
        - Review previous day topics (30 mins)
        - Attend classes actively
        
        **Afternoon**
        - 2–3 hour focused study session
        - Practice problems / coding
        
        **Evening**
        - Revise weak areas
        - Group study or discussion
        
        **Night**
        - Quick revision
        - Plan next day tasks
        """)

with col2:
    st.subheader("Performance Visualization")

    # Bar chart
    input_df = pd.DataFrame({
        'Category': ['Attendance', 'Study Hours', 'Sleep Hours', 'Social Media'],
        'Value': [att, std * 10, slp * 10, soc * 10]
    })
    st.bar_chart(input_df.set_index('Category'))

    st.info("Note: Study, Sleep, and Social Media hours are scaled by 10 for comparison with Attendance %.")

    # GPA Trend Chart
    st.subheader("GPA Trend")
    gpa_df = pd.DataFrame({
        'Semester': ['Previous', 'Current'],
        'GPA': [prev_gpa, curr_gpa]
    })
    st.line_chart(gpa_df.set_index('Semester'))

# footer
st.markdown("---")
st.caption("AI Student Risk Assessment System | Engine: Random Forest Classifier | Developed by Muzammil Tahir")
