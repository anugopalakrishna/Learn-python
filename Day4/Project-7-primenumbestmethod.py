n=int(input("Enter number of rows to be printed: "))


isprime=True
for i in range(2,n):
    if(n%i==0):
        isprime=False
        break

if(isprime):
    print("Prime Number")

else:
    print("Not a Prime Number")

