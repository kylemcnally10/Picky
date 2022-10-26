from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Round:

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# create

    @classmethod
    def save_round(cls):
        query = "INSERT INTO rounds (created_at) values (NOW());"
        # I need a function that joins the user with the room code.
        # Then, when a separate user puts that code in on their end, it joins
        # them with the room code and they are then able to search and pick their restaurants.

        return connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def save_relation(cls, data):
        query = "INSERT INTO rounds_has_users ( round_id , user_id ) values ( %(round_id)s , %(user_id)s );"
        # I need a function that joins the user with the room code.
        # Then, when a separate user puts that code in on their end, it joins
        # them with the room code and they are then able to search and pick their restaurants.

        return connectToMySQL(DATABASE).query_db(query, data)


# validator

    @staticmethod
    def validate_round(data: dict) -> bool:
        is_valid = True
    # checks to see if email is in system
        query = "select * from rounds where room_code = %(room_code)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) >= 1:
            is_valid = False

        return is_valid
