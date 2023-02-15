N= int(input())
A=list(map(int,input().strip().split()))
i=0
find=True


#i:받침대 놓는곳
for i in range(1,N):
    find=False
    # 양쪽 합 구하기
    s1=0
    s2=0
    for l in range(0,i):
        s1 +=A[l]

    for r in range(i+1,N):
        s2 +=A[r]


    # 합 비교하기
    if s1==s2 :
        find=True
        break


if find:
    print(i+1)
else:
    print(-1)