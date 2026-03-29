from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return "No file uploaded"
    
    return f"Uploaded: {file.filename}"

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get("question")
    return f"You asked: {question}"

if __name__ == "__main__":
    app.run()
