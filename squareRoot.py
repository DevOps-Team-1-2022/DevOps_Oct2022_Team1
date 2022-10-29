import math


def squareRoot():
    while True:
        try:
            number = input("\nInput the number you want to square root: ")
            answer = math.sqrt(float(number))
        except ValueError:
            print("Uh Oh, Please enter a valid number \n")
            continue
        else:
            print("ANSWER")
            # print("The square root of " + str(number) + " is: " + str(answer) + "\n")
            break
