user1=int(input("eneter the first num: "))
user2=int(input("eneter the second num: "))
user3=int(input("eneter the third num: "))

if(user1>user2 and user1>user3):
    print("user1 number is maximum number")
elif(user2>user1 and user2>user3):
    print("user2  number is maximum")
else:
    print("user3 number is minimum number")