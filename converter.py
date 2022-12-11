
import requests
import json

import config


def pretty(number):
    return '{:,}'.format(round(number, 2)).replace(',', ' ')


def get_rates():
    to_currencies = 'EUR,USD,TRY,GEL,KZT,RUB'
    from_currency = 'RUB'

    # url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={to_currencies}&base={from_currency}"

    payload = {}
    headers = {
        "apikey": config.API_TOKEN
    }

    # response = requests.request("GET", url, headers=headers, data=payload)
    # status_code = response.status_code
    # rates = json.loads(response.text)["rates"]

    result = '{ "success":"True", "timestamp": 1668101330,"base": "RUB","date": "2022-11-10","rates": {"EUR": 0.016239,"USD": 0.016495,"TRY": 0.305008,"GEL": 0.044694,"KZT": 7.702463,"RUB": 1}}'

    return json.loads(result)["rates"]


def get_coef(amount, rate):
    return amount / rate


def get_converted(amount, base_currency):
    rates = get_rates()

    base_coef = get_coef(amount, rates[base_currency])

    print(f"{pretty(amount)} {base_currency} = ")
    print(f"----------------")

    for currency in rates:
        if currency != base_currency:
            print(f"{pretty(rates[currency] * base_coef)} {currency}")


