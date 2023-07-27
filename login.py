from flask import Flask, render_template

app = Flask(__name__)

# In a real-world scenario, you should store the user credentials in a database.
# For simplicity, we are using an in-memory dictionary.
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/v1')
def home2():
    return render_template('login.html')

#@app.route('/login', methods=['POST'])
#def login():
#    username = request.form['username']
#    password = request.form['password']
#
#    if username in users and users[username] == password:
#        return f'Hello, {username}! You have successfully logged in.'
#    else:
#        return 'Invalid username or password. Please try again.'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8091, debug=True)

