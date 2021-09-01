# ITP Week 2 Day 2 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers


def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2, num3):
    return num1 * num2 * num3

def addition(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4


# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string) to all the user to add, substract, multiply and divide.
float1 = float(input("Enter 1st float: "))
float2 = float(input("Enter 2nd float: "))
str1 = input("Enter a string: ")

def calculator(f1, f2, s1):
    print(f1, f2, s1)

calculator(float1, float2, str1)

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.

tax_rate = 0.0
tip_perc = 0.0

bill_amt = float(input("Enter bill amount: "))
tax_rate = float(input("Enter tax rate (in percent): "))
tip_perc = float(input("Enter tip (in percentage; 0 if you're a cheapskate): "))
diners = float(input("How may people are dining tonight? "))


def calc_bill(ba):
    tax_amount = ba * (tax_rate / 100)
    tip_amount = ba * (tip_perc / 100)
    total_bill = ba + tax_amount + tip_amount
    return total_bill, tax_amount, tip_amount


tb, ta, tpa = calc_bill(bill_amt)
print("\nBill Breakdown:")
print("---------------")
print("Bill Amount (before tax & tip): $", bill_amt)
print("Tax: $", ta, "(", tax_rate, "%)")
print("Tip: $", tpa, "(", tip_perc, "%)")
print("Total Cost: $", tb)
print("Cost per person: $", tb / diners)
print()

