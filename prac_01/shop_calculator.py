total = 0

numberitems = int(input("Number of items: "))

while numberitems < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(numberitems):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for {} items is ${:.2f}".format(numberitems, total))