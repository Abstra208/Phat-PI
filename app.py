from flask import request, render_template, Flask, redirect, url_for
app = Flask(__name__)

Users = {
    'admin': '123456',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return redirect(url_for('login'))
    elif request.method == 'POST':
        Username = request.form['username']
        Passwd = request.form['passwd']

        if Username in Users and Users[Username] == Passwd:
            return render_template('index.html', user=Username)
        else:
            return render_template('login.html', erreur='Identifiants invalides')

@app.route('/login')
def login():
    return render_template('login.html')