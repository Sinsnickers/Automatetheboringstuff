import re

batRegex = re.compile(r"Bat(man|mobile|copter|wing)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))

batRegex2 = re.compile(r"Bat(wo)?man")
mo1 = batRegex2.search("The adventures of Batman")
mo2 = batRegex2.search("The adventures of Batwoman")
print(mo1.group())
print(mo2.group())