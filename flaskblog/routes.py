
from flask import  render_template, url_for, flash, redirect
from flaskblog.froms import RegisterFrom, LoginFrom
from flaskblog.models import User, Post
from flaskblog import app

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', "POST"])
def register():
    form = RegisterFrom()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}", 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', "POST"])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com':
            flash("You have Been Logged in", 'success')
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessfull, Plase Try again", 'danger')
    return render_template("login.html", title="Register", form=form)
