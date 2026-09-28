from gemini_client import ask_gemini


def summarize_text(passage: str) -> str:
    prompt = (
        "Summarize the following passage into a short, easy-to-understand version "
        "for quick revision. Keep the key points and remove repetition.\n\n"
        f"{passage}"
    )
    summary = ask_gemini(prompt)
    return summary or "Sorry, I could not summarize this. Please try again."
