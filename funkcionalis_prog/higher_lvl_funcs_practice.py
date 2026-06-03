# 1. task
# Készíts egy Python függvény gyártó függvényt, ami képes futás közben olyan függvényeket előállítani melyek
# megadott számmal való oszthatóságot képesek megállapítani.
# Készítsd el az első 10000 számmal való oszthatóságot megállapító
# függvényeket és teszteld pár példa számmal (2343453 milyen számokkal osztható)

# PL:
# is_div_2 = make_is_div(2)
# is_div_2(234) -> True

from typing import Callable


def make_is_div(dividable_with: int) -> Callable[[int], bool]:

    def is_div(x: int) -> bool:
        return x % dividable_with == 0

    return is_div


is_div_2 = make_is_div(2)
print(is_div_2(20))
print(is_div_2(21))

dividens = []
for i in range(1, 10000 + 1):
    is_div_i = make_is_div(i)
    is_dividable = is_div_i(2343453)
    if is_dividable:
        dividens.append(i)

print(dividens)


# 2. task
# Készíts egy saját magasabb rendű függvényt.
# A függvény várjon el a bemenetén egy string listát és egy függvényt.
# A függvény nyomtassa ki az összes elemet a listából miután meghívta a függvényt az adott elemre.


def apply(func_to_apply: Callable, strings: list[str]):
    applied_list = list(map(func_to_apply, strings))
    print(applied_list)


ls = ["Teszt", "Elek", "hello", "World", "!"]

apply(lambda s: s.upper(), ls)
