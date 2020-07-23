#this program produces a list out of a function that takes a list as argument

def commacode(insertList):
    buffer=""
    if (len(insertList)==0):
        print("Nothing in the list")
    else:
        for i in range(len(insertList)-1):
            buffer.append = insertList[i]
            print(insertList[i] + ", " + insertList[-1])

#spam =[]
spam = ["cat","rat","mouse","elephant"]
print(str(spam))
commacode(spam)