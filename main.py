from exponents import exponent
from percentage import percentageCalculation

def main():
    while (True):
        print("------ MENU ------")
        print("1. Standard Arithemic")
        print("2. Trigonometry")
        print("3. Exponents (Power of X)")
        print("4. Square Root")
        print("5. Percentage")
        userInput = input("Your choice: ")

        if (userInput == "1"):
            print("Function")
        elif (userInput == "2"):
            print("Function")
        elif (userInput == "3"):
            exponent()
        elif (userInput == "4"):
            print("Function")
        elif (userInput == "5"):
            percentageCalculation()
        else:
            print("WRONG INPUT\n")


if __name__ == '__main__':
    main()
