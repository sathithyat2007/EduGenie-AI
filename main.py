from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextInput(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/qa")
def qa(data: TextInput):
    try:
        return {"answer": answer_question(data.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/explain")
def explain(data: TextInput):
    try:
        return {"explanation": explain_concept(data.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/quiz")
def quiz(data: TextInput):
    try:
        return {"quiz": generate_quiz(data.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize")
def summarize(data: TextInput):
    try:
        return {"summary": summarize_text(data.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/learn/recommendations")
def recommendations(data: TextInput):
    try:
        return {"recommendations": get_learning_recommendations(data.text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
