import functools
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання '{func.__name__}': {end - start:.6f} секунд")
        return result
    return wrapper


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def manual_cache_decorator(func):
    cache = {}
    def wrapper(n: int):
        if n in cache:
            return cache[n]
        cache[n] = func(n)
        return cache[n]
    return wrapper


def lru_cache_10_decorator(func):
    return functools.lru_cache(maxsize=10)(func)

def lru_cache_16_decorator(func):
    return functools.lru_cache(maxsize=16)(func)

@measure_time
def run_no_cache():
    print("1 Без кешування:")
    for i in range(25):
        print(fibonacci(i), end=" ")
    print()

@measure_time
def run_manual_cache():
    print("2 Ручне кешування:")
    cached_fib = manual_cache_decorator(fibonacci)
    for i in range(25):
        print(cached_fib(i), end=" ")
    print()

@measure_time
def run_lru_cache_10():
    print("3 functools.lru_cache(maxsize=10):")
    cached_fib = lru_cache_10_decorator(fibonacci)
    for i in range(25):
        print(cached_fib(i), end=" ")
    print()

@measure_time
def run_lru_cache_16():
    print("4 functools.lru_cache(maxsize=16):")
    cached_fib = lru_cache_16_decorator(fibonacci)
    for i in range(25):
        print(cached_fib(i), end=" ")
    print()



run_no_cache()
run_manual_cache()
run_lru_cache_10()
run_lru_cache_16()