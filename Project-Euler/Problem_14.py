# Project Euler - 14
# Question:
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# Note: Once the chain starts the terms are allowed to go above one million.

dict = {} # I will use a dictionary to store the length of the chain for each number. It will be easier to look up the length of the chain for a number if I have already calculated it.
dict[1] = 1 # The length of the chain for 1 is 1.

en_uzun_zincir = 0 # Longest chain
sonuc_sayisi = 0 

for i in range(1, 1000000):
    n = i # I'll use n to avoid confusion.
    counter = 1 
    while n != 1:
        if n in dict:
            counter += dict[n] 
            break
       
        if n % 2 == 0:
            n = n // 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1
    dict[i] = counter
    if counter > en_uzun_zincir:
        en_uzun_zincir = counter
        sonuc_sayisi = i    

print(sonuc_sayisi)
print(en_uzun_zincir)
