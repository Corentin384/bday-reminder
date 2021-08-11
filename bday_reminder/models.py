from bday_reminder import db


class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    person_name = db.Column(db.String(32))
    person_birthday = db.Column(db.String(10))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pseudo = db.Column(db.String(32))
    password = db.Column(db.String(128))
    birthday = db.Column(db.String(10), default=None)
