
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

def fix_prompt(broken_code: str, error_message: str, language: str) -> str:
    return f"""You are an expert {language} debugger.

The user has this broken {language} code:
{broken_code}

Error message:
{error_message}

Respond with EXACTLY this format:

CODE:
<fixed working code here>

EXPLANATION:
<2-3 sentences explaining what was wrong and how you fixed it>
"""

def explain_prompt(code: str, language: str) -> str:
    return f"""You are a coding teacher explaining code to a beginner.

Explain this {language} code in simple plain English:

{code}

Respond with EXACTLY this format:

CODE:
{code}

EXPLANATION:
<explain line by
