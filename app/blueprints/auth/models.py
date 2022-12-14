from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    body = db.Column(db.String(1200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1200))
    date_created = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Ineger, db.ForeignKey('post.id'))