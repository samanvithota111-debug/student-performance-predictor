import streamlit as st

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# ---------- FUTURISTIC DESIGN ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #080817, #11112b, #1b1035);
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, label {
    color: white !important;
}

.hero {
    text-align: center;
    padding: 55px 20px;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        rgba(100, 40, 180, 0.35),
        rgba(20, 100, 200, 0.25)
    );
    border: 1px solid rgba(160, 100, 255, 0.5);
    box-shadow: 0 0 30px rgba(130, 60, 255, 0.15);
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    background: linear-gradient(90deg, #b794ff, #55d6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 20px;
    color: #d4d4f5 !important;
}

.feature-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(160, 100, 255, 0.35);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    min-height: 190px;
    box-shadow: 0 0 15px rgba(100, 60, 200, 0.08);
}

.feature-card h3 {
    color: #bd9cff !important;
}

.feature-card p {
    color: #d5d5eb !important;
}

.stButton > button {
    background: linear-gradient(90deg, #8b5cf6, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 30px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.7);
    border: 1px solid #c4b5fd;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<div class="hero">
<div style="font-size:65px;">🎓 🤖</div>
<div class="hero-title">STUDENT PERFORMANCE PREDICTOR</div>
<p class="hero-subtitle">
Discover the power of Machine Learning in Education
</p>
<p>
An intelligent application that predicts a student's
final Mathematics grade using academic performance
and study-related information.
</p>
</div>
""", unsafe_allow_html=True)

st.write("")



st.write("")
st.write("")


# ---------- INTRODUCTION ----------
st.markdown("## ✨ Welcome to the Future of Education")

st.markdown("""
This project uses **Machine Learning** to estimate a student's
final Mathematics grade based on previous grades, study time,
and school absences.

Our goal is to explore how data and artificial intelligence
can help us understand student performance.
""")


st.write("")
st.markdown("## ⚡ What Can You Explore?")


# ---------- FEATURE CARDS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:45px;">🧠</div>
        <h3>AI Prediction</h3>
        <p>Use a trained Machine Learning model to estimate
        a student's final grade.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:45px;">📊</div>
        <h3>Data Insights</h3>
        <p>Explore graphs showing study time, absences,
        and student grades.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:45px;">🚀</div>
        <h3>Smart Learning</h3>
        <p>Discover how Machine Learning can be applied
        to educational data.</p>
    </div>
    """, unsafe_allow_html=True)


st.write("")
st.write("")


# ---------- GET STARTED ----------
st.markdown(
    "<h2 style='text-align:center;'>Ready to Explore? 🚀</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Let's predict a student's performance!</p>",
    unsafe_allow_html=True
)

left, center, right = st.columns([1, 2, 1])

with center:
    if st.button("🚀 GET STARTED"):
       st.switch_page("pages/1_Prediction.py")


# ---------- FOOTER ----------
st.markdown("---")

st.markdown("""
<p style="text-align:center; color:#9ca3af;">
    Built with Python, Streamlit and Machine Learning 💜
</p>
""", unsafe_allow_html=True)