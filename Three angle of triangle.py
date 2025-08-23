#7 find three angles right,acute,obtuse

angle1=int(input("enter angle 1: "))
angle2=int(input("enter angle 2: "))
angle3=int(input("enter angle 3: "))
sum=angle1 + angle2 + angle3
if(sum==90):
    print(sum," is an right angle triangle: ")
elif(sum >90 and sum<180):
    print(sum,"is an obtuse angle triangle")
else:
    print(sum,"acute angle triangle")