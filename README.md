# EduGenie 🧞 Gemini Powered Learning Assistant

## Setup
1. Open the folder containing `requirements.txt` and `main.py` in VS Code. If your terminal is in the parent `Downloads\EduGenie` folder, run `cd .\EduGenie` first.
2. Put your Gemini API key in `.env` (GEMINI_API_KEY=...)
3. Open a terminal in VS Code and run:

Mac / Linux:
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    uvicorn main:app --reload

Windows:
    python -m venv venv
    venv\Scripts\activate
    python -m pip install -r requirements.txt
    uvicorn main:app --reload

4. Open http://127.0.0.1:8000

Model: gemini-3.8-flash (change GEMINI_MODEL in .env if needed)
