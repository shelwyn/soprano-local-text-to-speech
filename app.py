import streamlit as st
import os
from soprano import SopranoTTS

# ---------- Page Config ----------
st.set_page_config(
    page_title="Soprano TTS Demo",
    page_icon="🗣️",
    layout="centered"
)

st.title("🗣️ Soprano Text-to-Speech")
st.caption("Ultra-fast, lightweight open-source TTS")

# ---------- Load Model (cached) ----------
@st.cache_resource
def load_model():
    return SopranoTTS(
        backend="auto",
        device="auto",
        cache_size_mb=100,
        decoder_batch_size=1,
    )

model = load_model()

# ---------- UI ----------
text = st.text_area(
    "Enter text to convert to speech",
    height=180,
    placeholder="Type or paste your text here..."
)

generate = st.button("▶️ Generate & Play")

# ---------- Logic ----------
if generate:
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating audio…"):
            output_file = "output.wav"
            model.infer(text, output_file)

        if os.path.exists(output_file):
            st.success("Audio generated successfully!")
            st.audio(output_file, format="audio/wav")
        else:
            st.error("Failed to generate audio.")
