a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:"))
if(num1>0 and num2>0  and num3>0):
    if(num1 > num2 and num1> num3):
        print("num1 is greatest value among all threes!")
    elif(num2> num1 and num2> num3):
        print("num2 is greatest value among all threes!")
    elif(num3 >num1 and num3 >num2):
        print("num3 is greatest value among all thress!")
else:
    print("re-enter your value")