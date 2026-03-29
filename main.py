@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question")

    prompt = f"Answer based on these notes:\n{stored_text}\nQuestion:{question}"
    result = ask_ai(prompt)

    return result
