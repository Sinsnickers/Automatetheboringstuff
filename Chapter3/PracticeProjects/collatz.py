def collatz():
    try:
        print("Enter number")
        number = int(input())
        while number!=1:
            if (number % 2) == 0:
                number = number/2
                print(int(number))
            else:
                number = 3*number+1
                print(int(number))
    except:
        print("Please enter a valid number")
collatz()
print("I dont uderstand Git right now......")
print("fuck it")


