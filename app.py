import os
from flask import Flask, render_template, request

app = Flask(__name__)


USERNAME = "admin"
PASSWORD = "password123"

@app.route('/')
def home():
    
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    
    user_input = request.form.get('username')
    pass_input = request.form.get('password')

    if user_input == USERNAME and pass_input == PASSWORD:
        return "<h2>Login Successful! ✅</h2><p>Welcome to your PaaS App.</p>"
    else:
        return "<h2>Invalid Username or Password ❌</h2><a href='/'>Try Again</a>"

if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)