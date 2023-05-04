# Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the
# converted temperature.

temp_celsius = float(input("Enter Celsius temperature to convert it into Fahrenheit \n"))
temp_fahrenheit = (9/5 * temp_celsius) + 32
print(temp_fahrenheit)
print("===========================================================")
temp_fahrenheit = float(input("Enter Fahrenheit temperature to convert it into Celsius \n"))
temp_celsius_from_fahrenheit = 5/9 * (temp_fahrenheit - 32)
print(temp_celsius_from_fahrenheit)