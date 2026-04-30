
def build_prompt(user_request: str, language: str) -> str:
    return (
        "You are an expert " + language + " developer and coding teacher.\n"
        "A user has made the following request:\n\n"
        "\"" + user_request + "\"\n\n"
        "Respond with EXACTLY this format and nothing else:\n\n"
        "CODE:\n"
        "<write clean, well-commented " + language + " code here>\n\n"
        "EXPLANATION:\n"
        "<write 2-3 simple sentences explaining how the code works>\n\n"
        "Rules:\n"
        "- Code must be complete and working\n"
        "- Add comments inside the code\n"
        "- Explanation must be beginner-friendly\n"
        "- Do NOT add anything outside CODE: and EXPLANATION: sections\n"
    )

def fix_prompt(broken_code: str, error_message: str, language: str) -> str:
    return (
        "You are an expert " + language + " debugger.\n\n"
        "The user has this broken " + language + " code:\n"
        + broken_code + "\n\n"
        "Error message:\n"
        + error_message + "\n\n"
        "Respond with EXACTLY this format:\n\n"
        "CODE:\n"
        "<fixed working code here>\n\n"
        "EXPLANATION:\n"
        "<2-3 sentences explaining what was wrong and how you fixed it>\n"
    )

def explain_prompt(code: str, language: str) -> str:
    return (
        "You are a coding teacher explaining code to a beginner.\n\n"
        "Explain this " + language + " code in simple plain English:\n\n"
        + code + "\n\n"
        "Respond with EXACTLY this format:\n\n"
        "CODE:\n"
        + code + "\n\n"
        "EXPLANATION:\n"
        "<explain in simple English what this code does, line by line>\n"
    )
