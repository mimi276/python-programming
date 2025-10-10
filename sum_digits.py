n=int(input("enter a number"))
n2=n
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10

print("sum of digits of",n2,"is=",sum)
