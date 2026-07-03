import streamlit as st
import tempfile

from services.speech_to_text import convert_speech_to_text
from services.audio_features import extract_audio_features
from services.pdf_report import generate_pdf
from services.similarity import calculate_similarity


# ---------- Load CSS ----------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(
    page_title="Voice Based Concept Understanding Analyzer",
    page_icon="🎤",
    layout="wide"
)

load_css()
st.sidebar.title("📌 About Project")

st.sidebar.write("""
### 🎤 Voice Based Concept Understanding Analyzer

**Developer:** Karuna

### Technologies Used
- Python
- Streamlit
- SpeechRecognition
- Sentence Transformers
- ReportLab

### Features
✅ Speech to Text
✅ Similarity Score
✅ AI Feedback
✅ PDF Report
""")

# ---------- Header ----------
st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#7C3AED);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
">
<h1>🎤 Voice Based Concept Understanding Analyzer</h1>
<h4>AI Powered Speech Analysis Dashboard</h4>
</div>
""", unsafe_allow_html=True)

st.info("📂 Upload an audio file to analyze speech.")

uploaded_file = st.file_uploader(
    "Choose an Audio File",
    type=["wav", "mp3", "m4a", "mpeg", "ogg", "aac"]
)

if uploaded_file is not None:

    st.success("✅ Audio uploaded successfully!")
    st.audio(uploaded_file)
    st.info(f"📁 File Name: {uploaded_file.name}")
    st.info(f"📦 File Size: {round(uploaded_file.size/1024,2)} KB")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    if st.button("Convert Speech to Text"):

        with st.spinner("Converting speech to text..."):
            text = convert_speech_to_text(temp_path)

        st.subheader("📝 Transcribed Text")
        st.text_area(
            "Transcript",
            value=text,
            height=180
        )

        # Audio Features
        features = extract_audio_features(temp_path)

        duration = features["Duration"]
        sample_rate = features["Sample Rate"]

        word_count = len(text.split())

        if duration > 0:
            speaking_speed = round((word_count / duration) * 60)
        else:
            speaking_speed = 0

        st.subheader("🎵 Audio Features")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("⏱ Duration", f"{duration:.2f} sec")

        with col2:
            st.metric("🎧 Sample Rate", f"{sample_rate} Hz")

        st.subheader("📊 Speech Statistics")

        col3, col4 = st.columns(2)

        with col3:
            st.metric("📝 Word Count", word_count)

        with col4:
            st.metric("⚡ Speaking Speed", f"{speaking_speed} WPM")

        st.subheader("⭐ Performance")

        if duration >= 10:
            performance = "Excellent"
            st.success("⭐⭐⭐⭐⭐ Excellent Presentation")
        elif duration >= 5:
            performance = "Good"
            st.warning("⭐⭐⭐ Good Presentation")
        else:
            performance = "Needs Improvement"
            st.error("⭐ Needs Improvement")
        # ---------- Similarity ----------
        expected_text = st.text_area(
            "Enter Expected Answer",
            "Artificial Intelligence is the simulation of human intelligence by machines."
        )

        if expected_text.strip():

            score = calculate_similarity(expected_text, text)

            st.subheader("🤖 Similarity Score")

            st.progress(float(score) / 100)

            st.success(f"{score:.2f}%")

            # ---------- AI Feedback ----------
            st.subheader("💡 AI Feedback")

            if score >= 90:
                st.success("🌟 Excellent! Your explanation is very clear.")
            elif score >= 70:
                st.info("👍 Good! Your answer is mostly correct.")
            elif score >= 50:
                st.warning("⚠️ Average! Try to explain more clearly.")
            else:
                st.error("❌ Needs Improvement. Please explain the concept more clearly.")

            # ---------- PDF ----------
            report_file = generate_pdf(text)

            with open(report_file, "rb") as pdf:
                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf,
                    file_name="Voice_Analysis_Report.pdf",
                    mime="application/pdf"
                )

            st.success("✅ Analysis Completed Successfully!")

            st.markdown("---")
            st.caption("Developed by Karuna| © 2026 Voice Based Concept Understanding Analyzer")
