#test if a number is a power of 2

#get user input
c = int(input("Number: "))

while c>.5:
    if c%2 == 0:
        c = c/2
    elif c == 1:
        z = int(1)
        c=0
    elif c%2 != 0:
        c = 0
        z = int(0)
        
print(z)
