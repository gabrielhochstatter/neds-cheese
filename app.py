from flask import Flask, render_template, url_for
from model import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shop')
def shop():
    cheese_amount = calculate_cheese(19.99, 3.24, gbp_to_usd_rate, eur_to_usd_rate)
    return render_template('shop.html', cheese_amount=cheese_amount)


@app.route('/shop_japan')
def shop_japan():
    cheese_amount = calculate_cheese(4000, 3.24, yen_to_usd_rate, eur_to_usd_rate)
    return render_template('shop.html', cheese_amount=cheese_amount)
