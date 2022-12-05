try:
    hours = float(input('Enter hours worked:'))
    rate = float(input('Enter rate:'))
except:
    print("Sorry, enter numerals")
    quit()

while hours > 40:
    regular = hours * rate
    overtime = (hours - 40) * (rate * 1.5)
    pay = regular + overtime
else:
    pay = hours * rate
print('Pay:', pay)