from Prime import gen_primes

ans = 0
for prime in gen_primes():
    if prime > 2000000:
        break
    else:
        ans+=prime

print(ans)