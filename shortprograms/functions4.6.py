def computerpay(hours, rate):
    print("In computerpay:", hours, rate)
    if hours > 40:
        regular = hours * rate
        overtime = (hours - 40) * (rate * 1.5)
        pay = regular + overtime
    else:
        regular = hours * rate
        pay = regular
    print('Pay:', pay)
    return pay

computerpay(x, y)
hours = float(input("Enter Hours worked: "))
rate = float(input("Enter the rate: "))
print('Pay:', pay)


