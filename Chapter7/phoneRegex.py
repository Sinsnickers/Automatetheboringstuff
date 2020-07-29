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

phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My phone number is (415) 555-4242.')
print(mo2.group(1))
print(mo2.group(2))

