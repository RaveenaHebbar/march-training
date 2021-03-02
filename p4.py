# count of digits in a number

inputNum=int(input("Enter the number to find the count of digits in a number"))

count=0
tempNum=inputNum
while(tempNum!=0):
    remainderNum=tempNum%10
    count=count+1
    tempNum=tempNum//10


print("count of the number",inputNum,"is",count)