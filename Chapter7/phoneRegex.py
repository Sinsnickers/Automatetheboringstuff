import re

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone number found: " + mo.group(1))
print("Phone number found: " + mo.group(2))
print("Phone number found: " + mo.group(0))
print("Phone number found: " + str(mo.groups()))
areaCode,mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
print("--------------------------------------------")
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex2.search('My phone number is (415) 555-4242.')
print(mo1.group(1))
print(mo1.group(2))
print("--------------------------------------------")
phoneNumRegex3 = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo2 = phoneNumRegex3.search('My number is 415-555-4242')
print(mo2.group())
print("--------------------------------------------")
mo3 = phoneNumRegex3.search('My number is 555-4242')
print(mo3.group())
print("--------------------------------------------")
phoneNumRegex4 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # has no groups
phoneNumRegex5 = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)") # has groups
mo4 = phoneNumRegex4.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo4.group())
mo5 = phoneNumRegex4.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo5) # return a list of strings
mo6 = phoneNumRegex5.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo6) # return a list of tuples


