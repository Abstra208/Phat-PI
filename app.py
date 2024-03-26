from flask import request, render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = 'Erreur inconnue'
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['passwd']
        if username == "admin" and passwd == "123456":
            return render_template('index.html')
        else:
            error = 'Nom d/utilisateur ou mot de passe invalide'
            return render_template('login.html', error=error)
    return render_template('login.html', error=error)