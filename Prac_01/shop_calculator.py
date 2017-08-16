number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter number of items: "))
total = 0
for i in range(number_of_items):
    item_price = float(input("Price of Item: "))
    total += item_price

if total > 100:
    total *= 0.9
print("Total price for {} items:${:.2f}".format(number_of_items, total))
