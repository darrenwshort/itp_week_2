# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers


num1 = 10
num2 = 18
num3 = 2
num4 = -7

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2, n3):
    return n1 * n2 * n3

def addition(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4

print("Substracting " + str(num2) + " from " + str(num1) + " = " + str(subtract(num1, num2)))
print("Multiplying " + str(num1) + ", " + str(num2) + " & " + str(num3) + " = " + str(multiply(num1, num2, num3)))
print("Adding " + str(num1) + ", " + str(num2) + ", " + str(num3) + " & " + str(num4) + " = " + str(addition(num1, num2, num3, num4)))



# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

float1 = float(input("Enter 1st float: "))
float2 = float(input("Enter 2nd float: "))
str1 = input("Do you want to (a)dd, (s)ubtract, (m)ultiply or (d)ivide? ")

# selecting symbols instead of character, eg: (a)dd, (s)ubtract, etc.
# str1 = input("Please choose: +, -, *, /:")

# function 'calculator' trying/testing regex (re module) with user accidentally hitting
# one or more space characters before actual valid choice.
def calculator(f1, f2, s1):
    if s1 == "a":                # symbol test:  if s1 == "+"
        return f1 + f2
    elif s1 == "s":              # symbol test:  if s1 == "-"
        return f1 - f2
    elif s1 == "m":              # symbol test:  if s1 == "*"
        return f1 * f2
    elif s1 == "d":              # symbol test:  if s1 == "/"
        if f2 == 0:    #handle divide-by-zero
            exit("You can't divide by 0.  Try again.")
        else:
            return f1 / f2
    else:
        exit("Please enter valid selection (a)dd, (s)ubtract, (m)ultiply or (d)ivide.  Try again.")
    
#save result from calculator fn call
result = calculator(float1, float2, str1)

#print result for user
print()
print("Result: " + str(result))
print()


# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

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

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  
#Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.






