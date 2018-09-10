#get number
n = int(64)


#print n
"""
print(n)
"""

#subtract 1 till 1
"""
while n!=1:
    n = n-1
    print (n)
"""

# subtract 1 till 1, show even or odd
def minusOne(n):
    while n!=1:
        n = n-1
        print(n)
        if n%2 == 0:
            print("even")
        else:
            print("odd")

print(minusOne(n))
