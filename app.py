
import streamlit as st
import os, sys
sys.path.insert(0, '/content/nl-to-code-generator')
from generator import generate_code

st.set_page_config(page_title="AI Code Generator", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .title { font-size:2.5rem; font-weight:800; text-align:center; color:#00d4ff; }
    .subtitle { text-align:center; color:#888; font-size:1rem; margin-bottom:2rem; }
    .output-header { font-size:1.2rem; font-weight:600; color:#00d4ff; margin-top:1.5rem; }
    .explanation-box {
        background-color:#1e2a3a; border-left:4px solid #00d4ff;
        padding:1rem; border-radius:0.5rem; color:#ddd; font-size:0.95rem;
    }
    .stButton > button {
        width:100%; background-color:#00d4ff; color:#000;
        font-weight:700; font-size:1rem; border-radius:0.5rem; border:none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🤖 AI Code Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert plain English into working code — instantly</div>', unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_area("✍️ Describe what you want to build:", height=130,
                               placeholder="e.g. Write a function to check if a number is prime...")
with col2:
    language = st.selectbox("🌐 Language", ["Python", "JavaScript", "SQL", "Bash"])
    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button("⚡ Generate Code")

if generate_btn:
    if not user_input.strip():
        st.warning("⚠️ Please describe what you want to build first.")
    else:
        with st.spinner("🧠 Generating your code..."):
            result = generate_code(user_input, language)

        st.markdown('<div class="output-header">📋 Generated Code</div>', unsafe_allow_html=True)
        st.code(result["code"], language=language.lower())

        st.download_button(
            label="📥 Download Code",
            data=result["code"],
            file_name=f"generated.{'py' if language=='Python' else 'js' if language=='JavaScript' else 'sql' if language=='SQL' else 'sh'}",
            mime="text/plain"
        )

        if result["explanation"]:
            st.markdown('<div class="output-header">💡 Explanation</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="explanation-box">{result["explanation"]}</div>', unsafe_allow_html=True)

        st.divider()
        st.markdown("💬 **Want to try another?** Update the description above and click Generate again!")

st.divider()
st.markdown("<center style='color:#555; font-size:0.8rem;'>Built with ❤️ using Groq + LLaMA 3 + Streamlit</center>", unsafe_allow_html=True)
