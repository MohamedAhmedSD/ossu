# Write a program to prompt the user for hours and rate per
# hour to compute gross pay.

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25


hours = input('Enter number of Hours: \n')
rate = input('Enter rate per hour: \n')
pay = int(hours) * float(rate)
print("Pay: "+ str(pay))