from flask import request, render_template, Flask, redirect, url_for, session
app = Flask(__name__)
import json

app.secret_key = b'36f81d8585f136a0536a350f69443bf8e26bcbc8407e8dc3bcf584bd92ba4cd6'
app_version = "1.1.0"

with open("users.json", "r") as file:
    json_users = file.read()
data_users = json.loads(json_users)
Users = data_users

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if session.get('username'):
            if session['username'] in Users and Users[session['username']] == session['passwd']:
                with open("screen.json", "r") as file:
                    json_info = file.read()
                data_info = json.loads(json_info)
                screen_info = data_info
                return render_template('index.html', screen_info=screen_info, version = app_version)
        return redirect(url_for('login'))
    elif request.method == 'POST':
        Username = request.form['username']
        Passwd = request.form['passwd']

        if Username in Users and Users[Username] == Passwd:
            session['username'] = Username
            session['passwd'] = Passwd
            with open("screen.json", "r") as file:
                json_info = file.read()
            data_info = json.loads(json_info)
            screen_info = data_info
            return render_template('index.html', screen_info=screen_info, version = app_version)
        else:
            return render_template('login.html', error='Identifiants invalides')

@app.route('/login')
def login():
    if session.get('username'):
        if session['username'] in Users and Users[session['username']] == session['passwd']:
            return redirect(url_for('index'))
    return render_template('login.html')
@app.route('/logout')
def logout():
    session['username'] = ""
    session['passwd'] = ""
    return redirect(url_for('login'))

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        if session['username'] in Users and Users[session['username']] == session['passwd']:
            Speed = request.form['Scroll_input']
            Opacity = request.form['opacity_input']
            Text = request.form['test_input']
            data = {
                "speed": Speed,
                "opacity": Opacity,
                "text": Text,
            }
            json_string = json.dumps(data)
            f = open("screen.json", "a")
            f.truncate(0)
            f.write(json_string)
            f.close()
            with open("screen.json", "r") as file:
                 json_info = file.read()
            data_info = json.loads(json_info)
            screen_info = data_info
            return render_template('index.html', screen_info=screen_info, version = app_version)
    return redirect(url_for('index'))