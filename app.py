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