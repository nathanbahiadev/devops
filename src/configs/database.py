from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class PingModel(db.Model):
    __tablename__ = 'pings'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
