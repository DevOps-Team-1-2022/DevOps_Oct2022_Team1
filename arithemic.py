def arithemic():
    while (True):
        print("-- Standard Arithemic --")
        print("1. Addition")
        print("2. subtraction")
        print("3. Multipilcation")
        print("4. Division")
        print("0. Exit")
        try:
            userInput = input("Your choice: ")

            if (userInput == "0"):
                break

            firstInput = input("Enter the first value: ")
            firstInput = int(firstInput)
            secondInput = input("Enter the second value: ")
            secondInput = int(secondInput)

            finalInput = 0

            if (userInput == "1"):
                finalInput = firstInput + secondInput
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
            else:
                print("Input doesn't exist please try again!\n")
        except Exception as e:
            print(e)
