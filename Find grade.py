grade=int(input("enter the number: "))
if(grade>85):
    print("A+")
elif(grade<85 and grade>65):
    print("A")
elif(grade<65 and grade>45):
    print("B")
elif(grade<45 and grade>25):
    print("B")
else:
    print("D")