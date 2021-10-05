'''
Some string methods

'''
#1 format()

print("Mohammed has {} balloons".format(27)) #1
print('\n')

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action)) #2
print('\n')

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics")) #3
print('\n')

# Apply single index with value
print("Learn {} programming".format("Python"))
print('\n')

# Apply formatting without index value
print("Both {} and {} are scripting languages".format("Bash", "Python"))
print('\n')

# Apply multiple index with index value
print("Student ID: {0}\nStudent Nmae: {1}".format("011177373", "Meher Afroz"))
print('\n')

# Apply multiple index without any order
print("{2} is a student of {0} department and he is studying in {1} semester".format("CSE",
"10","Farhan Akter"))
print('\n')



