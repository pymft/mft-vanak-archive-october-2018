import json
from urllib.request import urlopen


def get_coin_data(i):
    url = "https://api.coinmarketcap.com/v2/ticker/{i}/".format(i=i)
    with urlopen(url) as req:
        return req.read().decode('utf-8')


def get_coin_trade_history(i, t1, t2):
    null = ''
    false = False
    true = True

    res = get_coin_data(789)
    res2 = eval(res)
    coin_name = res2['data']['name']

    url = "{base}/{currency}/{t1}000/{t2}000/".format(
        base="https://graphs2.coinmarketcap.com/currencies",
        currency=coin_name,
        t1=t1, t2=t2)



#
