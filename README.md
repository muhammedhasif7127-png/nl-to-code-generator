<div align="center">

# 🤖 AI Code Generator
### Convert plain English into working code — instantly

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA3-00A67E?style=for-the-badge)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)](https://share.streamlit.io)

<br>

**[🚀 Try Live Demo](https://muhammedhasif7127-png-nl-to-code-generator.streamlit.app)** · **[📁 View Code](https://github.com/muhammedhasif7127-png/nl-to-code-generator)** · **[🐛 Report Bug](https://github.com/muhammedhasif7127-png/nl-to-code-generator/issues)**

</div>

---

## 📌 What is this?
**AI Code Generator** is a web app that uses **LLaMA 3 AI** to convert plain English descriptions into clean, working code. No more Googling or Stack Overflow — just describe what you want and get code instantly!

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **Generate Code** | Describe what you want → get clean working code |
| 🐛 **Fix My Code** | Paste broken code → AI fixes it + explains what was wrong |
| 📖 **Explain Code** | Paste any code → get plain English explanation |
| 🌐 **4 Languages** | Python · JavaScript · SQL · Bash |
| 📥 **Download Code** | Save any generated snippet as a file |
| ⚡ **Usage Counter** | Track how many snippets you've generated |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.11 |
| **AI Model** | LLaMA 3.3 70B via Groq API |
| **UI Framework** | Streamlit |
| **Deployment** | Streamlit Community Cloud |
| **Version Control** | Git & GitHub |

---

## 🚀 Run Locally

```bash
# 1️⃣ Clone the repository
git clone [https://github.com/muhammedhasif7127-png/nl-to-code-generator.git](https://github.com/muhammedhasif7127-png/nl-to-code-generator.git)
cd nl-to-code-generator

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Add your Groq API key
mkdir .streamlit
echo 'GROQ_API_KEY = "your_key_here"' > .streamlit/secrets.toml

# 4️⃣ Run the app
streamlit run app.py
