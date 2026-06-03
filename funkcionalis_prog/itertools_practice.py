# 1. task
# Készíts egy Python programot ami egy parancssori progress indikátort forg
# megjeleniteni 5 masodpercig. Az indikator legyen karakteres (”\|/-”). Használd az itertools könyvtárat.
#
# (segítség, a cycle() fuggvény jól jöhet, illetve az is, hogy a print függvénynél a end='\r' opcionális paraméter visszatér a sor elejére)

from typing import Collection
import itertools as it
import time


def loading_icon(wait_time_sec: int = 5) -> None:
    icons = "abcd"

    start_time = time.time()
    dt = 0

    while dt < wait_time_sec:
        icon_it = it.cycle(icons)
        print(next(icon_it), end="\r")
        dt = time.time() - start_time
        time.sleep(0.1)

    print("loading done!")


loading_icon(5)

# 2. task
# Készits Python függvényt, ami csoportokba rendez embereket. Bonusz feladat: randomizald a kivalasztast.


def shift_maker(people_iterable: Collection[str], number_of_shifts: int):
    people_count_per_shift = len(people_iterable) / number_of_shifts
    return it.combinations(people_iterable, int(people_count_per_shift))


strs = ["a", "b", "c", "d"]
print(list(shift_maker(strs, 2)))

# shift_maker(people_iterable, number_of_shifts)
# shift_maker([‘Peter’, ‘Julia’, ‘Andrew’, ‘Bobby’, ‘Margo’, ‘Bill’, ‘Alice’, ‘Anna’], 3) ->
