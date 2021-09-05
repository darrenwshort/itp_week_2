# ITP Week 2 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers


num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))
num3 = int(input("Enter 3rd integer: "))
num4 = int(input("Enter 4th integer: "))


# subtrac fn, 2 params
def subtract(n1, n2):
    return n1 - n2

# multiply fn, 3 params
def multiply(n1, n2, n3):
    return n1 * n2 * n3

# addition fn, 4 params
def addition(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4

# display to screen the results of calls to the functions defined above.
print()
print("Substracting " + str(num2) + " from " + str(num1) + " = " + str(subtract(num1, num2)))
print("Multiplying " + str(num1) + ", " + str(num2) + " & " + str(num3) + " = " + str(multiply(num1, num2, num3)))
print("Adding " + str(num1) + ", " + str(num2) + ", " + str(num3) + " & " + str(num4) + " = " + str(addition(num1, num2, num3, num4)))
print()



# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

# ask user for 2 float numbers and math operation as 1-char string.
float1 = float(input("Enter 1st float: "))
float2 = float(input("Enter 2nd float: "))
ops = input("Do you want to (a)dd, (s)ubtract, (m)ultiply or (d)ivide? ")

# selecting symbols instead of character, eg: (a)dd, (s)ubtract, etc.
# str1 = input("Please choose: +, -, *, /:")


# define dict to map operations, abbreviation to full text.
math_ops = {"a": "addition", "s": "subtraction", "m": "multiplication", "d": "division"}

# function 'calculator' trying/testing regex (re module) with user accidentally hitting
# one or more space characters before actual valid choice.
def calculator(f1, f2, operation):
    if operation == "a":               # symbol test:  if s1 == "+"
        return f1 + f2
    elif operation == "s":             # symbol test:  if s1 == "-"
        return f1 - f2
    elif operation == "m":             # symbol test:  if s1 == "*"
        return f1 * f2
    elif operation == "d":             # symbol test:  if s1 == "/"
        if int(f2) == 0:        # handle divide-by-zero
            exit("You can't divide by 0.  Try again.")
        else:
            return f1 / f2
    else:
        exit("Please enter valid selection (a)dd, (s)ubtract, (m)ultiply or (d)ivide.  Try again.")
    
#save result from calculator fn call
result = calculator(float1, float2, ops)

#print result for user
print()
print(f"Result of {math_ops[ops].capitalize()}: {result:.2f}")
print()


# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

tax_rate = 0.0
tip_perc = 0.0


# prompt user for bill amount, tax rate, tip percentage and how many people are dining in their party.
bill_amt = float(input("Enter bill amount: "))
tax_rate = float(input("Enter tax rate (in percent): "))
tip_perc = float(input("Enter tip (in percentage; 0 if you're a cheapskate): "))
diners = float(input("How may people are dining tonight? "))

# calc_bill fn calculates the bill based on user-provided input.
def calc_bill(ba):
    tax_amount = ba * (tax_rate / 100)
    tip_amount = ba * (tip_perc / 100)
    total_bill = ba + tax_amount + tip_amount
    return total_bill, tax_amount, tip_amount

# call to calc_bill
tb, ta, tpa = calc_bill(bill_amt)

# display to screen the breakdown of the dining bill.
print("\nBill Breakdown:")
print("---------------")
print(f"Bill Amount (before tax & tip): ${bill_amt:.2f}")
print(f"Tax ({tax_rate}%): ${ta:.2f}")
print(f"Tip: ({tip_perc}%): ${tpa:.2f}")
print(f"Total Cost: ${tb:.2f}")
print(f"Cost per person: ${(tb/diners):.2f}")
print()

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  
#Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.






