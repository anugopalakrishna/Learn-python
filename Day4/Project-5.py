n=int(input("Enter number of rows to be printed: "))
         
for i  in range(0,n+1):
      for j in range(1,i+1):
          print("*",end=" ")

for i  in range(n,0,-1):
      for j in range(1,i+1):
          print("*",end=" ")
      print()
