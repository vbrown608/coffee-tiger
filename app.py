from flask import Flask
from move_motor import Chime
app = Flask(__name__)
chime = Chime()

@app.route('/ding')
def index():
  chime.ring()
  return "ding."
