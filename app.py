from flask import request, render_template, Flask
app = Flask(__name__)

Users = {
    'admin': '123456',
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = 'Erreur inconnue'
    if request.method == 'POST':
        Username = request.form['username']
        Passwd = request.form['passw']

        if Username in Users and Users[Username] == Passwd:
            return render_template('index.html', user=Username)
        else:
            return render_template('login.html', erreur='Identifiants invalides')