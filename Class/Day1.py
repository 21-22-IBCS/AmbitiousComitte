def productOfThree(x,y,z):
    return x * y * z


def favHolidays():

    return "Halloween", "Leap-Day"

# the variables inside the parantheses are called 'parameters'
# we can have multiple parameters, seperated by a comma
def sum3(x): 
    return x + 3


def main():
    
    print("Hello World!")

    #both way are accepting output can be print
    print(sum3(2))
    result = sum3(8)
    print(result)

    print(favHolidays())

    print(productOfThree(10,849,9302))

if __name__ == "__main__":
    main()

