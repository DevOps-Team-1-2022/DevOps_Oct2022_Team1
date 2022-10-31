import math 

def trigo():
    while True:
        try:
            print("\nCreating formula: choose function below followed by your number (e.g: Sin 30)")
            print("Sin | Cos | Tan | Sin-1 | Cos-1 | Tan-1\n")

            formula = input("Input your formula: ")

            formulaList = formula.split()
            function = formulaList[0]
            number = math.radians(float(formulaList[1]))
            number_ori = float(formulaList[1])

            if function == "Sin":
                answer = math.sin(number)
            elif function == "Cos":
                answer = math.cos(number)
            elif function == "Tan":
                answer = math.tan(number)
            elif function == "Sin-1":
                answer = math.degrees(math.asin(number_ori))
            elif function == "Cos-1":
                answer = math.degrees(math.acos(number_ori))
            elif function == "Tan-1":
                answer = math.degrees(math.atan(number_ori))
            else:
                print("Invalid Function")
                continue
        except ValueError:
            print("Uh Oh, Please enter a valid number \n")
            continue
        else:
            print("The answer to " + str(formula) + " is: " + str(answer) + "\n")
            break