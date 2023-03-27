from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # username column
    username = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return f"User: {self.username}"

class Tweet(DB.Model):
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    #text column
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    #user_id column (foreign / secondary key)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nulable=False)
    # user column creates a two-way link between a user object and a tweet
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"Tweet: {self.text}"
