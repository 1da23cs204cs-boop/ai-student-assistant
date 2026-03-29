from flask import Flask, request, render_template

app = Flask(__name__)

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

    content = file.read().decode("utf-8", errors="ignore")
    stored_text = content

    return "File uploaded successfully!"

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get("question")

    if not stored_text:
        return "Upload notes first!"

    # simple logic (replace later with AI)
    if question.lower() in stored_text.lower():
        return f"Answer found in notes!"
    else:
        return "Answer not found in notes."

@app.route('/summary')
def summary():
    if not stored_text:
        return "Upload notes first!"

    return stored_text[:300] + "..."

if __name__ == "__main__":
    app.run()
