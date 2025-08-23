#6. print maximum num

num1=int(input("enter 1 num: "))
num2=int(input("enter 2 num: "))
num3=int(input("enter 3 num: "))

if(num1>num2 and num1>num3):
    print("num1 is maximum")
elif(num2>num1 and num2>num3):
    print("num2 is maximum")
else:
    print("num3 is maximum")