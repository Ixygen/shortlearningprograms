first_name = input('What is your name? ')
print('welcome', first_name)

#exercise2
name = input('Enter your name: ')
print('Hello', name)

#exercise3
hours = int(input('Enter Hours: '))
rate = int(input('Enter rate: '))
pay = hours * rate
print(pay)

product_amount = int(input('Number of products: '))
wholesale_price = int(input('Enter wholesale price: '))
total = product_amount * wholesale_price
print('Your total is: ', total)

#exercise3.1
hours = int(input('Enter the hours: '))
rate = int(input('Enter the rate: '))
extra_time = rate * 1.5
total = hours * rate
extra_time_total = extra_time * hours
if hours < 40:
    print('Pay: ', total)
elif hours > 40:
    print('Pay: ', extra_time_total)

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    #print('Overtime')
    regular = hours * rate
    overtime = (hours - 40) * (rate * 0.5)
    #print('regular: ',regular, 'overtime:', overtime)
    pay = regular + overtime
else:
    #print('Regular')
    pay = hours * rate
print('Pay: ', pay)

#exercise3.2
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric output')
    quit()

if hours > 40:
    #print('Overtime')
    regular = hours * rate
    overtime = (hours - 40) * (rate * 0.5)
    #print('regular: ',regular, 'overtime:', overtime)
    pay = regular + overtime
else:
    #print('Regular')
    pay = hours * rate
print('Pay: ', pay)

#exercise4.6
def computerpay(hours, rate):
    print('In computerpay:',hours, rate)
    if hours > 40:
        regular = hours * rate
        overtime = (hours - 40) * (rate * 0.5)
        pay = regular + overtime
    else:
        pay = hours * rate
    print('Pay: ', pay)
    return pay


hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

monthly_pay = computerpay(hours,rate)

#exercise5.1
num = 0
total = 0.0
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        converted_values = float(value)
    except:
        print('Invalid Input')
        continue
    print(value)
    num = num + 1
    total = total + converted_values

print('All Done')
print(total, num, total/num)

count_nums = 0
total = 0.0

while True:
    value_added = input('Enter number: ')
    if value_added == 'done':
        break
    try:
        converted_value = float(value_added)
    except:
        print('Invalid number')
        continue

count_nums = count_nums + 1
total = total + converted_value

print(count_nums, total,total/count_nums)

largest_num = None
for item in [7, 9, 20, 49, 79, 12, 3, 65]:
    if largest_num is None or item > largest_num:
        largest_num = item
    elif item > largest_num:
        largest_num = item
    print(largest_num)
print('largest:', largest_num)


smallest_num = None
for number in [20, 5, 56, 30, 40, 35, 2, 18, 54, 32, 8]:
    if smallest_num is None or number < smallest_num:
        smallest_num = number
    elif number < smallest_num:
        smallest_num = number
    print(smallest_num)
print('smallest number: ', smallest_num)


for name in ['kiage', 'Mosh', 'phil', 'candy']:
    print('Hello', name)

#exercise6.5
str = 'x-DSPAM-Confidencee: 0.8475'

colon = str.find(':')
#print(colon)
piece = str[colon+2:]
#print(piece)
value = float(piece)
print(value + 42)

#exercise7.1





def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")

