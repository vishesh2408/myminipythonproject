cakeangle=eval(input("Enter the angle of the cake: "))
n=eval(input("Enter n: "))
if(cakeangle%n==0):
    print("YES cake will cut in equal pieces of size %d"%n)
else:
    print("NO cake will cut in equal pieces of size %d"%n)
if(n>cakeangle):
    print("NO cake will not cut in equal pieces of size %d"%n)
else:
    print("YES the cake will cut in any pieces of size %d"%n)
n=1
for i in range(n):
    cakeangle-=n
    n+=1
    if(cakeangle<0):
        print("NO cake will not cut in equal pieces of size %d"%n)
        break
    else:
        print("YES the cake will cut into %d pieces such that no two of them are equal"%n)