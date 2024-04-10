from flask import request, render_template, Flask, redirect, url_for, session
app = Flask(__name__)
import json

app.secret_key = b'36f81d8585f136a0536a350f69443bf8e26bcbc8407e8dc3bcf584bd92ba4cd6' # make sure to change this before using, and keep it secret (if you want to generate a secret one, you can use { python -c 'import secrets; print(secrets.token_hex())' } )

Users = {
    'admin': '123456',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if session['username'] != "":
            if session['username'] in Users and Users[session['username']] == session['passwd']:
                return render_template('index.html')
        return redirect(url_for('login'))
    elif request.method == 'POST':
        Username = request.form['username']
        Passwd = request.form['passwd']

        if Username in Users and Users[Username] == Passwd:
            session['username'] = Username
            session['passwd'] = Passwd
            return render_template('index.html')
        else:
            return render_template('login.html', error='Identifiants invalides')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    session['username'] = ""
    session['passwd'] = ""
    return redirect(url_for('login'))

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        if session['username'] != "":
            Speed = request.form['Scroll_input']
            Opacity = request.form['opacity_input']
            Text = request.form['test_input']
            data = {
                "speed": Speed,
                "opacity": Opacity,
                "text": Text
            }
            json_string = json.dumps(data)
            f = open("screen.json", "a")
            f.truncate(0)
            f.write(json_string)
            f.close()
            return render_template('index.html', info=json_string)
    elif request.method == 'GET':
        if session['username'] == "":
            return render_template('login.html')
