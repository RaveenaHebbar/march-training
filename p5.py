# sum of digits
inputNum=int(input("Enter the number to find the sum of digits in a number"))

sum=0
tempNum=inputNum
while(tempNum!=0):
    remainderNum=tempNum%10
    tempNum=tempNum//10
    sum=sum+remainderNum

print("count of the number",inputNum,"is",sum)