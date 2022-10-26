from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_restaurant import Restaurant
import requests


@app.route('/process', methods=["POST"])
def process():
    session['search_term'] = request.form['term']
    session['search_location'] = request.form['location']
    session['active_slide'] = 3
    return redirect("/results")


@app.route('/results')
def search_results():
    API_KEY = "CXHzHSza09AFAe5RV5N0y_e-O8a0k4tFdFqGznQYtnvnhtu07PxKjaRl0zx3kkXvraPc1S86SsX6Lk_NgbUoJBf0WI2b-_LHdtq3Zn-riRNEUQQ-5i5ofolRUgIAY3Yx"

    TERM = session['search_term']
    LOCATION = session['search_location']
    LIMIT = 10

    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
    url_params = {
        'term': TERM,
        'location': LOCATION,
        'limit': LIMIT
    }

    response = requests.request('GET', url, headers=headers, params=url_params)
    all_restaurants = []
    for business in response.json()["businesses"]:
        all_restaurants.append(Restaurant(business))

    print(session["search_term"])
    print(session["search_location"])
    print(session["active_slide"])
    print(all_restaurants[0])
    print(all_restaurants[1])
    print(all_restaurants[2])
    print(all_restaurants[3])
    print(all_restaurants[4])
    print(all_restaurants[5])
    print(all_restaurants[6])
    print(all_restaurants[7])
    print(all_restaurants[8])
    print(all_restaurants[9])
    return render_template("results.html", restaurants=all_restaurants)
