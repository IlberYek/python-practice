# Project Euler - 7
# Question:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# I'll use a simple function. Function will check if a number is a prime or not.
def is_prime(sayi): 
    if sayi < 2: return False

    for i in range(2, int(sayi**0.5) + 1): # We only need to check up to the square root of the number. It will make it easier adn faster.
        if sayi %i == 0:
            return False
    return True

sayac = 1 # We start with 1 because we already know that the first prime number is 2, and we will start checking from 3.
sayi = 3 # We bypass 2
son_asal = 0 # Last prime number.

while sayac < 10001: 
    if is_prime(sayi):
        sayac += 1 # Sayac is counter for how many prime numbers we have found so far.
        son_asal = sayi
    sayi += 2 

print(son_asal)
