# Basic Bazaar Simulator

wallet = 100
inv = []
prices = {"apple" : 10, "pear" : 20, "banana" : 30}

while True:
    print(f"Your current money : {wallet}")
    choice = input("What do you want to do? (buy, sell, go away): ").strip().lower()
    if choice == "buy":
        fruitchoice = input("What would you like to buy? : ").strip().lower()
        if fruitchoice == "apple":
            if wallet >= prices["apple"]:
                wallet -= prices["apple"]
                inv.append("apple")
                print(f"You successfully bought an apple! Your current inventory: {inv}")
            else:
                print("You don't have enough money.")
        if fruitchoice == "pear":
            if wallet >= prices["pear"]:
                wallet -= prices["pear"]
                inv.append("pear")
                print(f"You successfully bought a pear! Your current inventory: {inv}")
            else:
                print("You don't have enough money.")
        if fruitchoice == "banana":
            if wallet >= prices["banana"]:
                wallet -= prices["banana"]
                inv.append("banana")
                print(f"You successfully bought a banana! Your current inventory: {inv}")
            else:
                print("You don't have enough money.")

   
    elif choice == "sell":
      sellingchoice = input("What would you like to sell? : ").strip().lower()
      if sellingchoice == "apple":
         if "apple" in inv:
          wallet += prices["apple"] + 2
          inv.remove("apple")
          print(f"You sold an apple! Your current money : {wallet}, Your inventory: {inv}")
         else:
            print("You can't sell something you don't have.")
      elif sellingchoice == "pear":
          if "pear" in inv:
             wallet += prices["pear"] + 4
             inv.remove("pear")
             print(f"You sold an pear! Your current money : {wallet}, Your inventory: {inv}")
          else:
            print("You can't sell something you don't have.")
      elif sellingchoice == "banana":
           if "banana" in inv:
             wallet += prices["banana"] + 6 
             inv.remove("banana")
             print(f"You sold an banana! Your current money : {wallet}, Your inventory: {inv}")
           else: 
              print("You can't sell something you don't have.")
   
   
    elif choice == "go away":
        if wallet < 100:
            print("You couldn't make a profit, pal. You left the bazaar..")
            break
        elif wallet == 100:
            print("It seems like you didn't even put your hands into your pockets. No profit, no loss. You left the bazaar.")
            break
        else:
            print("That's it! You made a profit today! You left the bazaar with a sily grin!") 

            break  


