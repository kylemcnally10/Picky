from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask_app import DATABASE
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:

    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# create
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( full_name , username , email , password ) VALUES ( %(full_name)s , %(username)s , %(email)s , %(password)s );"

        return connectToMySQL(DATABASE).query_db(query, data)

# read
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(user)
        return users

    @classmethod
    def get_one_by_email(cls, data: dict) -> object:
        query = "SELECT * FROM users where email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False

        return cls(results[0])

# update


# validators

    @staticmethod
    def validate_user(data: dict) -> bool:
        is_valid = True

        # first name must be submitted
        if len(data['full_name']) <= 1:
            flash("Full name is required", "err_user_full_name")
            is_valid = False

        # last name must be submitted
        if len(data['username']) <= 1:
            flash("Username is required", "err_user_username")
            is_valid = False

        # checks to see if email is in system
        query = "select * from users where username = %(username)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) >= 1:
            flash("Username already taken.", "err_user_username")
            is_valid = False

        # checks to see if email is in system
        query = "select * from users where email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) >= 1:
            flash("Email already taken.", "err_user_email")
            is_valid = False

        # email must be submitted and in the correct format
        if len(data['email']) <= 0:
            flash("Email is required", "err_user_email")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address", "err_user_email")
            is_valid = False

        # password length
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters", "err_user_password")
            is_valid = False

        # confirm password length and match
        if len(data['password']) <= 0:
            flash("Please confirm password", "err_user_confirm")
            is_valid = False
        elif data['confirm'] != data['password']:
            flash("Passwords do not match!", "err_user_confirm")
            is_valid = False

        if is_valid == True:
            flash("Registration was successful!\n\nPlease log in.", 'success_user')

        return is_valid

    @staticmethod
    def validate_search(data: dict) -> bool:
        is_valid = True

        # Term must be submitted
        if len(data['term']) <= 1:
            flash("Term is required", "err_user_search_term")
            is_valid = False

        # Location must be submitted
        if len(data['location']) <= 1:
            flash("Location is required", "err_user_search_location")
            is_valid = False

        # checks to see if email is in system
        if len(data['price']) <= 1:
            flash("Price is required", "err_user_search_price")
            is_valid = False

        # checks to see if email is in system
        if len(data['delivery']) <= 1:
            flash("Delivery is required", "err_user_search_delivery")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data: dict) -> bool:
        """will validate info from form before going into the database

        Args:
            data (dict): _description_

        Returns:
            bool: _description_
        """
        is_valid = True

        # email must be submitted and not exist
        if len(data['email']) <= 0:
            flash("Email is required", "err_user_login_email")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address", "err_user_login_email")
            is_valid = False

        return is_valid
