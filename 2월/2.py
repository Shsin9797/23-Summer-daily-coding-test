N,M =map(int,input().strip().split())

#리스트 생성
nlist=[]
for i in range(1,N+1):
    nlist.append(i)


for j in range(M):
    U,V =map(int,input().strip().split())
    #N개
    nlist[U-1],nlist[V-1] =  nlist[V-1],nlist[U-1]


#출력
for t in nlist:
    print(t,end=" ")

print()