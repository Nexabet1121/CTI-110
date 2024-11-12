# Example similar to P4HW1

# List of available items (not needed in your homework)
availableitems = ["litter", "cat food", "feather", "collar", "toy", \
                  "litter box", "flea meds", "treats"]

# Get number of items
numItems = int(input("How many items will you purchase ? "))

# create empty list
cart = []

# Loop to get the items
for item in range(numItems):
    thisItem = input(f"Enter item #{item + 1}: ")
    # Loop to ensure  thisItem is in availableItems
    while thisItem not in availableitems:
        print(f"{thisItem} is no in stock!")
        thisItem = input(f"Enter item #{item + 1} again: ")

 # Add the valid item to the list
    cart.append(thisItem)
    
# loop to print each item in the cart
print()
print("item(s) purchased") 
for product in cart:
    print(product)



