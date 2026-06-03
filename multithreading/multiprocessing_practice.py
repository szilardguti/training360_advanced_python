# A multithreading fejezethez készített feladat megoldást alakítsd át úgy,
# hogy multiprocessing modult használva is fusson ugyan az a megoldás.
#  Mérd le mind a két megoldáshoz szükséges időt.

import queue
import random
from multiprocessing import Queue, Process, Pool, Manager
import time


class CalculatorProcess(Process):
    def __init__(self, queue: Queue):
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


def test_own_processes(number_count: int, process_count: int = 5):
    rand_nums = (random.randint(1, 100000000) for _ in range(number_count * 2))
    q = Queue(number_count)  # nagyon fontos, hogy ez syncronized legyen!
    for _ in range(number_count):
        t = (next(rand_nums), next(rand_nums))
        q.put(t)

    processes = [CalculatorProcess(q) for _ in range(process_count)]

    start_time = time.time()
    for thread in processes:
        thread.start()

    for thread in processes:
        thread.join()
    stop_time = time.time()
    print(f"finished in {stop_time - start_time}")


# 2. Alakítsd át a megoldást, hogy használjon ThreadPoolExecutor.
def calculate(queue):
    while not queue.empty():
        i1, i2 = queue.get()
        addition = i1 + i2
        print(f"{i1}+{i2}={addition}")
        multip = i1 * i2
        print(f"{i1}*{i2}={multip}")


def test_pool_processes(number_count: int, process_count: int = 5):
    with Manager() as manager:
        queue = manager.Queue(number_count)
        rand_nums = (random.randint(1, 100000000) for _ in range(number_count * 2))
        num_pairs = [(next(rand_nums), next(rand_nums)) for _ in range(number_count)]
        for tup in num_pairs:
            queue.put(tup)

        start_time = time.time()
        with Pool(processes=process_count) as pool:
            pool.map(calculate, [queue] * process_count)
        stop_time = time.time()
        print(f"finished in {stop_time - start_time}")


if __name__ == "__main__":
    test_own_processes(100000)

    test_pool_processes(100000)
