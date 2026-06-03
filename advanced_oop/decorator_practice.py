# Készíts egy Python dekoratort ami kepes lemerni es printelni egy fugveny idokomplxitasat, azaz az idot ami a futtatasahoz kellett.
# PL:
# @timeit_decorator
# def comprehension():
#     return [x**2 for x in range(3000000)]

# comprehension took 767.8432464599609


from typing import Any, Generator
import time


def timeit_decorator(fn):
    def timer(*args) -> Any:
        start_time = time.time()
        results = fn(*args)
        stop_time = time.time()

        print(f"comprehension took: {stop_time - start_time}")
        return results

    return timer


@timeit_decorator
def comprehension() -> list[int]:
    return [x**2 for x in range(3000000)]


@timeit_decorator
def generator() -> Generator:
    return (x**2 for x in range(3000000))


comprehension()
generator()
