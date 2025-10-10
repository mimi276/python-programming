n=[1,2,4,6,8,9,12,16,21,31]
print("list is",n)
print("list after removing even numbers")
for i in n:
    if(i%2==0):continue
    print(i)
