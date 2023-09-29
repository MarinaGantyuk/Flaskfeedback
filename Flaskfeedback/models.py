from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt

#bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    db.init_app(app) 



class User(db.Model):
    __tablename__ = "users"
    
    username = db.Column(
        db.String(20),
        nullable=False,
        unique=True,
        primary_key=True,
    )
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    feedback = db.relationship("Feedback", backref="user", cascade="all,delete")


    def to_dict(self):
        """Serialize cupcake to a dict of cupcake info."""

        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "feedback" : self.feedback

        }

class Feedback(db.Model):
    """Feedback."""

    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(
        db.String(20),
        db.ForeignKey('users.username'),
        nullable=False,
    )



    