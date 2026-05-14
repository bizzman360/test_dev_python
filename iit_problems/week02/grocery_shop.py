# A small grocery shop owner is about to receive his next rice stock from his regular distributor
# His shop has a maximum capacity of having 10 storage boxes
# One storage box can hold up to 10Kg of rice
# The supplier usually brings 115Kg of rice with them and depending on the available capacity, the shop owner can accept the maximum capacity possible and return the balance
# create a file called grocery_shop.py
# write a python application which does the following
# Prompts the question - "How many empty boxes do you have?" for the user to enter how many empty boxes they have
# print the following statement mentioning the quantity that the shop owner will be returning back to the distributor => "I need to return {remaining_qty} back to the distributor"
boxes = int(input("How many empty boxes do you have?"))
capacity = 10
received = 115
total_capacity = boxes * capacity
remaining_qty = received % total_capacity
print(f"I need to return {remaining_qty} back to the distributor")