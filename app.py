from datetime import datetime, timedelta
from flask import Flask, json, render_template, url_for, request, redirect, jsonify
from flask.helpers import make_response
import jwt
import functools
import bcrypt
from connection import Database


app = Flask(__name__)
app.config['JWT_KEY'] ='soiqwueho28973987265362#^$%#'

# Connecting to the database
db = Database()


@app.context_processor
def handle_context():
    '''Inject object into jinja2 templates.'''
    return dict(jsonify = jsonify)

def secure_site(f):
    @functools.wraps(f)
    def secure_wrapper(*args, **kwargs):

        token = request.cookies.get('token')
        
        if not token:
            return "No token provided."
        
        try:
            auth_data = jwt.decode(token, app.config['JWT_KEY'], algorithms=["HS256"])
        except:
            return "Token invalid."

        return f(*args, **kwargs, auth_data = auth_data)
    return secure_wrapper

@app.route('/')
def index():
    return 'This is the index page for the Enrichery web app.'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        userExists = db.get_user({"username":username})
        #print(userExists)
        if userExists is not None:
            print('user exists')
            if userExists["userPassword"] == password:
                print('login successful.')
                return render_template("home.html")
        else:
            return render_template('error.html'), {"Refresh": "4; url=/login"}

@app.route('/logout')
def logout():
    return 'You have been logged out.'

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        states = db.getStates()
        return render_template("register.html", states = states)
    elif request.method == "POST":
        return f"User created with state {request.form.get('state')}"

@app.route('/home')
@secure_site
def home(auth_data = None):
    return f"{auth_data['username']} you are logged in!"

# students page with diff request methods.
# tables will be shown with editing functions add/edit/delete/etc.
# data entered will be replaced with sql information once DB is up and running.
@app.route('/students', methods=['POST','GET', 'DELETE', 'PUT'])
def students():
    if request.method=='GET':
        return render_template('students.html', studentName='John Doe', studentID='0001', subjects='Sample Text',
                               grades='Sample Text', status='Active')
    else:
        #template text showcasing an error or something in else in the future. will return an error page or something.
        return render_template('error.html', studentName='John Doe')


@app.route('/coaches')
def staff():
    return 'coaches'



"""
Debug mode to run the code without having to
run it from the terminal/cmd. Please remove it during
production.
"""
if __name__=='__main__':
    app.run(debug=True)
