import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math

def calc_factorial(n: int) -> int:
    return math.factorial(n)

numbers = [50000 + i for i in range(10)]

start = time.time()
with ThreadPoolExecutor() as executor:
    thread_results = list(executor.map(calc_factorial, numbers))
end = time.time()
print(f"ThreadPoolExecutor виконав за: {end - start:.2f} сек.")

start = time.time()
with ProcessPoolExecutor() as executor:
    process_results = list(executor.map(calc_factorial, numbers))
end = time.time()
print(f"ProcessPoolExecutor виконав за: {end - start:.2f} сек.")
