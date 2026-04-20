# A Sales Data Visualizer
# I'll create two variables. One contains imaginary product ID's, the other one contains categories. 

iddatas = [101, 102, 101, 103, 105, 102, 101, 107, 103, 101, 105, 102, 108, 107, 101, 103, 105, 105, 102, 101] # These are the ID's
categorydatas = [
    "Electronic", "Fashion", "Electronic", "House & Living", "Fashion", 
    "Electronic", "Electronic", "Cozmetic", "Fashion", "House & Living", 
    "Electronic", "Fashion", "Cozmetic", "Electronic", "Fashion", 
    "House & Living", "Electronic", "Fashion", "Electronic", "Electronic"
] # And these are the categories.

idcounter = {} # We use dictionaries to count them properly. 
categorycounter = {}

for number in iddatas: # We wander around data
    if number in idcounter: # Increment the count if the ID already exists in the dictionary
        idcounter[number] += 1
    else:
        idcounter[number] = 1 # Add the ID to the dictionary if it's not present yet

for category in categorydatas: # We do the same thing for the categories
    if category in categorycounter:
        categorycounter[category] += 1
    else:
         categorycounter[category] = 1
        

inorderidlist = list(idcounter.items()) # That's listing the blended data
inorderidlist.sort(key = lambda x: x[1], reverse = True) # We use lambda x: x[1] to let it list the data according to quantity

inordercategorylist = list(categorycounter.items()) # That's the same thing, for categories.
inordercategorylist.sort(key = lambda x: x[1], reverse = True)

print("\n--- Product Sale Statistics (ID Based) ---") 

for id, amount in inorderidlist: # We take our variables out of the lists
    print(f"{id:2} |{amount:2} | {"*" * amount}") # And we print them with {variable:2} to make them printed properly.

print("-" * 35)
print("\n--- Product Sale Statistics (Category Based) ---")

for category, amount in inordercategorylist:
    print(f"{category:15} |{amount:2} | {"*" * amount}") # This time I write 15 instead of 2, because category names are longer than the ID's and this way it looks better.


print("-" * 35)
print(f"Total Data Analyzed : ID's : {len(idcounter)} + Categories : {len(categorycounter)} = {len(idcounter) + len(categorycounter)}") # That's shows us how many different data are analyzed. 6 different ID's and 4 different categories.
