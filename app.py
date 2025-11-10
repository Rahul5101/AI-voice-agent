import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
print("🧠 sys.path:", sys.path)  # debug line


from fastapi import FastAPI, Form,Request
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from agent.chat import ConversationAgent
from agent.text_to_speech import SpeechSynthesizer
import os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")
agent = ConversationAgent(API_KEY)
tts = SpeechSynthesizer()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="template")

# Root endpoint (renders chat.html)
@app.get("/chat", response_class=HTMLResponse)
async def chat_form(request: Request):
    """Renders the HTML chat interface"""
    return templates.TemplateResponse("chat.html", {"request": request})


@app.get("/")
def root(): 
    return {"message": "Riverwood AI Voice Agent is running "}

@app.post("/chat/")
async def chat(user_id: str = Form(...), message: str = Form(...)):
    reply = agent.generate_reply(user_id, message)  
    voice_path = tts.synthesize(reply)
    return JSONResponse({"reply": reply, "voice_path": voice_path})



@app.get("/healthz")
def health_check():
    return {"status": "ok"}
