from flask import Flask, render_template
from model import *

app = Flask(__name__)

@app.route('/')
def index():
    cheese_amount = calculate_cheese(19.99, 3.24, gbp_to_usd_rate, eur_to_usd_rate)
    return render_template('index.html', cheese_amount=cheese_amount)
