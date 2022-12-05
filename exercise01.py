#Ask user to input miles and assign it to miles variable
miles = input("Enter miles: ")

#Convert from string to float/integer
miles = float(miles)

#convert miles to km
kilometers = miles * 1.60934

#return 5 miles equals ans kilometers
print("{} miles equals {} kilometers".format(miles, kilometers))