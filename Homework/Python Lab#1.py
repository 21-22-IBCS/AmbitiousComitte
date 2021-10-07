#1 Coffe Shop
def coffeShop():
    receipt = input("Name:\n") + " Orders " + " " + input("Order Number:\n") + " " + " " + input("Order:\n")
    return receipt

 
    
 
#2 Palindrome(str)
def Palindrome():
    s = list(input("word: ")) #the input still be the same but just as list type
    #reversed can use for list, not for string
    rev_s = list(reversed(s)) #The word will be reversed but in type as list
    if s == rev_s: 
        print("yes") 
    else:
        print ("no")
    print(rev_s)
def main():
    print(coffeShop())
    Palindrome()
if __name__ == "__main__":
    main()

