import streamlit as st
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Transcript Cleanup Engine",
    page_icon="📝",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #f4f6f9;
}

/* Title */
h1 {
    color: #1e293b;
    text-align: center;
    font-size: 50px;
}

/* Subheadings */
h2, h3 {
    color: #1e293b !important;
}

/* Normal Text */
p, label, div {
    color: #111827 !important;
    font-size: 17px;
}

/* Text Area */
.stTextArea textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 12px;
    border: 2px solid #cbd5e1;
    font-size: 18px;
}

/* File Upload Box */
[data-testid="stFileUploader"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 2px solid #cbd5e1;
}

/* Buttons */
.stButton button {
    background-color: #22c55e !important;
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
}

/* Download Button */
.stDownloadButton button {
    background-color: #3b82f6 !important;
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #e2e8f0;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Project Info")

st.sidebar.write("## Transcript Cleanup Engine")

st.sidebar.write("### Technologies Used")
st.sidebar.write("- Python")
st.sidebar.write("- Streamlit")
st.sidebar.write("- Regex")

st.sidebar.write("### Features")
st.sidebar.write("- Filler word removal")
st.sidebar.write("- Duplicate word removal")
st.sidebar.write("- File upload support")
st.sidebar.write("- Download cleaned transcript")

# ---------------- MAIN TITLE ----------------
st.title("📝 Transcript Cleanup Engine")

st.write(
    "Clean noisy transcripts by removing filler words, duplicate words, and formatting issues."
)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📂 Upload Transcript File",
    type=["txt"]
)

# ---------------- TEXT AREA ----------------
text = st.text_area(
    "✍️ Enter Transcript Text",
    height=200
)

# ---------------- FILLER WORDS ----------------
filler_words = ["um", "uh", "like", "hmm"]

# ---------------- CLEANUP FUNCTION ----------------
def clean_text(text):

    # Remove filler words
    for word in filler_words:
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    # Remove duplicate consecutive words
    text = re.sub(
        r'\b(\w+)(\s+\1\b)+',
        r'\1',
        text,
        flags=re.IGNORECASE
    )

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Fix punctuation
    text = re.sub(r'[,.!?]+', '.', text)

    # Remove spaces before punctuation
    text = re.sub(r'\s+\.', '.', text)

    # Trim text
    text = text.strip()

    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]

    # Add final period
    if text and not text.endswith('.'):
        text += '.'

    return text

# ---------------- FILE CLEANUP ----------------
if uploaded_file is not None:

    # Read uploaded file
    file_text = uploaded_file.read().decode("utf-8")

    # Show original content
    st.subheader("📄 Original File Content")
    st.write(file_text)

    # Clean file text
    cleaned_file_text = clean_text(file_text)

    # Show cleaned content
    st.subheader("✅ Cleaned File Content")
    st.write(cleaned_file_text)

    # Download button
    st.download_button(
        label="⬇️ Download Cleaned File",
        data=cleaned_file_text,
        file_name="cleaned_transcript.txt",
        mime="text/plain"
    )

# ---------------- MANUAL CLEANUP ----------------
if st.button("🚀 Clean Transcript"):

    cleaned = clean_text(text)

    st.subheader("✅ Cleaned Transcript")

    st.write(cleaned)

    st.download_button(
        label="⬇️ Download Cleaned Transcript",
        data=cleaned,
        file_name="cleaned_transcript.txt",
        mime="text/plain"
    )