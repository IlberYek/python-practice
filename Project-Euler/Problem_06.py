# Project Euler - 6
# Question: 
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

karelerintoplami = 0 # the sum of the squares
toplamlarinkaresi = 0 # the square of the sum

toplam = 0

for i in range(1, 101):
    toplam += i

toplamlarinkaresi = toplam ** 2 # we calculate the square of the sum after we have calculated the sum. We can also calculate the sum of the squares in the same loop, but I prefer to keep them separate for clarity.
print(toplamlarinkaresi)

for i in range(1, 101):
    karelerintoplami += i ** 2
print(karelerintoplami)
fark = toplamlarinkaresi - karelerintoplami
print(fark)
 
