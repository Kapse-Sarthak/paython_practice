def largenum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(largenum(10,20,30))
print(largenum(20,10,40))
print(largenum(40,5,60))
print(largenum(20,30,40))