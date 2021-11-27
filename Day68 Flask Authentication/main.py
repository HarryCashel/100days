import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, send_from_directory, flash
from flask_login import UserMixin, LoginManager, login_required, login_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
db.drop_all()
db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pass_word = request.form.get('password')
        hashed_password = werkzeug.security.generate_password_hash(pass_word)

        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You have already signed up with that email, log in instead")
            return redirect(url_for('login'))

        new_user = User()
        new_user.name = request.form.get('name')
        new_user.email = request.form.get('email')
        new_user.password = hashed_password
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('secrets', name=new_user.name))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Invalid credentials. Please try again")
        if user:
            if werkzeug.security.check_password_hash(user.password, password):
                login_user(user)
                flash("You were successfully logged in")
                return redirect(url_for('secrets'))
            else:
                flash("Invalid credentials")
    return render_template("login.html", logged_in=True)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", logged_in=True)


@app.route('/logout')
def logout():
    pass


@app.route('/download<path:filename>')
@login_required
def download(filename):
    return send_from_directory('static/files', filename)


if __name__ == "__main__":
    app.run(debug=True)
