# Project Euler - 5 Optimised
# Question: 
# # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# We won't use brute-force this one. We need 2 functions for this.
import math
import functools # These two will work.

def gcd(x, y):
    return math.gcd(x, y) # We did this to shorten and simplify the code. We can use math.gcd directly, but this way it looks cleaner.

def lcm(x,y): 
    return (x * y) // gcd(x, y) # This function will calculate the least common multiple of two numbers. We will use this function to calculate the LCM of a list of numbers.

liste = range(1, 21)

result = functools.reduce(lcm, liste) # This will apply the lcm function cumulatively to the items of the list, from left to right, so as to reduce the list to a single value. In this case, it will calculate the LCM of all the numbers from 1 to 20.

print(result)
