from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://httpbin.org/ip')
    return 'Your IP is {0}'.format(response.json()['origin'])
