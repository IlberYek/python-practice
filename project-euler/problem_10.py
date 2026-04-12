# Project Euler - 10
# Question: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Well, we may use the same function I write in question 7 to check prime numbers.
def is_prime(sayi): 
    if sayi < 2: return False

    for i in range(2, int(sayi**0.5) + 1): # We only need to check up to the square root of the number. It will make it easier adn faster.
        if sayi %i == 0:
            return False
    return True

asallarintoplami = 0 # We will keep the sum of the prime numbers in this variable.

for i in range(1, 2000000): # We will check all the numbers below 2 million.
    if is_prime(i): # If the number is prime, we will add it to the sum.
        asallarintoplami += i

print(asallarintoplami)
