from flask import request, render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = 'Erreur inconnue'
    if request.method == 'POST':
        return render_template('index.html')
        
@app.route('/succes')
def succes():
    return "Authentification réussie !"