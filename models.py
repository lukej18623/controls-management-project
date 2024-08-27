from app import db
from datetime import datetime, timezone

class Control(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g. active, inactive
    date = db.Column(db.DateTime, default=datetime.now(timezone.utc))  # record date and time
