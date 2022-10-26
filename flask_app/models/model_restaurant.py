from flask import flash, session


class Restaurant:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.is_closed = data['is_closed']
        self.rating = data['rating']
        self.review_count = data['review_count']
        self.location = data['location']['address1']
        self.url = data['url']
        self.image_url = data['image_url']
