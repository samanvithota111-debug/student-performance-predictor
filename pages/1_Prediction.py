import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Custom website styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .main-title {
        text-align: center;
        color: #173b6c;
        font-size: 38px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #5b6578;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .result-card {
        background-color: #e8f1ff;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #c6dcff;
    }

    .result-label {
        color: #173b6c;
        font-size: 20px;
    }

    .result-value {
        color: #174ea6;
        font-size: 42px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Load the trained model
model = joblib.load("student_model.pkl")
data = pd.read_csv("student-mat.csv", sep=";")

# Website heading
st.markdown(
    '<div class="main-title">🎓 Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based Final Grade Prediction</div>',
    unsafe_allow_html=True
)

st.info(
    "Enter the student's academic details below to estimate "
    "their final Mathematics grade."
)

# Input section
st.subheader("📝 Student Information")

col1, col2 = st.columns(2)

with col1:
    g1 = st.slider(
        "First Period Grade (G1)",
        min_value=0,
        max_value=20,
        value=10
    )

    studytime = st.selectbox(
        "Weekly Study Time",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "Less than 2 hours",
            2: "2 to 5 hours",
            3: "5 to 10 hours",
            4: "More than 10 hours"
        }[x]
    )

with col2:
    g2 = st.slider(
        "Second Period Grade (G2)",
        min_value=0,
        max_value=20,
        value=10
    )

    absences = st.number_input(
        "Number of School Absences",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

# Prediction button
st.markdown("---")

if st.button("🔮 Predict Final Grade", use_container_width=True):

    input_data = pd.DataFrame(
        [[g1, g2, studytime, absences]],
        columns=["G1", "G2", "studytime", "absences"]
    )

    prediction = model.predict(input_data)[0]

    # Keep the displayed grade within the expected range
    prediction = max(0, min(20, prediction))

    # Display result
    st.subheader("📊 Prediction Result")

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-label">Predicted Final Mathematics Grade</div>
            <div class="result-value">{prediction:.2f} / 20</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if prediction >= 10:
        st.success("The predicted grade is 10 or above.")
    else:
        st.warning(
            "The predicted grade is below 10. "
            "The student may need additional academic support."
        )

    st.caption(
        "Note: This is a machine learning estimate, not a guaranteed "
        "exam result. Actual grades may differ."
    )

# Footer
st.markdown("---")

st.markdown(
    "<center>Developed using Python, Streamlit and Machine Learning</center>",
    unsafe_allow_html=True
)
st.markdown("---")
st.header("📚 Study Time vs Final Grade")

st.write(
    "This chart compares the average final Mathematics grade "
    "for each weekly study-time category in our dataset."
)

study_grades = data.groupby("studytime")["G3"].mean()

study_grades.index = [
    {
        1: "Less than 2 hours",
        2: "2 to 5 hours",
        3: "5 to 10 hours",
        4: "More than 10 hours"
    }[value]
    for value in study_grades.index
]

st.bar_chart(study_grades)

st.caption(
    "Note: This chart shows averages from the dataset. "
    "It does not prove that study time alone causes higher grades."
)

st.markdown("---")
st.header("📊 School Absences vs Final Grade")

st.write(
    "This scatter chart shows the relationship between the number "
    "of school absences and students' final Mathematics grades."
)

st.scatter_chart(
    data,
    x="absences",
    y="G3"
)

st.caption(
    "Each point represents a student. This chart shows a relationship "
    "in the dataset and does not prove that absences alone cause lower grades."
)
