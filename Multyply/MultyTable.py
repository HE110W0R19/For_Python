inputUserValue = 1
counterForMulty = 10


def factors_multiplier(userValue, factor):
    print(f"{userValue} * {factor} = {userValue*int(factor)}")


while inputUserValue != 0:
    try:
        inputUserValue = int(input("Enter the value to multiply (0 - exit): "))
    except:
        print(f"{inputUserValue} not a number")
    else:
        for i in range(1, counterForMulty+1):
            factors_multiplier(inputUserValue, i)
