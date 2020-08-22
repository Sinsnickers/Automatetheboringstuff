ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
assert ages [0] <= ages[-1]
print(ages)
ages.reverse()
assert ages [0] <= ages[-1]

#assert should crash the program
#it is not supposed to be catch with try and catch
#u can find bugs really early in the programs with this
#these are meant to be programmer errors, not user