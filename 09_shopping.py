#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

from pprint import pprint

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
sweets = {
    'название сладости': [
        {'shop': 'название магазина', 'price': 99.99},
    ],
}
# Указать надо только по 2 магазина с минимальными ценами


# составляем список магазинов, где продается печенье:


def raschet():
    cookies = [
        {'shop': 'ашан', 'price': shops['ашан'][0]['price']},
        {'shop': 'пятерочка', 'price': shops['пятерочка'][0]['price']},
        {'shop': 'магнит', 'price': shops['магнит'][0]['price']}
       ]

    #pprint(cookies)


# составляем список стоимости печенья в магазинах
    cookies1 = []
    i = 0
    for i in range(len(cookies)):
        cookies1.append(cookies[i]['price'])
        i += 1

    #print(cookies1)

# оставляем i самых низких цен
    cookies2 = []
    i = 0
    for i in range(2):
        cookies2.append(min(cookies1))
        cookies1.remove(min(cookies1))

    #print(cookies2)

# составляем список i самых дешевых магазинов
    cookies3 = []
    n = 0
    for n in range(len(cookies2)):
        for i in range(len(cookies)):
            if cookies2[n] == cookies[i]['price']:
                cookies3.append(cookies[i])

    #print(cookies3)

    return(cookies3)

#словарь цен на продукты

cheap_price = {'Самое дешевое печенье': raschet()}

print(cheap_price)