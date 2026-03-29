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

    stored_text = file.read().decode("utf-8", errors="ignore")

    return "<h2>File uploaded successfully!</h2><a href='/'>Go Back</a>"

@app.route('/summary')
def summary():
    if not stored_text:
        return "Upload notes first!"

    summary = stored_text[:500]
    return f"<h2>Summary:</h2><p>{summary}</p><a href='/'>Back</a>"

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get("question")

    if not stored_text:
        return "Upload notes first!"

    if question.lower() in stored_text.lower():
        return f"<h2>Answer found in notes!</h2><a href='/'>Back</a>"
    else:
        return "<h2>Answer not found.</h2><a href='/'>Back</a>"

@app.route('/flashcards')
def flashcards():
    if not stored_text:
        return "Upload notes first!"

    lines = stored_text.split('.')[:5]
    cards = "".join([f"<p>Q: {l.strip()} ?<br>A: {l.strip()}</p>" for l in lines])
    return f"<h2>Flashcards</h2>{cards}<a href='/'>Back</a>"

@app.route('/quiz')
def quiz():
    if not stored_text:
        return "Upload notes first!"

    lines = stored_text.split('.')[:5]
    quiz = "".join([f"<p>Q{i+1}: {l.strip()} ?</p>" for i,l in enumerate(lines)])
    return f"<h2>Quiz</h2>{quiz}<a href='/'>Back</a>"

if __name__ == "__main__":
    app.run()
