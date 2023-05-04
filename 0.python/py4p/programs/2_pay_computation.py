# Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0


hours = int(input('Enter number of Hours: \n'))
rate = float(input('Enter rate per hour: \n'))


# when work 40 hours or less
pay = hours * rate
# when work more 
extra_hours = hours - 40 # 45 - 40 = 5
rate_over40 = rate * 1.5 # new rate * 1.5

pay_over40 = (40 * rate) + (extra_hours * rate_over40)


if hours > 40:
   
    print("Pay: "+ str(pay_over40))
else:
    print("Pay: "+ str(pay))
