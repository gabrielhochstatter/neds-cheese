from flask import Flask, render_template
from model import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shop')
def shop():
    cheese_amount = calculate_cheese(19.99, 3.24, gbp_to_usd_rate, eur_to_usd_rate)
    return render_template('shop.html', cheese_amount=cheese_amount)
