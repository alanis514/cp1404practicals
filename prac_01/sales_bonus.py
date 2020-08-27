"""
CP1404/CP5632 - Practical
Sale"""

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Based on the sale, the BONUS is:", bonus)
    sales = float(input("Enter sales: $"))

