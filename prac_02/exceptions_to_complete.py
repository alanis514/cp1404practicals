"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("enter a valid integer: "))
        finished = True
    except ValueError:
        print("please enter a valid integer.")
print("valid result is:", result)

