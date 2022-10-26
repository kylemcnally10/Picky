from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_pick import Pick


@app.route('/save/pick', methods=["POST"])
def save_pick():

    data = {
        'name': request.form['name'],
        'rating': request.form['rating'],
        'review_count': request.form['review_count'],
        'location': request.form['location'],
        'url': request.form['url'],
        'image_url': request.form['image_url'],
        'rounds_has_users_id': session['rounds_has_users_id'],
        'rounds_has_users_round_id': session['round_id'],
        'rounds_has_users_user_id': session['user_id'],
    }

    Pick.save_pick(data)

    # session['active_slide'] = request.form['index']

    return redirect('/results')


@app.route('/results/combined')
def results_combined():
    if 'user_id' not in session:
        return redirect("/")
    picks = Pick.get_all_picks({'round_id': session['round_id']})
    return render_template("combined_results.html", picks=picks)


@app.route('/results/random')
def results_random():
    if 'user_id' not in session:
        return redirect("/")
    picks = Pick.get_random_from_picks({'round_id': session['round_id']})
    return render_template("random_result.html", picks=picks)
