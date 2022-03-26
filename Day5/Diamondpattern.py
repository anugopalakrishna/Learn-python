
#Diamond Pattern
n=int(input("Enter row:"))

#for number of rows
for r in range(1,n):
    #First Half
    for s in range(n,r,-1):
        print(" ",end="")
    for star in range(1,2*r):
        print("*",end="")
    print("")
#Second Half
for r in range(n,0,-1):
    for s in range(n,r,-1):
        print(" ",end="")
    for star in range(1,2*r):
        print("*",end="")
    print("")
