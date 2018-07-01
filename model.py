import requests

APP_ID = '56745ada79314950a0f144ca6c02908f'

response = requests.get('https://openexchangerates.org/api/latest.json?app_id=' + APP_ID)

eur_to_usd_rate = response.json()['rates']['EUR']
gbp_to_usd_rate = response.json()['rates']['GBP']

def convert(amount, exchange_rate):
    return amount / exchange_rate


def calculate_cheese(gbp_total_amount, eur_price, gbp_rate, eur_rate):
    result = convert(gbp_total_amount, gbp_rate) / convert(eur_price, eur_rate)
    return int(result)
