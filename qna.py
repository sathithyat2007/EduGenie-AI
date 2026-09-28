from gemini_client import ask_gemini


def answer_question(question: str) -> str:
    prompt = (
        "You are EduGenie, a friendly learning assistant for students. "
        "Answer the question accurately in a short and clear way.\n\n"
        f"Question: {question}"
    )
    answer = ask_gemini(prompt)
    return answer or "Sorry, I could not generate an answer. Please try again."
