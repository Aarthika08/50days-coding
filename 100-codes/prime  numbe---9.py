#prime number--9
n=int(input())
f=0
for i in range(2,n):

    if n%i==0:
        f=1

if f==1:   
    print("NOT PRIME num")
else:
    print("prime num")
