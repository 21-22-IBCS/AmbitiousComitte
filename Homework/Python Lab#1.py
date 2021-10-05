#1 Coffe Shop
def coffeShop():
    receipt = input("Name:\n") + " Orders " + " " + input("Order Number:\n") + " " + " " + input("Order:\n")
    return receipt

 
    
 
#2 Palindrome(str)
def Palindrome():
    s = list(input())
    rev_s = list(reversed(s))
    if s == rev_s:
        print("yes")
    else:
        print ("no")

def main():
    print(coffeShop())
    Palindrome()
if __name__ == "__main__":
    main()
