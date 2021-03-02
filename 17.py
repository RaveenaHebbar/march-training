# Find the number of pairs of brackets if arranged properly



brackets=input("enter the string of brackets")
oc=0
cc=0
flag=True

for ch in brackets:
    if ch=="{":
        oc+=1
    else:
        cc+=1
    if cc>oc:
        flag=False
        break
if flag and oc==cc:
    print("Number of pairs is ",oc)
else:
    print("Brackets not arranged properly")