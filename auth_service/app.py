from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        response = {'message': 'Login successful'}
        return jsonify(response), 200
    else:
        response = {'message': 'Login failed'}
        return jsonify(response), 401

if __name__ == '__main__':
    app.run(port=5000)