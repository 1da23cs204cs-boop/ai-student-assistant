from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Student Assistant Running!"

# Upload route (basic for now)
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"})
    
    return jsonify({"message": f"{file.filename} uploaded successfully!"})

# Simple Q&A test route
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")
    
    return jsonify({
        "answer": f"You asked: {question} (AI will answer later)"
    })

if __name__ == "__main__":
    app.run()
