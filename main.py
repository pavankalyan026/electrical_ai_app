from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ai_engine import ask_electrical_ai

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def chat_home(request: Request):
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "answer": None
    })


@app.post("/", response_class=HTMLResponse)
def chat_submit(
    request: Request,
    question: str = Form(...),
    language: str = Form(...)
):
    answer = ask_electrical_ai(question, language)

    return templates.TemplateResponse("chat.html", {
        "request": request,
        "answer": answer
    })
