from crypt import methods
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_round import Round


@app.route('/new/round')
def create_round():
    session['round_id'] = Round.save_round()

    data = {
        'round_id': session['round_id'],
        'user_id': session['user_id']
    }

    session['rounds_has_users_id'] = Round.save_relation(data)

    # join user on this room code

    return redirect('/new')


@app.route('/join/round', methods=["POST"])
def join_round():

    data = {
        'round_id': request.form['round_id'],
        'user_id': session['user_id']
    }

    session['rounds_has_users_id'] = Round.save_relation(data)
    session['round_id'] = data['round_id']


# join user on this room code

    return redirect('/new/criteria')
