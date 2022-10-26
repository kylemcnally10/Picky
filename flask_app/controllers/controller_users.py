from flask_app import app, bcrypt
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User

# create


@app.route('/process/user', methods=['POST'])
def create_user():

    is_valid = User.validate_user(request.form)

    if not is_valid:
        return redirect('/')

    hash_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        'password': hash_password
    }
    User.save(data)
    return redirect("/")


# read


# update

# delete
