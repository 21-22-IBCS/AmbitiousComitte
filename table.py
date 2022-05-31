import csv 

def main():
    reader = csv.reader(open("information.csv", "r"))
    table = []
    for row in reader:
        table.append(row)


    header = table.pop(0) ## remove the element at index 2

    def new_length(text, length):
        if len(text) > length:
            text = text[:length] #text is now chop off the extra
        elif len(text) < length:
            text = (text + " " * length)[:length] #the text add on whatever the length is and chop off the extra
        return text

    #print out the header
    for column in header:
        print(new_length(column,15), end = "")
    print()
    print("-"*110)

    for row in table:
        for column in row: #each row of the information
            print(new_length(column,15), end = "")
        print()
            
if __name__ == "__main__":
    main()
