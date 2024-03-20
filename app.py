from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = 'Mot de passe invalide'
    if request.method == 'POST':
        if valid_passwd(request.form['valid_login']):
            return set_screen(request.form['test_input'],request.form['Scroll_input'], request.form['opacity_input'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('error.html', error=error)

def valid_passwd(passwd):
    if passwd == "123456":
        return

def set_screen(text, scroll, opacity):
    set_file = open('info.txt', 'a')
    set_file.write(text)
    set_file.close()

    set_file = open

@app.errorhandler(404)
def error404():
    error = '404'
    return render_template('error.html', error=error)