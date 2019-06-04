#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
    return n == n[::-1]

ans = 0
for i in range (999, 100,-1):
    for j in range(999,100,-1):
        if i*j > ans and is_palindrome(str(i*j)):
            ans = i*j

print(ans)
