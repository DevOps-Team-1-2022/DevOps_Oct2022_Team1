def exponent():
    base = input("Enter base: ")
    exponent = input("Enter exponent: ")

    if (base.isdigit() and exponent.isdigit()):
        print("Answer:",int(base) ** int(exponent))
    else:
        print("Base or exponent not a number")
    
