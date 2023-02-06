#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
# TODO здесь ваш код

all_flowers = garden_set | meadow_set
print(all_flowers)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

doubled_flowers = garden_set & meadow_set
print(doubled_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код

garden_only_flowers = garden_set - meadow_set
print(garden_only_flowers)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код

meadow_only_flowers = meadow_set - garden_set
print(meadow_only_flowers)
