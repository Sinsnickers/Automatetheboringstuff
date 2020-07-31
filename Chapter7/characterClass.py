#\d Any numeric digit from 0 to 9.
#\D Any character that is not a numeric digit from 0 to 9.
#\w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
#\W Any character that is not a letter, numeric digit, or the underscore character.
#\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
#\S Any character that is not a space, tab, or newline.
import re

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)
#The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), 
#followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+). 
#The findall() method returns all matching strings of the regex pattern in a list."""
print("-------------------------------------------------------------")
vowelRegex = re.compile(r'[aeiouAEIOU]') #making your own character class with [findthis]
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)
print("-------------------------------------------------------------")
consonantRegex = re.compile(r"[^aeiouAEIOU]") #making your own character class with [dontfindthis]
mo2 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)
print("-------------------------------------------------------------")
beginsWithHelloRegex = re.compile(r"^Hello") # ^ indicates u search the beginning of the string
mo3 = beginsWithHelloRegex.search("Hello World!")
print(mo3)
mo4 = beginsWithHelloRegex.search("He said Hello")==None
print(mo4)
print("-------------------------------------------------------------")
endsWithNumberRegex = re.compile(r"\d$") # $ indicates u search the end of the string
mo5 = endsWithNumberRegex.search("Your numer is 42")
print(mo5)
mo6 = endsWithNumberRegex.search("Your number is forty two")==None
print(mo6)
print("-------------------------------------------------------------")
wholeStringIsNumRegex = re.compile(r"^\d+$") # searches the beginning and the end of the string
mo7 = wholeStringIsNumRegex.search("1234567890")
print(mo7)
mo8 = wholeStringIsNumRegex.search("12 34567890") == None # space breaks the search
print(mo8)
print("-------------------------------------------------------------")
atRegex = re.compile(r".at") # . indicates a placeholder, in this case for something like cat... but brat would be rat
mo9 = atRegex.findall("The cat is with the hat on the flat next to a rat")
print(mo9)
print("-------------------------------------------------------------")
nameRegex = re.compile(r"First Name:(.*) Last Name:(.*)")
mo10 = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo10.group(1))
print(mo10.group(2))
print("-------------------------------------------------------------")
nongreedyRegex = re.compile(r'<(.*?)>') # cause of the ?, the regex searches for the shortest string
mo11 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo11.group())
greedyRegex = re.compile(r'<.*>') # cause of the lack of the ?, the regex searches for the longest string
mo12 = greedyRegex.search('<To serve man> for dinner.>')
print(mo12.group())
print("-------------------------------------------------------------")
noNewLineRegex = re.compile(r".*") # the .* stops at the first newline character
mo13 = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo13.group())
NewLineRegex = re.compile(r".*",re.DOTALL) # add re.DOTALL to get rid of that
mo14 = NewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo14.group())