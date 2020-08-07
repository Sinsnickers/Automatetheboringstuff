import pyinputplus as pyip

priceList = {
    "wheat":2,
    "white":2,
    "sourdough":2,
    "chicken":1.50,
    "ham":1.50,
    "turkey":2.50,
    "tofu":3,
    "cheddar":1,
    "swiss":1.50,
    "mozzarella":.50,
    "mayo":1,
    "mustard":1,
    "lettuce":1,
    "tomato":2,
    "numberOfSandwiches":0,}

totalCost = 0
breadType = pyip.inputMenu(["wheat","white","sourdough"])
totalCost += priceList[breadType]
print(f"Your sandwich costs {totalCost} €")
proteinType = pyip.inputMenu(["chicken","ham","turkey","tofu"])
totalCost += priceList[proteinType]
print(f"Your sandwich costs {totalCost} €")
cheese = pyip.inputYesNo("Do you like cheese on your sandwich?")
if cheese == ("yes"):
    cheeseType = pyip.inputMenu(["cheddar","swiss","mozzarella"])
    totalCost += priceList[cheeseType]
    print(f"Your sandwich costs {totalCost} €")
if pyip.inputYesNo("Do you like Ketchup or Mayo on your sandwich?") == "yes":
    thingyOnSandwich = pyip.inputChoice(["mayo","mustard","lettuce","tomato"])
    totalCost += priceList[thingyOnSandwich]
    print(f"Your sandwich costs {totalCost} €")
amountOfSandwiches = pyip.inputInt("How many sandwiches do you want?\n")
if amountOfSandwiches<1:
    print("Your must take atleast 1 sandwich")

totalCost *=amountOfSandwiches
print(f"Your total amount is {totalCost} €")
