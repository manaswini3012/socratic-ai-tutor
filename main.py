from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
async def socratic_chat(data: ChatMessage):
    try:
        prompt = f"""
You are a Socratic Tutor.
Never give direct answers.
Ask guiding questions.
Encourage the student to think step by step.
Be friendly and motivating.

Student question: {data.message}
"""

        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return {"reply": response["message"]["content"]}

    except Exception as e:
        return {"reply": f"Error connecting to AI: {str(e)}"}