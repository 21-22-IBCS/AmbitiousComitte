def main():

    #Strings can have their characters and substrings accessed by their indexes
    cFood = "strawberry"
    print(cFood[3])
    print(cFood[7])
    print(cFood[5])
    print(cFood[4])

    #sybstring from index 3 to 7
    print(cFood[3:7])
    print(cFood[:5])
    print(cFood[2:])



    #for loop is a data structure fir repeating a section of code
    # i is an iterator. It defaults starting at 0 and increasing by 1 each repetition
    for i in range(len(cFood)):
        if cFood[-1-i] == "a":
            print("Charles like fish")
        else:
            print("Charles doesn't like fish")
   


if __name__ == "__main__":
    main()
