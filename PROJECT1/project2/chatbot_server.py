from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    return jsonify({'reply': user_message})

if __name__ == '__main__':
    app.run(debug=True)