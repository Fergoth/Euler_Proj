# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sq_sum_1_n(n):
    return (n * (n + 1) // 2) ** 2


def sum_sq_1_n(n):
    return ((2 * n + 1) * (n + 1) * n) // 6


def answer(n):
    print(sq_sum_1_n(n) - sum_sq_1_n(n))


answer(100)
