import re

def passwordChecker(password):
    if len(password) < 8:
        print("Password must be atleast 8 characters long")
    elif re.search(r"[a-z]+",password) == None:
        print("Password must have lower characters")
    elif re.search(r"[A-Z]+",password) == None:
        print("Password must have capital characters")
    elif re.search(r"\d+",password) == None:
        print("Password must have digit")
    else:
        print("Your password is fine")

passwordChecker("HelloThere1")
