from flask import Flask
from model import *
app = Flask(__name__)

@app.route('/')
def index():
    
    return 'Your IP is {0}'.format(eur_to_usd_rate)
