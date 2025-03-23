from todo import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return f"<User: {self.username}>"


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    created_by  = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default = False)


    def __init__(self, created_by, title, desc, state = False):
        self.created_by = created_by
        self.title = title
        self.desc = desc
        self.state = state

    def __repr__(self):
        return f"<Todo: {self.title}>"

