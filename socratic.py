import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

def get_socratic_response(question):
    prompt = f"""
You are a Socratic AI Tutor.
Do NOT give direct answers.
Guide the student step by step.
Encourage thinking.
Ask questions instead of solving directly.

Student question: {question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    bot_reply = get_socratic_response(user_message)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    print("--- Server is running at http://127.0.0.1:5000 ---")
    app.run(port=5000)