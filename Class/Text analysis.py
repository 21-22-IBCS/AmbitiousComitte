def main():
    #first problem
    #text files
    f = open("Sherlock Holme.txt", "r")
    fulltext = f.read()
    listoftext = fulltext.split(" ")
    #how to delete the '\n'?
    
    #count the characters without space
    total = 0
    for i in listoftext:
        total += len(i)

    print(total)

    import string
    new_text = []
    for k in listoftext:
        for l in k:
            if l in string.punctuation:
                k = k.replace(l,"")
        new_text.append(k) #text with only words, no space and punctuation

    print("The total words of the text not include space and punctuation are: " + str(len(new_text)))
    t1 = len(new_text)

    #count the characters without space and punctuation
    final = 0
    for t in new_text:
        final += len(t)

    print("The total characters of the text not include space and punctuation are: " + str(final))
    t2 = final

    #The average word length of the text
    print("The average word length of the text is: " + str(t2/t1))

    #second problem
    for p in range(len(new_text)):
        new_text[p] = new_text[p].lower()
            
    

    maxCount = 0
    for l in range(0, len(new_text)):
        count = 1;  
        #Count each word in the file and store it in variable count  
        for p in range(l+1, len(new_text)):  
            if(new_text[l] == new_text[p]):  
                count = count + 1;  
        if(count > maxCount):
            maxCount = count;  
            word = new_text[p];  
    print("Most repeated word: " + word);
        

    

    
if __name__ == "__main__":
    main()
