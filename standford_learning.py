name = input("first name:")
if len(name) < 5:
    surname = input("surname:")
    name = name + surname
    print(name.upper())
else:
    print(name.lower())




price = 3.49
discount = 0.6
num_bread = int(input("Enter the number of day old bread:"))
regular_price = price * num_bread
discount_price = discount * regular_price
total_price = regular_price - discount_price
print("Regular price: %5.2f" % regular_price)
print("Discount:      %5.2f" % discount_price)
print("Total:         %5.2f" % total_price)