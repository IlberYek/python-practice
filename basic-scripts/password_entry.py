# Password Entry

weakcombinations = ["123", "password", "123456", "12345678", "qwerty", "abc123", "monkey", "letmein", "dragon", "111111"]

while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password is too short. Please enter at least 8 characters.")
        continue

    forbiddenfound = False

    for forbidden in weakcombinations:
        if forbidden in password:
            forbiddenfound = True # If there's weak combination in the password, it won't let it be accepted.
            break
    if forbiddenfound:
        print("Password contains a weak combination. Please choose a stronger password.")
        continue
    else:
        print("Password accepted.")
        break
