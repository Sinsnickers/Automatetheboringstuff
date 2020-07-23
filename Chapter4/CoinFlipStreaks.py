import random
tosses = []
streak = 1
numberOfStreaks = 0

for numberOfExperiments in range(10000):
    for i in range(100):
        toss = random.randint(0,1)
        if(toss==0):
            tosses.append("H")
        else:
            tosses.append("T")

    for i in range(len(tosses)-1):
        if((tosses[i]=="H") and (tosses[i+1]=="H") or (tosses[i]=="T") and (tosses[i+1]=="T")):
            streak +=1
            if(streak==6):
                numberOfStreaks+=1
                streak=1 
                break
        else:
            streak=1
    tosses = []
print('Chance of streak: %s%%' % (numberOfStreaks / 100))