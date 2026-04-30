
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def _call_api(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    return response.choices[0].message.content

def _parse_response(text: str) -> dict:
    code, explanation = "", ""
    if "CODE:" in text and "EXPLANATION:" in text:
        code = text.split("CODE:")[1].split("EXPLANATION:")[0].strip()
        explanation = text.split("EXPLANATION:")[1].strip()
    else:
        code = text.strip()
        explanation = "Done!"

    # Clean markdown code fences
    for lang in ["python", "javascript", "sql", "bash", ""]:
        code = code.replace(f"```{lang}", "")
    code = code.replace("```", "").strip()

    return {"code": code, "explanation": explanation}

def generate_code(user_request: str, language: str = "Python") -> dict:
    from prompts import build_prompt
    prompt = build_prompt(user_request, language)
    return _parse_response(_call_api(prompt))

def fix_code(broken_code: str, error_message: str, language: str = "Python") -> dict:
    from prompts import fix_prompt
    prompt = fix_prompt(broken_code, error_message, language)
    return _parse_response(_call_api(prompt))

def explain_code(code: str, language: str = "Python") -> dict:
    from prompts import explain_prompt
    prompt = explain_prompt(code, language)
    return _parse_response(_call_api(prompt))
