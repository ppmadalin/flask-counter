from flask import Blueprint
from .models import Counter
from application import db

counter_app = Blueprint('counter_app', __name__)


@counter_app.route('/')
def init():
    counter = Counter.query.first()
    if not counter:
        counter = Counter(1)
        db.session.add(counter)
        db.session.commit()
    else:
        counter.count += 1
        db.session.commit()
    return f"<h1>Counter: {str(counter.count)}</h1>"
