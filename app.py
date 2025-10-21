# app.py
"""
🧠 Artificial Brain - Mini chat Demo
Lightweight Flask API for demo conversational responses.
-------------------------------------------------------
This module demonstrates a simple POST endpoint (/chat)
that handles user input and returns a structured JSON reply.
"""

from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

# Placeholder for actual model logic
# In the future, this will connect to the "Artificial-Brain.AI" models or an external API.
def artificial_brain_response(user_input: str) -> str:
    """
    Core response generator.
    Currently returns mock data for demonstration.
    """
    user_input = user_input.strip().lower()

    # Simple keyword simulation (for demo only)
    replies = {
        "hello": "Hi there! 👋 I'm Artificial Brain — your lightweight AI assistant.",
        "help": "You can send me a message via JSON to /chat. Try saying 'hello' or ask anything!",
        "bye": "Goodbye 👋 — Stay curious!",
    }

    # Default fallback response
    default_reply = f"I received: '{user_input}'. (This is a demo placeholder response 🧠)"

    # Simulate slight thinking delay for realism
    time.sleep(random.uniform(0.2, 0.6))

    return replies.get(user_input, default_reply)


@app.route("/chat", methods=["POST"])
def chat():
    """
    POST /chat
    Request:  { "message": "your message here" }
    Response: { "response": "AI reply here" }
    """
    try:
        data = request.get_json(force=True)
        user_input = data.get("message", "")
        response = artificial_brain_response(user_input)
        return jsonify({
            "success": True,
            "timestamp": time.time(),
            "response": response
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
