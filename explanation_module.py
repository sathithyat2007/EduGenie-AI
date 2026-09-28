from gemini_client import ask_gemini


def explain_concept(topic: str) -> str:
    prompt = (
        "Explain the following concept in simple words for a beginner student, "
        f"in a short and clear way: {topic}"
    )
    result = ask_gemini(prompt)
    return result or "Sorry, I could not generate an explanation. Please try again."
