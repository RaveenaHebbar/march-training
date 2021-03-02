n=int(input("enter the value of n"))
for i in range(1,n+1):
    if i==1 or i==n:
        for j in range(1,n+1):
            print("*",end=" ")
    else:
        for j in range(1,n+1):
            if i==j and i==n//2+1:
                print("0",end=" ")
            elif j==1 or j==n or i==j or j==n-i+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()