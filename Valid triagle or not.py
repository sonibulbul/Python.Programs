#triangle is 180 or not
tri1=int(input("enter first angle: "))
tri2=int(input("enter second angle: "))
tri3=int(input("enter third angle: "))
sum=tri1+tri2+tri3
if(sum==180):
    print(sum,"triangle is valid!!!")
else:
    print(sum,"it is not a valid triangle , it is not equal to 180")

