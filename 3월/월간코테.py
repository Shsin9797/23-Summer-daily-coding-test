A,B=map(int,input().strip().split())
count=0

while True:
    if A>1 and B>0:
        A-=2
        B -=1
        count +=1
    else:
        break
print(count)

