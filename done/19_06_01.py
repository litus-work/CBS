from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import math

def calc_factorial(n: int) -> int:
    return math.factorial(n)

def measure_time(executor_class, numbers):
    start = time.time()
    with executor_class() as executor:
        results = list(executor.map(calc_factorial, numbers))
    end = time.time()
    print(f"{executor_class.__name__} виконав за: {round(end - start, 2)} сек.")
    return results

if __name__ == "__main__":
    numbers = [50000 + i for i in range(5)]

    # ThreadPoolExecutor
    thread_results = measure_time(ThreadPoolExecutor, numbers)

    # ProcessPoolExecutor
    process_results = measure_time(ProcessPoolExecutor, numbers)
