from app import db
from hashutils import make_pw_hash

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(3000))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ### TODO add a DateTime column eventually so we can sort with respect to it.

    def __init__(self, title, body, owner):
        self.title = title
        self.body = body
        self.owner = owner

    def __repr__(self):
        return '<Blog {0}>'.format(self.title)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    pw_hash = db.Column(db.String(120))
    blogs = db.relationship('Blog', backref = 'owner')

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)