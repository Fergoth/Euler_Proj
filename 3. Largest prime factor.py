#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def max_prime_factor(n):
    i = 2
    ans = 1
    while n > 1:
        while n%i ==0:
            n = n//i
            ans = i
        i+=1
    return ans

print(max_prime_factor(600851475143))