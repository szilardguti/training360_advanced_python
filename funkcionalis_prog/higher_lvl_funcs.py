from functools import reduce


def pow_make(n):
    """pow of n factory"""

    def pow(x):
        return x**n

    return pow


pow_of_2 = pow_make(2)
pow_of_3 = pow_make(3)

print(pow_of_2(3))

li = [2, 4, 5, 5, 5, 15, 45, 35]
sum2 = reduce(lambda x, y: x + y, map(pow_of_2, filter(lambda x: x % 2 == 0, li)))
print(sum2)
