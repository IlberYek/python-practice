# Project Euler - 9
# Question:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1, 500): # a < b < c, so a must be less than 500
    for b in range(a, 500): # b must be greater than a and less than 500. No need to check for b in range 
        c = 1000 - a - b 
        if a*a + b*b == c*c:
            if a < b: # Ensure a < b  Otherswise, we might find the same triplet in a different order.
                print(f"The Pythagorean triplet is: {a}, {b}, {c}")
                print(f"The product abc is: {a * b * c}")
