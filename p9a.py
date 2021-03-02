inputNum=int(input("enter the odd placed even digit"))

tempNum=inputNum
falg=True
sum1=0
sum2=0
while(tempNum!=0):
    remainderNum=tempNum%10
    tempNum=tempNum//10

    if remainderNum%2==1:
      sum1+=remainderNum
    else:
      sum2+=remainderNum

print("sum of odd placed ",inputNum,"is",sum2)