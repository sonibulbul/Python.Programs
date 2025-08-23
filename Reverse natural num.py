N=int(input("enter the num: "))
rev=0
while(N>0):
    digit=N%10
    N=N//10
    rev=rev*10+digit
    print(digit,end=" ")



