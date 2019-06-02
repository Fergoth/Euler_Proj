# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def mult_3_or_5(number):
    return not (number % 3 and number % 5)


ans = 0
for i in range(1, 1000):
    if mult_3_or_5(i):
        ans += i
print(ans)
