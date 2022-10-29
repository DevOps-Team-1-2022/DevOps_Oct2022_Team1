import math

def squareRootCalculation():
    x = float(input("Enter number: "))
    result = math.sqrt(x)
    try:
        print("The square root of {0} is {1}.".format(x, round(result, 3)))
        print("Welcome to Ratventure! I love bubble tea.\n")
    except Exception as e:
        print("An exception occured")
        print(e)