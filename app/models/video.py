from app import db
from datetime import datetime, timedelta

class Video(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    total_inventory = db.Column(db.Integer)
    available_inventory = db.Column(db.Integer)
    # rentals = db.relationship("Rental", backref = "video", lazy = True)

    def to_dict(self):
        response={
        "id": self.id,
        "title": self.title,
        "release_date": self.release_date,
        "total_inventory": self.total_inventory,
        }
        return response

