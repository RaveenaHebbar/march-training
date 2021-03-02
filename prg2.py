# find smallest digit in a integer number

inputNum=int(input("enter a number to find smallest digit in it:"))

tempNum=inputNum
smallDigit=9

while (tempNum!=0):
    remainderNum=tempNum%10
    tempNum=tempNum//10
    if smallDigit>remainderNum:
        smallDigit=remainderNum
print("Smallest digit in",inputNum,"is",smallDigit)

