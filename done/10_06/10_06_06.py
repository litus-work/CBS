

def only_even_numbers(generator_func):
    def wrapper(n):
        for num in generator_func(n):
            if num % 2 == 0:
                yield num
    return wrapper

@only_even_numbers
def fibonacci_generator(n):
    """
    Generates Fibonacci sequence numbers up to the specified count.

    Args:
        n (int): The number of Fibonacci sequence elements to generate.

    Yields:
        int: Next number in the Fibonacci sequence.

    Note:
        Due to the @only_even_numbers decorator, only even numbers from 
        the sequence will be yielded.
    """

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b



for num in fibonacci_generator(20):
    print(num, end=" ")


