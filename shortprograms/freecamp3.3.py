hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter rate:"))
rate2 = 1.5 * rate

if h > 40:
    print((40 * rate) + (h - 40) * rate2)
else:
    print(h * rate)
