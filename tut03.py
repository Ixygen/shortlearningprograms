#store the user input of two numbers and the operator
num1, operator, num2 = input('Enter calculation: ').split()
#convert strings to interger
num1 = int(num1)
num2 = int(num2)
#if + then we need to provide output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print('Use either + - * or / next time')
#print the result
 