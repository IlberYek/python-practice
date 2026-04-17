# Gas Station Simulator
# I decided to create a simple gas station simulator in Python. The simulator will allow users to purchase fuel, check their balance, and view their transaction history.
# I'll make prices for different types of fuel, and the prices will be according to the current Turkish market rates. 
# I'm going to use benzin, dizel and LPG 

# Benzin costs 62,56 TL
# Dizel costs 71,45 TL
# LPG costs 34,39 TL

wallet = 1000 # Starting balance for the user
prices = {"BENZIN" : 62.56, "DIZEL" : 71.45, "LPG" : 34.39} # Fuel prices in Turkish Lira
storage = 50 # Storage capacity for fuel in liters
current_storage = 0 # Current storage level

secim = input("What type of fuel would you like to purchase? (BENZIN, DIZEL, LPG): ").strip().upper() # User input for fuel type, converted to uppercase for consistency
secim2 = input("How many liters would you like to purchase? (Max 50 liters): ").strip() # User input for the amount of fuel to purchase, as a string

if secim not in prices: # Check if the selected fuel type is valid
    print("Invalid fuel type selected.")

if not secim2.isdigit(): # Check if the input for liters is a valid number
    print("Invalid input for liters. Please enter a number.")

if secim in prices and secim2.isdigit(): # If both inputs are valid, proceed with the transaction
    liters = int(secim2) # Convert the liters input to an integer
    totalcost = liters * prices[secim] # Calculate the total cost of the fuel
    if liters > storage: # Check if the requested liters exceed storage capacity
        print("Sorry, we don't have that much fuel in storage.")
    elif liters <= storage: # If the requested liters are within storage capacity
      
        if totalcost > wallet: # Check if the user has enough money to make the purchase
            print("You don't have enough money to make this purchase.")
        else: # If the user has enough money, complete the transaction
            wallet -= totalcost # Deduct the total cost from the user's wallet
            current_storage += liters # Add the purchased liters to the current storage
            print(f"You have successfully purchased {liters} liters of {secim}. Your remaining balance is {wallet:.2f} TL. Current storage level: {current_storage} liters.")
