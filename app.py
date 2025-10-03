from flask import Flask, render_template, request, jsonify
from chatbot_response import chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json['message']
    response = chatbot_response(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
