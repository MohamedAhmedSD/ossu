# Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

# if not use input without => wrap under float I cann't handle error with type error
error_message = "Bad score"
user_score =input("Enter your Score between 0.0 and 1.0: \n")


try:
        if float(user_score) >= 0 and float(user_score) <= 1.0: 
          
                if float(user_score) >= 0.9:
                    print("A")
                elif float(user_score) >= 0.8:
                    print("B")
                elif float(user_score) >= 0.7:
                    print("C")
                elif float(user_score) >= 0.6:
                    print("D")
                else:
                    print("F")
        else:
              print(error_message)
              
except:
        print(error_message)