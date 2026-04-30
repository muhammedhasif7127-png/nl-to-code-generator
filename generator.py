
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_code(user_request: str, language: str = "Python") -> dict:
    from prompts import build_prompt
    prompt = build_prompt(user_request, language)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )

    text = response.choices[0].message.content
    code, explanation = "", ""

    if "CODE:" in text and "EXPLANATION:" in text:
        code = text.split("CODE:")[1].split("EXPLANATION:")[0].strip()
        explanation = text.split("EXPLANATION:")[1].strip()
    else:
        code = text.strip()
        explanation = "Code generated successfully."

    code = code.replace("```python", "").replace("```javascript", "")
    code = code.replace("```sql", "").replace("```bash", "")
    code = code.replace("```", "").strip()

    return {"code": code, "explanation": explanation}
