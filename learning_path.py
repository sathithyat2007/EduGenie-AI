from gemini_client import ask_gemini


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized, structured learning path for: {topic}

Include:
- Beginner, Intermediate and Advanced concepts, organized by difficulty
- A suggested timeline for each level
- Useful resources for each level (videos, articles, books)
- Simple step-by-step guidance and practice tips
Use clear headings and bullet points.
"""
    try:
        result = ask_gemini(prompt)
        return result or "The response was empty or incomplete. Please try again."
    except Exception as e:
        return f"Could not generate learning path: {e}"
