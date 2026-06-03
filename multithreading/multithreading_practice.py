# 1. Készíts egy Python függvényt, ami kiszámítja két szám összegét és szorzatát, majd kiírja ezeket.
# A függvényt futtasd le párhuzamosan 100000, 10000000 és 100000000 véletlen egész számpárra.
# Használd a threading modult.
import queue
import random
import threading
import time
import concurrent.futures


class CalculatorThread(threading.Thread):
    def __init__(self, queue: queue.Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            try:
                i1, i2 = self.queue.get(timeout=1)
                self.calculate(i1, i2)
            except queue.Empty:
                break

    def calculate(self, i1, i2):
        addition = i1 + i2
        print(f"{i1}+{i2}={addition}")

        multip = i1 * i2
        print(f"{i1}*{i2}={multip}")


def test_threading(number_count: int, thread_count: int = 5):
    rand_nums = (random.randint(1, 100000000) for _ in range(number_count * 2))
    q = queue.Queue(number_count)
    for _ in range(number_count):
        t = (next(rand_nums), next(rand_nums))
        q.put(t)

    threads = [CalculatorThread(q) for _ in range(thread_count)]

    start_time = time.time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    stop_time = time.time()
    print(f"finished in {stop_time - start_time}")


test_threading(100000, 5)
# test_threading(10000000, 5)
# test_threading(100000000, 5)


# 2. Alakítsd át a megoldást, hogy használjon ThreadPoolExecutor.
def calculate(i1, i2):
    addition = i1 + i2
    print(f"{i1}+{i2}={addition}")
    multip = i1 * i2
    print(f"{i1}*{i2}={multip}")


def test_threading(number_count: int, thread_count: int = 5):
    rand_nums = (random.randint(1, 100000000) for _ in range(number_count * 2))
    num_pairs = [(next(rand_nums), next(rand_nums)) for _ in range(number_count)]

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.map(lambda x: calculate(*x), num_pairs)
    stop_time = time.time()
    print(f"finished in {stop_time - start_time}")


test_threading(100000, 5)
# test_threading(10000000, 5)
# test_threading(100000000, 5)
