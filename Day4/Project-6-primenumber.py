n=int(input("Enter number of rows to be printed: "))
counter=0

for i in range(1,n+1):
    if(n%i==0):
         counter=counter+1
         
if (counter==2):
      print("Prime Number")
else:
      print(" Not a Prime Number")
