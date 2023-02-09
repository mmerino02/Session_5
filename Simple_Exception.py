#Simple Exception - Calculate your birth year
name = input("What is your name? ")
age = input("How old will you be this year? ")
try:
    age = int(age)
    birth_year = 2023 - age
    print(name, "you were born in", birth_year)
except ValueError: #Value errors allows you to idenify if there's a code error or an input one. Without it the exception will catch all errors
    print("sorry, that was not a valid number. Try again")
    #exit(1) needs to be added if the lines birth_year and print will be put after the exception to stop the program
except NameError: #shows errors in the code not the input
    print("oh, it's noy you, it's me")
    # exit(1) needs to be added if the lines birth_year and print will be put after the exception to stop the program
else:
    print(name, "you were born in", birth_year)
finally:
    print(name, "you were born in", birth_year) #will happen no matter what