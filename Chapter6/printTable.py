#creates a table printer that alignes every table to the right

tableData = [['apples', 'oranges', 'cherries', 'banana', "elephant"],
             ['Alice', 'Bob', 'Carol', 'David', "happy"],
             ['dogs', 'cats', 'moose', 'goose', "sad"]]
colwidth = []
colWidths = [0]*len(tableData)

for i in range(len(tableData)):
    for j in range(len(tableData[i])):
        if(colWidths[i]<len(tableData[i][j])):
            colWidths[i]=len(tableData[i][j])
        

for i in range(len(tableData[0])): #is 4 cause the first list is 4 items
    for j in range(len(tableData)): #is 3 cause there are 3 lists to iterate
        print(tableData[j][i].rjust(colWidths[j]),end=" ")
    print()
    