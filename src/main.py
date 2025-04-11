import os
from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

conversation_history = []

def get_bot_response(user_message):
    # Basic static response for now.  Replace with actual chatbot logic.
    return f"You said: {user_message}" 

@app.route("/")
def index():
    return send_file('index.html')

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
