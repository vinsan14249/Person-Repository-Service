from application import db
from flask_sqlalchemy import SQLAlchemy

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    user_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer, nullable=False)


db.create_all()
db.session.commit()