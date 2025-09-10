n=int(input("enetr the num of row: "))
for i in range(0,n):
    # print("_",end=" ")
    for j in range(n-i-1):
        print("_",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()