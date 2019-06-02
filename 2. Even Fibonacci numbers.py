def fib():
    fib_list = [1,2]
    fib_curr = 2
    while fib_curr < 4000000:
        fib_curr = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_curr)
        yield fib_curr

ans = 2
for i in fib():
    ans = ans + i if i%2==0 else ans

print(ans)