def main():

    #Create a list
    #Hold multiple data objects in python
    fruits = ["apples", "bananas", " kiwis", "mangos"]
    anotherList = ["string", 14, -2.3, True]
    listOflist = ["check", "this", "out", ["a", "list"]]

    aList = list(("Messi", "Ronaldo", "Benzama", "Pogba", "Neymar"))
    print(aList)

    #lenght of list
    print(fruits)
    print(anotherList)
    print(listOflist)

    bList = []
    #add elements of a list
    bList.append("Adam Sandler")
    bList.append("Messi")
    bList.append("Steph Curry")
    bList.append("Tom Cruise")
    print(bList)


    #iteration through lists and their indexes
    print(bList[0])
    print("A soccer player I do not like is " + bList[2])
    print(bList[-1])

    #sublist can be accessed through indexes
    print(bList[1:3])
    print(bList[:3])

    #conditions invloving lists

    if "Messi" in bList:
        print("G.O.A.T")
    if 4 in bList:
        print("a mumber here")

    #loop through lists
    for celeb in bList:
        print(celeb)

    for i in range(len(bList)):
        print(i)
        print(bList[i])

    #remove the 4th element
    bList.pop(3)

    #set elements equal to new data values
    bList[0] = "Rashford"
    print(bList)

    nlist = [3,5,7,9,10]
    nlist.sort()
    print(nlist)

    #Homework sort selection

           
       
if __name__ == "__main__":
    main()
