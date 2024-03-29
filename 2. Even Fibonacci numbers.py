# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib():
    fib_list = [1, 2]
    fib_curr = 2
    while fib_curr < 4000000:
        fib_curr = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_curr)
        yield fib_curr


ans = 2
for i in fib():
    ans = ans + i if i % 2 == 0 else ans

print(ans)
