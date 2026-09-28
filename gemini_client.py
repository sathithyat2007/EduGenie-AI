import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
_client = None


def get_client():
    """Create the Gemini client once, and give a clear error if the key is missing."""
    global _client
    if _client is None:
        key = os.getenv("GEMINI_API_KEY")
        if not key or key == "paste_your_key_here":
            raise ValueError("GEMINI_API_KEY is missing. Add your key in the .env file.")
        _client = genai.Client(api_key=key)
    return _client


def ask_gemini(prompt: str) -> str:
    response = get_client().models.generate_content(model=MODEL, contents=prompt)
    return response.text or ""
