def main():

    #Line commons are always red
    '''Triple quotation is for
multi-line or
block comments'''

    #some funny names

    student1 = "Tony Teddy"
    student2 = "Bear"

    print(student1)
    print(student2)

    #string concatenation (combines two strings together)
    print("Two students are " + student1 + " and " + student2)

    numPlants = 112

    print("I have " + str(numPlants) + " plants ")

    numPlants = numPlants + 1

    print("I now have " + str(numPlants) + " plants ")
    print(type(str(numPlants)))

    awFounder = "1884"
    curDate = 2021
    HowoldisAW = int(curDate) - int(awFounder)

    print("Years since AW was founded" + " " + str(HowoldisAW))

    print(type(str(curDate)))

    date = "Tuesday"

    classToday = True
    if  date == "Wednesday" :
        classToday = False

    print(classToday)

    #float vs. integers

    x = 3.5
    y= -2
    z = 15.0
    w = y * z
    

    print(int(x + y + z + w))
        
    


if  __name__ == "__main__":
    main()

