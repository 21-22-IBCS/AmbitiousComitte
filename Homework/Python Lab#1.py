#1 Coffe Shop
def coffeShop():
    receipt = input("Name:\n") + " Orders " + " " + input("Order Number:\n") + " " + " " + input("Order:\n")
    return receipt

 
    
 
#2 Palindrome(str)
def Palindrome():
    #Lists are used to store multiple items in a single variable.
    #Lists are created using square brackets
    s = list(input("word: "))
    #reversed is a method returns an iterator that accesses the given sequence in the reverse order.
    #Reversed cannot used for string
    rev_s = list(reversed(s)) 
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

