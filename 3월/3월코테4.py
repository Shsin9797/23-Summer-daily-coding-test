N,M,K =map(int,input().strip().split())
A=list(map(int,input().strip().split()))
A=[0]+A
print(A)
result=True
while True:
    if K==M:
        result=True
        break
    elif A[K]==0:
        result=False
        break
    else:
        t=K
        K = A[t]
        A[t] = 0



if result:
    print('YES')
else:
    print('NO')