# 🗣️ Soprano Streamlit TTS

A lightweight, blazing-fast **Text-to-Speech web application** built using **Soprano-1.1-80M** and **Streamlit**.  
This project demonstrates how to run Soprano locally, generate high-quality speech in seconds, and play audio instantly in the browser.

---

## Features

- Ultra-fast inference (near real-time, even for long paragraphs)
- Lightweight Soprano-1.1-80M model (~80M parameters)
- High-quality 32kHz WAV audio
- Runs locally on **CPU / CUDA GPU / Apple MPS**
- Simple Streamlit UI
- No cloud APIs or external services required

---

## 🔗 Model & Source

- **Hugging Face Model**  
  https://huggingface.co/ekwek/Soprano-1.1-80M

- **Official Soprano GitHub**  
  https://github.com/ekwek1/soprano

---

## Project Structure

```text
soprano-streamlit-tts/
├── app.py
├── requirements.txt
└── README.md

Installation
1️⃣ Clone the repository
git clone https://github.com/shelwyn/soprano-local-text-to-speech
cd soprano-streamlit-tts

2️⃣ Install dependencies
pip install -r requirements.txt


⚠️ Windows + CUDA users
After installing soprano-tts, reinstall the correct PyTorch CUDA wheel:

pip uninstall -y torch
pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128

▶️ Run the Streamlit App
streamlit run app.py


Open your browser at:

http://localhost:8501

How the App Works

Enter text into the input area

Click Generate & Play

Soprano converts text to speech

Audio plays instantly in the browser

Even large paragraphs can be converted in ~2 seconds, showcasing Soprano’s extremely optimized inference pipeline.