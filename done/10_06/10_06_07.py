from functools import partial

def multiply(a, b, с):
    return a * b * с


def multiply_curried(a: int):
    def inner1(b: int):
        def inner2(c: int):
            return a * b * c
        return inner2
    return inner1

result1 = multiply_curried(5)(3)(4)
result2 = partial(multiply, 2, 2)

print(result1)
print(result2(3))
