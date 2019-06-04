# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from functools import reduce

def GCD(a,b):
    while a!=0 and b!=0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return a or b

def LCD(a,b):
    return (a*b)//GCD(a,b)

def LCD_list(l):
    return reduce(LCD, l)

print (LCD_list(range(1,21)))