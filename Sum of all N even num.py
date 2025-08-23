N=int(input("enter the num: "))
sum=0
while(N>0):
    if(N%2==0):
        sum+=N
    N-=1
print(sum)