
def build_prompt(user_request: str, language: str) -> str:
    return f"""You are an expert {language} developer and coding teacher.
A user has made the following request:

\"{user_request}\"

Respond with EXACTLY this format and nothing else:

CODE:
<write clean, well-commented {language} code here>

EXPLANATION:
<write 2-3 simple sentences explaining how the code works>

Rules:
- Code must be complete and working
- Add comments inside the code
- Explanation must be beginner-friendly
- Do NOT add anything outside CODE: and EXPLANATION: sections
"""
