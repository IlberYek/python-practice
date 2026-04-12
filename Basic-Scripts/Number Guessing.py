# A little Number Guessing Game
import random
target = random.randint(1, 20)
attempts = 5

print("--- Welcome to the Number Guessing Game! ---")
print("I will think of a number between 1 and 20. You have 5 attempts. Let's see if you can guess it!")

while attempts > 0:
    print(f"\nYou have {attempts} attempts left.")
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 20:
        print("Invalid input. Please enter a number between 1 and 20.") 
    
    elif guess > target:
        print("You couldn't guess it! The number is lower.")
        attempts -= 1
    
    elif guess < target:
        print("You couldn't guess it! The number is higher.")
        attempts -= 1
    
    elif guess == target: 
     print(f"Congratulations! You guessed the number! The number was {target}") 
     break 
     
    else:
        print("Invalid input. Please enter a number between 1 and 20.")
    
if attempts == 0:
    print(f"Game Over! You've used all your attempts. The number was {target}. Better luck next time!")
