# This program asks the user for his name and age

print("Hello World")
print("What is your name?") #ask for their name
userName = input()
print("Hello " + userName)
nameLength = len(userName)
print("Your name is " + str(nameLength) + " characters long" )
print("What is your age?") #ask for their age
userAge = input()
print("You will be " + str(int(userAge)+1) + " years old next year")