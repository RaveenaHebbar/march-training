# sum of odd placed even digits in a number

inputNum=int(input("Enter the number to find the sum of digits in a number"))


tempNum=inputNum
sumofEvenDigits=0
flag=0
sum1=0
sum2=0


while(tempNum!=0):
    remainderDigit=tempNum%10
    tempNum=tempNum//10

    if remainderDigit%2==0:
        
            sum1 +=remainderDigit
    else:
            sum2 +=remainderDigit

    
    flag=~flag


print("sum of even digits numnber is",inputNum,"is",sum1)
print("sum of odd digits numnber is",inputNum,"is",sum2)