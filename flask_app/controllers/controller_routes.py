from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models import model_pick, model_user, model_restaurant


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect("/dashboard")
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("dashboard.html")


@app.route('/new')
def new_room():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("new_search.html")


@app.route('/join')
def join_room():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("join_search.html")


@app.route('/new/criteria')
def criteria():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("criteria.html")


@app.route('/login', methods=['POST'])
def login():
    data = {"email": request.form["email"]}
    if not model_user.User.validate_login(data):
        return redirect("/")
    user_in_db = model_user.User.get_one_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "err_user_login_email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "err_user_login_password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['full_name'] = user_in_db.full_name
    session['username'] = user_in_db.username
    return redirect("/dashboard")


@app.route('/logout')
def logout():
    if 'user_id' in session:
        del session['user_id']
    if 'full_name' in session:
        del session['full_name']
    if 'username' in session:
        del session['username']
    if 'round_id' in session:
        del session['round_id']
    if 'rounds_has_users_id' in session:
        del session['rounds_has_users_id']
    return redirect('/')
