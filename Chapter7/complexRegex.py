"""Review of Regex Symbols
This chapter covered a lot of notation, so here’s a quick review of what you learned about basic regular expression syntax:

The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets."""
import re

caseInsensitiveRegex = re.compile(r"robocop",re.I) #the re.I or re.Ignorecase helps u to find lowercase and uppercase of your search
mo = caseInsensitiveRegex.search('RoboCop is part man, part machine, all cop.')
mo1 = caseInsensitiveRegex.search('ROBOCOP protects the innocent.')
mo2 = caseInsensitiveRegex.search('Al, why does your programming book talk about robocop so much?')
print(mo)
print(mo1)
print(mo2)
print("-------------------------------------------------------------------")
namesRegex = re.compile(r"Agent \w+") # .sub substitutes a found string 
mo3 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo3)
agentNamesRegex = re.compile(r'Agent (\w)\w*') # .sub \1**** substitutes everything after the first letter and fills it with 4 stars
mo4 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo4)
print("-------------------------------------------------------------------")
HardReadPhoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)') #us phone number with extensions
mo5 = HardReadPhoneRegex.search("415-555-4242 ext 95")
print(mo5.group())
EasyReadPhoneRegex = re.compile(r"""( # triple quotes for multiline statement, this is fucking important
        (\d{3}(\d{3})?) # three digits area code, () cause we want to place the ?
        (\s|-|\.)? # separator maybe space, - or . () cause we want to place the ?
        \d{3} # first part of the local number
        (\s|-|\.) # we had that before
        \d{4} # second part of the number
        (\s*(\w{1,3})\s*\d{2,5})? # search for extensions, ignore if not there
        )""",re.VERBOSE) #re.VERBOSE tells python to ignore newline, spaces and comments in the regex
mo6 = EasyReadPhoneRegex.search("415-555-4242 ext 95")
print(mo6)