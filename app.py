
import streamlit as st
import os, sys

# ─── Load API Key (works both in Colab and Streamlit Cloud) ─────
if "GROQ_API_KEY" not in os.environ:
    try:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    except Exception:
        st.error("⚠️ GROQ_API_KEY not found. Please add it to your secrets.")
        st.stop()

sys.path.insert(0, os.path.dirname(__file__))
from generator import generate_code, fix_code, explain_code

# ─── Page Config ────────────────────────────────────────────────
st.set_page_config(page_title="AI Code Generator", page_icon="🤖", layout="centered")

# ─── CSS ────────────────────────────────────────────────────────
st.markdown("""
    <style>
    .title { font-size:2.5rem; font-weight:800; text-align:center; color:#00d4ff; }
    .subtitle { text-align:center; color:#888; font-size:1rem; margin-bottom:1rem; }
    .output-header { font-size:1.2rem; font-weight:600; color:#00d4ff; margin-top:1.5rem; }
    .explanation-box {
        background-color:#1e2a3a; border-left:4px solid #00d4ff;
        padding:1rem; border-radius:0.5rem; color:#ddd; font-size:0.95rem;
    }
    .counter-box {
        background-color:#1a1a2e; border:1px solid #00d4ff;
        padding:0.5rem 1rem; border-radius:0.5rem;
        text-align:center; color:#00d4ff; font-weight:700;
    }
    .stButton > button {
        width:100%; background-color:#00d4ff; color:#000;
        font-weight:700; font-size:1rem; border-radius:0.5rem; border:none;
    }
    .stButton > button:hover { background-color:#00b8d9; }
    </style>
""", unsafe_allow_html=True)

# ─── Header ─────────────────────────────────────────────────────
st.markdown('<div class="title">🤖 AI Code Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate · Fix · Explain code using AI</div>', unsafe_allow_html=True)

# ─── Usage Counter ──────────────────────────────────────────────
if "count" not in st.session_state:
    st.session_state.count = 0

st.markdown(f'<div class="counter-box">⚡ Snippets Generated: {st.session_state.count}</div>',
            unsafe_allow_html=True)
st.divider()

# ─── Mode Selector ──────────────────────────────────────────────
mode = st.radio("Select Mode:", ["🧠 Generate Code", "🐛 Fix My Code", "📖 Explain Code"], horizontal=True)
st.markdown("<br>", unsafe_allow_html=True)
language = st.selectbox("🌐 Language", ["Python", "JavaScript", "SQL", "Bash"])

# ─── Mode: Generate ─────────────────────────────────────────────
if mode == "🧠 Generate Code":
    user_input = st.text_area("✍️ Describe what you want to build:", height=130,
                               placeholder="e.g. Write a function to check if a number is prime...")
    if st.button("⚡ Generate Code"):
        if not user_input.strip():
            st.warning("⚠️ Please describe what you want to build.")
        else:
            with st.spinner("🧠 Generating your code..."):
                result = generate_code(user_input, language)
            st.session_state.count += 1
            st.markdown('<div class="output-header">📋 Generated Code</div>', unsafe_allow_html=True)
            st.code(result["code"], language=language.lower())
            st.download_button("📥 Download Code", data=result["code"],
                file_name=f"generated.{'py' if language=='Python' else 'js' if language=='JavaScript' else 'sql' if language=='SQL' else 'sh'}",
                mime="text/plain")
            if result["explanation"]:
                st.markdown('<div class="output-header">💡 Explanation</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="explanation-box">{result["explanation"]}</div>', unsafe_allow_html=True)

# ─── Mode: Fix Code ─────────────────────────────────────────────
elif mode == "🐛 Fix My Code":
    broken_code = st.text_area("🐛 Paste your broken code here:", height=150,
                                placeholder="Paste the code that has errors...")
    error_msg = st.text_area("❌ Paste the error message (optional):", height=80,
                              placeholder="e.g. TypeError: unsupported operand type...")
    if st.button("🔧 Fix My Code"):
        if not broken_code.strip():
            st.warning("⚠️ Please paste your broken code first.")
        else:
            with st.spinner("🔧 Fixing your code..."):
                result = fix_code(broken_code, error_msg, language)
            st.session_state.count += 1
            st.markdown('<div class="output-header">✅ Fixed Code</div>', unsafe_allow_html=True)
            st.code(result["code"], language=language.lower())
            st.download_button("📥 Download Fixed Code", data=result["code"],
                file_name=f"fixed.{'py' if language=='Python' else 'js' if language=='JavaScript' else 'sql' if language=='SQL' else 'sh'}",
                mime="text/plain")
            if result["explanation"]:
                st.markdown('<div class="output-header">🔍 What Was Wrong</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="explanation-box">{result["explanation"]}</div>', unsafe_allow_html=True)

# ─── Mode: Explain Code ─────────────────────────────────────────
elif mode == "📖 Explain Code":
    code_input = st.text_area("📋 Paste any code to explain:", height=150,
                               placeholder="Paste any code here and AI will explain it...")
    if st.button("📖 Explain This Code"):
        if not code_input.strip():
            st.warning("⚠️ Please paste some code first.")
        else:
            with st.spinner("📖 Analyzing your code..."):
                result = explain_code(code_input, language)
            st.session_state.count += 1
            st.markdown('<div class="output-header">💡 Code Explanation</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="explanation-box">{result["explanation"]}</div>', unsafe_allow_html=True)

# ─── Footer ─────────────────────────────────────────────────────
st.divider()
st.markdown("<center style='color:#555; font-size:0.8rem;'>Built with ❤️ using Groq + LLaMA 3 + Streamlit</center>",
            unsafe_allow_html=True)
