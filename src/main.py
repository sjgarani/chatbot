import os
from flask import Flask, send_file, request, jsonify
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_neo4j import Neo4jGraph
from langchain_neo4j import GraphCypherQAChain

app = Flask(__name__)

conversation_history = []

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
enhanced_graph = Neo4jGraph(enhanced_schema=True)
chain = GraphCypherQAChain.from_llm(graph=enhanced_graph, llm=llm, verbose=True, allow_dangerous_requests=True)

def get_bot_response(user_message):
    answer = chain.invoke({"query": "{user_message}"})
    print(answer)
    return answer['result']

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
