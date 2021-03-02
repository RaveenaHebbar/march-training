bracket=input("enter the string of the bracket")

ocf=0
ccf=0
ocp=0
ccp=0
flag=True
stk=[]

for i in range(len(bracket)):
    if bracket[i]=="{":
        stk.append("}")
        ocf+=1
    elif bracket[i]=="(":
        stk.append(")")
        ocp+=1
    elif bracket[i]=="}":
        if bracket[i]!=stk[-1]:
            flag=False
            break
        else:
            ccf+=1
            stk.pop()
    elif bracket[i]==")":
        if bracket[i]!=stk[-1]:
            flag=False
            break
        else:
            ccp+=1
            stk.pop()
if flag and ocf==ccf and ocp==ccp:
    print("Flower bracket pairs is",ocf,"parenthesis pairs is",ocp)
else:
    print("not properly arranged")