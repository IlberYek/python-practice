# Project Euler - 3
# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# I will create a 'prime' function here. I will make it check square root of that number.

def en_buyuk_asal_carpan(sayi):
    bolen = 2 # We start with the smallest prime number, which is 2.
    while bolen * bolen <= sayi:
        if sayi % bolen == 0:
            sayi //= bolen
        else:
            bolen += 1
    return sayi

print(en_buyuk_asal_carpan(600851475143))
