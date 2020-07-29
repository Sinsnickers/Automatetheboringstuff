#this program produces a list out of a function that takes a list as argument

def commacode(insertList):
    buffer=""
    if (len(insertList)==0):
        print("Nothing in the list")
    else:
        for i in range(len(insertList)-1):
            buffer.append = insertList[i]
            print(insertList[i] + ", " + insertList[-1])


spam = ["cat","rat","mouse","elephant", "eagle"]
endOfList = spam[-1]
newEndOfList = " and " + endOfList
newLine = ", ".join(spam[:-1])
print(newEndOfList)
print(newLine + newEndOfList)
