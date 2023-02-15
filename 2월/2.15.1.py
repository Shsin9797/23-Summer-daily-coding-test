a,b =map(int,input().strip().split())
c= a+b%2
e= a+b//2

if a<b :
    d = abs(b-e)
else:
    d= abs(a-e)

print(c,d)



