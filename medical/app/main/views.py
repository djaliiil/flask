from flask import Blueprint, render_template
from app.models.event import Event
 

main = Blueprint('main', __name__)


@main.route('/')
def index():
	event = Event.query.all()
	print('event')
	print(event)
	return render_template('main/index.html',events=event)
 