from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Pick:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.rating = data['rating']
        self.review_count = data['review_count']
        self.location = data['location']
        self.url = data['url']
        self.image_url = data['image_url']
        self.rounds_has_users_id = data['rounds_has_users_id']
        self.rounds_has_users_round_id = data['rounds_has_users_round_id']
        self.rounds_has_users_user_id = data['rounds_has_users_user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# create


    @classmethod
    def save_pick(cls, data):
        query = "INSERT INTO picks ( name , rating , review_count , location , url , image_url , rounds_has_users_id , rounds_has_users_round_id , rounds_has_users_user_id) VALUES ( %(name)s , %(rating)s , %(review_count)s , %(location)s , %(url)s , %(image_url)s , %(rounds_has_users_id)s , %(rounds_has_users_round_id)s , %(rounds_has_users_user_id)s );"

        return connectToMySQL(DATABASE).query_db(query, data)

# read
    @classmethod
    def get_all_picks(cls, data):
        query = "SELECT * FROM picks where rounds_has_users_round_id = %(round_id)s order by rand();"
        results = connectToMySQL(DATABASE).query_db(query, data)
        picks = []
        for pick in results:
            picks.append(pick)
        return picks

    @classmethod
    def get_random_from_picks(cls, data):
        query = "SELECT * FROM picks where rounds_has_users_round_id = %(round_id)s order by rand() limit 1;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        picks = []
        for pick in results:
            picks.append(pick)
        return picks
