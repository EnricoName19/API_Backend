from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)                     # allow calls from React (port 3000)

@app.route('/')
def home():
    return "Hello from Flask!"

# ⬇️ New chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)   # force=True tolerates empty headers
    user_msg = (data.get('message') or '').strip().lower()

    if user_msg == 'hi':
        reply = 'hello enrico'
    else:
        reply = f'I dont understand.: {user_msg}'

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
