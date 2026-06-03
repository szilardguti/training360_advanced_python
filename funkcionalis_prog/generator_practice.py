import random
from typing import Any, Generator


"""
1) Írj egy Python generátor kifejezést (generator expression) ami kiszámítja a köbét minden páros számnak
az alábbi listából [10,3,7,9,11,33,22,8,2]. Használd a `list` függvényt, hogy az eredményeket egy listában tudd prezentálni.
"""

li = [10, 3, 7, 9, 11, 33, 22, 8, 2]

fn_gen = (x**3 for x in li if x % 2 == 0)

print(list(fn_gen))
"""

2) Készítsünk Python generátor piplinet, azaz ágyazzunk egymásba több generátor kifejezéséseket.

a) Írj egy python generátor kifejezést ami a `random.randint` függvény segítségével generál legfeljebb 100 random számot 1 es 1000 között.

b) Írj egy másik kifejezést ami négyzetre négyzetre emeli a számokat

c) Írj egy harmadik kijezést ami stringge konvertálja az értékeket

d) Ellenőrzés képpen irasd ki az összes egyedi stringet amit kaptunk. (Hasznos lehet a `set` halmaz adatszerkezet)

"""


def random_nums() -> Generator[int]:
    i = 0
    while i < 1000:
        yield random.randint(1, 1000)


rand_nums = (random.randint(1, 1000) for _ in range(1000))

sqr_nums = (x**2 for x in rand_nums)

str_conv = (str(i) for i in sqr_nums)

print(set(str_conv))

# 3) írj egy Python generátor függvényt ami kiválasztja az egyedi elemeket bármilyen listából.


def unique(lr: list) -> Any:
    for elem in set(lr):
        yield elem


lr = [1, "Tamas", 2, 1, 5, 32, 2, 1, "Agi", 33.3, 33.3, 33.3]
u = unique(lr)

print(next(u))  # -> 1
print(next(u))  # -> ’Tamas’
print(next(u))  # -> 2
print(next(u))  # -> 5
print(next(u))  # -> 32
print(next(u))  # -> ’Agi’
print(next(u))  # -> 33.3
