# 🎧 AI-Powered Audio Signal Processing Assistant

An AI-powered educational assistant built using **IBM watsonx Orchestrate**, **GPT-OSS-120B**, and **Streamlit**. The application helps students, educators, and professionals understand Audio Signal Processing concepts through an interactive conversational interface.

---

Live demo: https://audiosignalprocessingassistantagent-4aqbzczot2zuj4sejyoq59.streamlit.app/

---

## 📌 Project Overview

Audio Signal Processing is an important subject in Electronics, Communication Engineering, and Digital Signal Processing. Understanding concepts like filtering, sampling, aliasing, Fourier Transform, FIR, IIR, and operational amplifiers can be challenging.

This project provides an intelligent AI assistant capable of answering Audio Signal Processing questions in real time using IBM watsonx Orchestrate and the GPT-OSS-120B language model.

---

## 🚀 Features

- 🎧 Interactive AI chatbot
- 📚 Explains Audio Signal Processing concepts
- 🔍 Answers technical DSP questions
- 💬 Maintains conversation history
- 📥 Download chat history
- 🌙 Modern dark-themed Streamlit interface
- ⚡ Powered by IBM watsonx Orchestrate
- 🤖 Uses GPT-OSS-120B Large Language Model

---

## 🛠 Technologies Used

- Python
- Streamlit
- IBM watsonx Orchestrate SDK
- GPT-OSS-120B
- HTML
- CSS
- GitHub
- Streamlit Community Cloud

---

## ▶ Running the Application

Start the Streamlit application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 🔐 Environment Variables

Create a `.env` file for local development.

```env
API_KEY=YOUR_IBM_API_KEY
INSTANCE_URL=YOUR_INSTANCE_URL
```

For **Streamlit Cloud**, add the following under **App Settings → Secrets**:

```toml
API_KEY="YOUR_IBM_API_KEY"
INSTANCE_URL="YOUR_INSTANCE_URL"
```

> Never upload your API Key or Instance URL to GitHub.

---

## 💡 Sample Questions

- What is an operational amplifier?
- Explain Sampling Theorem.
- What is aliasing?
- Difference between FIR and IIR filters.
- Explain FFT.
- What is convolution?
- Explain digital filters.
- What is signal quantization?
- Difference between analog and digital signals.
- Explain low-pass and high-pass filters.

---

## 🏗 System Architecture

```
User
   │
   ▼
Streamlit Interface
   │
   ▼
IBM watsonx Orchestrate SDK
   │
   ▼
GPT-OSS-120B
   │
   ▼
AI Generated Response
   │
   ▼
Chat Output
```

---

## 🔄 LangFlow Workflow

```
Chat Input
     │
     ▼
Agent
 │
 ├── GPT-OSS-120B
 └── Agent Instructions
     │
     ▼
Chat Output
```

---

## 📈 Future Enhancements

- Voice-based interaction
- PDF question answering (RAG)
- Audio file analysis
- FFT visualization
- Waveform plotting
- Circuit diagram explanation
- Multilingual support
- Speech-to-Text integration
- Text-to-Speech support

---

## 📖 Project Objective

The objective of this project is to provide an AI-powered educational assistant capable of explaining Audio Signal Processing concepts through natural language interaction. It helps students quickly understand theoretical and practical DSP topics using IBM watsonx Orchestrate and GPT-OSS-120B.

---

## 👨‍💻 Author

**Ajay Garshakurthi**

Electronics and Communication Engineering

IBM University Engagement Project

---

