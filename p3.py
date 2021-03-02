# find Biggest digit 



inputNum=int(input("Enter the number to find the biggest digit in the number"))



tempNum=inputNum
bigdigit=0

while(tempNum!=0):
   remainderNum=tempNum%10
   tempNum=tempNum//10

   if bigdigit<remainderNum:
       bigdigit=remainderNum
       print("Biggest digit in",inputNum,"is",bigdigit)