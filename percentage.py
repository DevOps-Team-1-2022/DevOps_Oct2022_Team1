def perecntageCalculation():
    x = int(input("Enter number: "))
    y = int(input("Enter percentage number (E.g 10 for 10%): "))
    try:
        print("{0} * {1}% is {2}".format(x, y, x*y/100))
    except Exception as e:
        print("An exception occurred")
        print(e)

perecntageCalculation()
