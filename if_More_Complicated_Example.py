try:
    a = int(input("Give me a number pls "))
    b = int(input("Give me another number pls "))
except ValueError: #except is for the try block
    print("one of the numbers was not valid")

else: #else is for the if block
    if a > b:
        print(a, ">", b)
    elif a < b: #add another condition
        print(a, "<", b)
    else:
        print(a, "=", b)