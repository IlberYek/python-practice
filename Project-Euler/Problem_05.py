# Project Euler - 5
# Question:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# I will write 2 different solutions to this problem. The first one is a brute-force approach, and the second one is an optimized approach using the least common multiple (LCM).

sayi = 20 

while True:
    hepsi_bolunuyor_mu = True

    for bolen in range (11, 21): # We only need to check from 11 to 20, because any number that is divisible by 20 will also be divisible by 1 to 10.
        if sayi % bolen != 0:
            hepsi_bolunuyor_mu = False
            print(sayi) # It'll take some time, so I will print the number that is being checked to see the progress.
            break
    if hepsi_bolunuyor_mu == True:
     print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: {sayi}")
     break
    
    sayi += 20

# This one would take a lot of time, but it will find the answer eventually. Now, let's write the optimized approach using LCM. 
# I'll write it on another file. 
