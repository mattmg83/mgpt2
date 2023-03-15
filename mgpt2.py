import os
import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

print('Welcome to MathieuGPT, you\'ll need an OpenAI API key (https://platform.openai.com)\nThis script requires python 3.x and the openai package to run\nWrite your queries in English or French and input \'exit\' at any point to exit and return to the terminal')
openai.organization = "org-vNip1LEkzDa2rbFClEkXncDz"
openai.api_key = os.environ.get("CHATGPT_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    content = request.json.get('content')
    if content:
        messages = [{"role": "system", "content": "you are an assistant with a french accent, you occasionally swear in english and often respond sarcastically"}]
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
