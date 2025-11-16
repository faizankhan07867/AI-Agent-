from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate_blog(
    request: Request,
    topic: str = Form(...),
    subtitles: str = Form(...)
):
    # Simple Blog Generator Logic
    subtitle_list = subtitles.split("\n")

    final_output = f"<h2>Blog Topic: {topic}</h2><br>"

    for st in subtitle_list:
        final_output += f"<h3>{st}</h3>"
        final_output += f"<p>{topic} — {st} ka detailed explanation yaha aa jayega.</p><br>"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": final_output}
    )
