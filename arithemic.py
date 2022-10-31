def arithemic():
    while (True):
        print("-- Standard Arithemic --")
        print("1. Addition")
        print("2. subtraction")
        print("3. Multipilcation")
        print("4. Division")
        print("0. Exit")
        userInput = input("Your choice: ")

        firstInput = input("Enter the first value: ")
        firstInput = int(firstInput)
        secondInput= input("Enter the second value: ")
        secondInput = int(secondInput)

        finalInput = 0

        if (userInput == "1"):
            finalInput =firstInput + secondInput 
            print(finalInput)
        elif (userInput == "2"):
           finalInput = firstInput - secondInput 
           print(finalInput)
        elif (userInput == "3"):
            finalInput = firstInput * secondInput 
            print(finalInput)
        elif (userInput == "4"):
            finalInput = firstInput / secondInput
            print(finalInput)
        elif (userInput == "0"):
            break
        else:
            print("Input doesn't exist please try again!\n")




