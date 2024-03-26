from flask import request, render_template, app

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = 'Erreur inconnue'
    if request.method == 'POST':
        connection(request.form['username'], request.form['passw'])
    if request.method == 'GET':
        render_template('/html/login.html')
    return render_template('login.html', error=error)

def connection(username, passwd):
    if username == "admin" and passwd == "123456":
        set_screen(request.form['test_input'],request.form['Scroll_input'], request.form['opacity_input'])
        render_template('html/login.html')
    else:
        error = 'Nom d/utilisateur ou mot de passe invalide'
        return render_template('login.html', error=error)

def set_screen(text, scroll, opacity):
    set_file = open('info.txt', 'a')
    set_file.write(text)
    set_file.close()

    set_file = open

@app.errorhandler(404)
def error404():
    error = '404'
    return render_template('error.html', error=error)