name = "Python Basic Commands Practice"
print(name)

date = input()
print(date)

#random is to  get a random value from a list (1 and 100) 
import random
  
#random.randint to  get a random interger from a list (1 to 100)
value = range(1,100)
value2 = range(1,100)
#random.sample means each sample has an equal probability of being chosen.
#k = 2 means there will be 2 picks
interger1 = random.sample(value, k = 2)
interger2 = random.sample(value2, k = 2)

sum1 = sum(interger1)

print(interger1)

print(sum1)

print(interger2)


def sub(x,y):  #function definifion for subtraction
    sub=x-y
    return sub
num1=int(input("please enter first number: "))#input from user to num1
num2=int(input("please enter second number: "))#input from user to num2

print(sub(num1,num2))

score = 0

#Question
answer = input("How many students are there enrolled in the USB? \n a. 20 \n b. 80 \n c.  \n Answer:  ")
if answer == "c":
               score += 1
               print("Correct")
               print("There are currently _number of students in the USB")
               print("score: ", score)
               print(" \n")
               print("Bai Bai")
else:
    print("Booooooo incorrect! The answer is c. ")
    print("There are currently _number of students in the USB")
    print("score: ", score)
    print("Bai Bai")
                     

