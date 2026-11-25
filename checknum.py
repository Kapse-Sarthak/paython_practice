def checknum(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"
print(checknum(100))
print(checknum(-100))
print(checknum(0))

    