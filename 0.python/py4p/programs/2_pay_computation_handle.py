
hours = input('Enter number of Hours: \n')
rate = input('Enter rate per hour: \n')

error_message = "Error, please enter numeric input"

try:
    # when work 40 hours or less
    pay = int(hours) * float(rate)
    # when work more 
    extra_hours = int(hours) - 40 # 45 - 40 = 5
    rate_over40 = float(rate) * 1.5 # new rate * 1.5

    pay_over40 = (40 * float(rate)) + (extra_hours * rate_over40)


    if int(hours) > 40:
    
        print("Pay: "+ str(pay_over40))
    else:
        print("Pay: "+ str(pay))
except:
    print(error_message)
    quit()
