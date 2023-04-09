import os
import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

openai.organization = "org-vNip1LEkzDa2rbFClEkXncDz"
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    content = request.json.get('content')
    messages = request.json.get('messages')

    if content:
        messages.append({"role": "user", "content": content})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        chat_response = completion.choices[0].message.content
        return jsonify({"response": chat_response})
    else:
        return jsonify({"error": "Please provide a message."}), 400

if __name__ == '__main__':
    app.run(debug=True)
