<<<<<<< HEAD
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
=======
from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for '/process' URL
@app.route('/process', methods=['POST'])
def process():
    # Only execute this code when a POST request is made to '/process'
    name = request.form.get('test_input')
    # Process the data or perform any desired action
    return f'Hello, {name}!'

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
>>>>>>> 6bed5d48b6dab314ff9b3e3eea49b9a814586496
