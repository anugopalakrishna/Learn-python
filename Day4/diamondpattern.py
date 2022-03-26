#printing diamond pattern *
n=int(input("Enter no of rows to be printed:"))
k=0
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for k in range(0,2*i-1):
        print("*",end="")
    print()

for i in range(1,n):
    for j in range(1,i+1):
        print(end=" ")
    for l in range(1,(2*(n-i))):
        print("*",end="")
    print()

input()
    
