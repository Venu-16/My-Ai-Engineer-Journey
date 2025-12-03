from flask import *

app = Flask(__name__)


@app.route('/')
def vm():
    return 'prajwala'

#url building url_for() used
@app.route('/admin')
def admin():
    return 'this is me'

@app.route('/student')
def student():
    return 'this is me'

@app.route('/staff')
def staff():
    return 'this is me'
@app.route('/user<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'student':
        return redirect(url_for('student'))
    if name == 'staff':
        return redirect(url_for('staff'))


if __name__=='__main__':
    app.run()