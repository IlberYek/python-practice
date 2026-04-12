# Project Euler - 4
# Question:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# I will create a 'palindrome' function here. I will make it check if the number is a palindrome or not. 
def palindrome_check(sayi):
    sayi = str(sayi) # I will convert the number to a string to check if it reads the same both ways.
    terssayi = sayi [::-1]
    if sayi == terssayi:
        return True
    else:
        return False
    
palindromeliste = []

for i in range (100, 1000):
    for j in range (100, 1000):
        carpim = i * j
        if palindrome_check(carpim): # If the product of i and j is a palindrome, I will add it to the list.
            palindromeliste.append(carpim)
        else:
            continue

print(palindromeliste)

print(f"\n{max(palindromeliste)}")
