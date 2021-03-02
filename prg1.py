inputNum=int(input("enter the number to check perfect square "))


rootNum=int(inputNum ** 0.5)

if rootNum*rootNum==inputNum:
    print(inputNum,"is a perfect square")
else:
      print(inputNum,"is not a perfect square")
