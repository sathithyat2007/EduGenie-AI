import json
from gemini_client import ask_gemini


def clean_json_block(text: str) -> str:
    """Remove ```json ... ``` markdown fences from the model response."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text[:-3]
    return text.replace("```json", "").replace("```", "").strip()


def generate_quiz(passage: str) -> list:
    prompt = f"""
Create exactly 3 multiple-choice questions from the topic or passage below.
Each question must have exactly 4 options and one correct answer.
Return ONLY valid JSON (no extra text) in this format:
[
  {{
    "question": "...",
    "options": ["option 1", "option 2", "option 3", "option 4"],
    "answer": "the exact text of the correct option"
  }}
]

Topic or passage:
{passage}
"""
    try:
        cleaned = clean_json_block(ask_gemini(prompt))
        quiz = json.loads(cleaned)
        if not isinstance(quiz, list):
            raise ValueError("Model did not return a list of questions.")
        return quiz
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse quiz JSON: {e}")
    except Exception as e:
        raise ValueError(f"Quiz generation failed: {e}")
