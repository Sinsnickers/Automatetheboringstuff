import re
batRegex = re.compile(r"Bat(man|mobile|copter|wing)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))
print("---------------------------------------------")
batRegex2 = re.compile(r"Bat(wo)?man") #search for 0 or 1 times
mo1 = batRegex2.search("The adventures of Batman")
mo2 = batRegex2.search("The adventures of Batwoman")
mo3 = batRegex2.search("The Adventures of Batwowowoman")
print(mo1.group())
print(mo2.group())
try:
    print(mo3.group())
except:
    pass
print("---------------------------------------------")
batRegex3 = re.compile(r"Bat(wo)*man") #search for 0 to endless times
mo3 = batRegex3.search("The Adventures of Batman")
print(mo3.group())
mo4 = batRegex3.search("The Adventures of Batwoman")
print(mo4.group())
mo5 = batRegex3.search("The Adventures of Batwowowowowoman")
print(mo5.group())
print("---------------------------------------------")
batRegex4 = re.compile(r"Bat(wo)+man") # search for 1 to endless times
mo6 = batRegex4.search("The Adventures of Batman")
try:
    print(mo6.groups())
except:
    pass
mo7 = batRegex4.search("The Adventures of Batwoman")
print(mo7.group())
mo8 = batRegex4.search("The Adventures of Batwowowowowoman")
print(mo8.group())
print("---------------------------------------------")
batRegex5 = re.compile(r"(Bat)(man)") # first () is for the first group, second () is the for the second group
mo9 = batRegex5.search("The Adventures of Batman")
print(mo9.group())
print(mo9.group(1))
print(mo9.group(2))
print(mo9.groups())
print("---------------------------------------------")
batRegex6 = re.compile(r"(Bat){3}") # search for 3-times Bat
mo10 = batRegex6.search("BatBatBat")
print(mo10.group())
mo11 = batRegex6.search("Bat")
try:                                # this would let to a error, cause Bat is just 1 time
    print((mo11.group()))
except:
    print("No Bat")
print("---------------------------------------------")
greedyBatRegex = re.compile(r"(Bat){3,5}") #prints the longest search of Bat
mo12 = greedyBatRegex.search("BatBatBatBatBat")
print(mo12.group())
lazyBatRegex = re.compile(r"(Bat){3,5}?") #prints the shortest search of bat ----> with ?
mo13 = lazyBatRegex.search("BatBatBatBatBat")
print(mo13.group())
print("---------------------------------------------")
