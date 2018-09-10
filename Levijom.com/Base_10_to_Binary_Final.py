#convert base 10 to binary

"""
b = base number
c = base number converted
z = test value
    1 = true
    0 = false
n = base 2 number directly below b
"""

#get base 10 number from user
b = int(input("Please provide a base 10 number you want in binary: "))
if b <= 0:
    print("you must type a number larger than 0!")
#misc def
c = b
z = 0
n = 0

# find base 2 below or equal to b

#test if c is a power of two (returns 1 for yes, 0 for no)
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

#lower c to a base 2, then set to n
while n != c:
    if twoTest(c)==1:
        n = c
    else:
        c = c-1

    
#convert to binary
while n>.5:
    if b-n >= 0:
        b = b-n
        n = n/2
        print(1)
    else:
        b = b
        n = n/2
        print(0)
        


        
