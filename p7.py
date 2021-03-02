# Find sum of Even/Odd digits in a number

inputNum=int(input("enter the number to find Sum of Odd digits in a number"))

tempNum=inputNum
sumOfOddDigits=0

while tempNum!=0:

    remainderDigit=tempNum%10
    tempNum=tempNum//10
    if remainderDigit%2!=0:
        sumOfOddDigits += remainderDigit
print("sum of the digit of ",inputNum,"is",sumOfOddDigits)

