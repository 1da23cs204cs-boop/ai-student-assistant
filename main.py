from flask import Flask, request, render_template
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

stored_text = ""

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    global stored_text
    file = request.files.get('file')

    if not file:
        return "No file uploaded"

    stored_text = file.read().decode("utf-8", errors="ignore")

    return "<h2>File uploaded!</h2><a href='/'>Back</a>"

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@app.route('/summary')
def summary():
    if not stored_text:
        return "Upload notes first!"

    prompt = f"Summarize this:\n{stored_text}"
    result = ask_ai(prompt)

    return f"<h2>Summary</h2><p>{result}</p><a href='/'>Back</a>"

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get("question")

    prompt = f"Answer based on these notes:\n{stored_text}\nQuestion:{question}"
    result = ask_ai(prompt)

    return f"<h2>Answer</h2><p>{result}</p><a href='/'>Back</a>"

@app.route('/flashcards')
def flashcards():
    prompt = f"Create 5 flashcards from this:\n{stored_text}"
    result = ask_ai(prompt)

    return f"<h2>Flashcards</h2><p>{result}</p><a href='/'>Back</a>"

@app.route('/quiz')
def quiz():
    prompt = f"Create a 5-question quiz with answers:\n{stored_text}"
    result = ask_ai(prompt)

    return f"<h2>Quiz</h2><p>{result}</p><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run()
