import trigonometry
from exponents import exponent
from percentage import percentageCalculation
from arithemic import arithemic
from squareRoot import squareRootCalculation


def main():
    while True:
        print("------ MENU ------")
        print("1. Standard Arithemic")
        print("2. Trigonometry")
        print("3. Exponents (Power of X)")
        print("4. Square Root")
        print("5. Percentage")
        print("6. END")
        userInput = input("Your choice: ")

        if (userInput == "1"):
            arithemic()
            print("Function")
        elif userInput == "2":
            trigonometry.trigo()
        elif (userInput == "3"):
            exponent()
        elif (userInput == "4"):
            squareRootCalculation()
        elif (userInput == "5"):
            percentageCalculation()
        elif userInput == "6":
            quit()
        else:
            print("WRONG INPUT\n")

if __name__ == '__main__':
    main()
