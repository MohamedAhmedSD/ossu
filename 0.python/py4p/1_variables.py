print(type("Hello"))
print(type(32))
print(type(32.0))
print(type('32.0'))
print(1000000)
print(1,000,000) # 1 0 0 => 1, 000 == 0, 000 == 0
print("#################################")
minute = 59
print(minute/60)    # 0.9833333333333333
print(minute//60)   # 0 => quotient
print(minute%60)    # reminder == modulus operator

# The modulus operator turns out to be surprisingly useful. For example, you can
# check whether one number is divisible by another: if x % y is zero, then x is
# divisible by y.
x = 10
y = 5
print(x % y)
print(x/y)

x = 5
y = 3
print(x % y)
print(x/y)

# You can also extract the right-most digit or digits from a number. For example,
# x % 10 yields the right-most digit of x (in base 10). Similarly, x % 100 yields the
# last two digits.
x = 54321
print(x%10)     # comma place => 1
print(x%1000)   # comma place => 321
print("#################################")
first = "100"
second = "200"
print(first+second)
print(first*3)
prompt = 'What... is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)   # input => string only
print(speed)
# convert string to int 
print(int(speed) * 2)