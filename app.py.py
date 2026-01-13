from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # <<< THIS IS THE KEY LINE

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    # Example reply using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": message}]
    )
    reply = response.choices[0].message.content

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
