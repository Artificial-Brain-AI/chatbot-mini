from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple “AI” response function (API feature is partially done 😅)
def simple_ai_response(user_input):
    # Demo logic: simple keyword responses
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "help" in user_input:
        return "I can answer questions or simulate simple chatbot responses."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return f"You said: {user_input}. (This is a demo response.)"

# API route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = simple_ai_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
