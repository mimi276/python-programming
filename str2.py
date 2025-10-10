s=input("enter a string")
l=len(s)
if l>2:
    if s[-3:]=="ing":
        s1=s.replace(s[-3:],'ly')
        print(s1)
    else:
        s=s+"ing"
        print(s)

else:
    print(s)
    

        
