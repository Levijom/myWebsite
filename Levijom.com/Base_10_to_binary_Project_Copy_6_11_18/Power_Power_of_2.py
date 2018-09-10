#Find lower power of 2

#get user input
g = int(input("Number for lower 2 power: "))

c=g
n = 0

def twoTest(c):
    while c>.5:
        if c%2 == 0:
            c = c/2
        elif c == 1:
            z = int(1)
            c=0
        elif c%2 != 0:
            c = 0
            z = int(0)
        
    return(z)

while n != c:
    if twoTest(c)==1:
        n = c
    else:
        c = c-1
print(n)
