from flask import Flask, render_template, session, redirect
from user.routes import user_bp
import pymongo
from functools import wraps

client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system
app = Flask(__name__)
app.secret_key = 'secretkey'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    
    return wrap

app.register_blueprint(user_bp)

@app.route('/')
def view():
    return render_template('view.html')

@app.route('/register')
def register():
    return render_template('registiration.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    posts = list(db.blog_db.find())
    return render_template('dashboard.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
