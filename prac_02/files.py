

out_file = open("name.txt", "w")
name = input("What is your name? ")
out_file.write(name)
out_file.close()

with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
