def sum_digit(a):
    sum=0
    while a>0:
        d=a%10
        sum=sum+d
        a=a//10
    return sum
    
n=int(input("enter a number"))
s=sum_digit(n)
print("sum",s)
