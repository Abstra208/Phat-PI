from flask import request, render_template, Flask, redirect, url_for, make_response
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
            resp = make_response(render_template('index.html', user=Username))
            resp.set_cookie('User', Username)
            return resp
        else:
            return render_template('login.html', erreur='Identifiants invalides')

@app.route('/login')
def login():
    return render_template('login.html')