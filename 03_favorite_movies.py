#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код


print(my_favorite_movies[0:10])
print(my_favorite_movies[-15:-1] + my_favorite_movies[-1])  # ммм, хуета
print(my_favorite_movies[12:25])
print(my_favorite_movies[35:40])

# Ну а если по-нормальному:

my_favorite_movies = my_favorite_movies.split(', ')
print(my_favorite_movies, type(my_favorite_movies))
print(my_favorite_movies[0], my_favorite_movies[-1], my_favorite_movies[1], my_favorite_movies[-2], sep='\n')
