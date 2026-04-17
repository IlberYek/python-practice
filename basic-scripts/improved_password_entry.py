# Improved Password Entry
# We will write a better version of my Passord Entry.py code. It is going to have more and detailed criterias.
# The password must have minimum 8 characters, at least 1 number (0-9), at least 1 capitalised character and at least 1 special character.


# I prefer to use flags to check if the password meets the criteria instead of using a single variable to store the password and then checking it later. This way, we can check each criteria as we go through the password.

special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

while True: 
    has_digit = False
    has_upper = False
    has_special = False
    length_ok = False 
 
    input_password = input("Enter your password: ")
    if len(input_password) >= 8:
        length_ok = True
    
    for char in input_password:
        if char.isdigit():
            has_digit = True
    
        if char.isupper():
            has_upper = True
    
        if char in special_characters:
            has_special = True
    if length_ok == False: 
        print("Password must be at least 8 characters long.")
    if has_digit == False:
        print("Password must contain at least 1 number (0-9).")
    if has_upper == False:
        print("Password must contain at least 1 capitalised character.")
    if has_special == False:
        print("Password must contain at least 1 special character.")
    if length_ok and has_digit and has_upper and has_special:
        print("Password is valid.")
        break
