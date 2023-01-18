import csv
import requests

url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

headers = {
    'content-type': 'application/json'
}

order = {
    'asset': 'USDT',
    'countries': [],
    'fiat': 'RUB',
    'page': 1,
    'payTypes': [],
    'publisherType': None,
    'rows': 10,
    'tradeType': 'BUY',
}

with open('bin_test.csv', 'w', encoding='cp1251', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        (
            'Продавец',
            'Цена',
            'Доступно',
            'Лимит',
            'Ссылка на ордер'
        )
    )

page = requests.post(url, headers=headers, json=order).json()
for i in page['data']:
    nick = i['advertiser']['nickName']
    price = i['adv']['price']
    available = i['adv']['tradableQuantity']
    min_limit = i['adv']['minSingleTransAmount']
    max_limit = i['adv']['maxSingleTransAmount']
    link = 'https://p2p.binance.com/ru/advertiserDetail?advertiserNo=' + i['advertiser']['userNo']
    print(f'Продавец: {nick} Цена: {price} Доступно: {available} Лимит: {min_limit} - {max_limit} Ссылка на ордер: {link}')

    with open('bin_test.csv', 'a', encoding='cp1251', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            (
                nick,
                price,
                available,
                min_limit + '-' + max_limit,
                link,
            )
        )
