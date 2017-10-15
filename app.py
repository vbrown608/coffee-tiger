from flask import Flask
from move_motor import Chime
app = Flask(__name__)
chime = Chime()

@app.route('/ding')
def index():
  chime.ring()
  return "ding."

@app.route('/gitlab')
def gitlab():
  pipeline = request.get_json()
  if pipeline['object_attributes']['status'] == 'success':
    chime.ring()
