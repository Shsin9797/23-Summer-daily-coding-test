N,M= map(int,input().strip().split())

graph={}
for j in range(1,N+1):
    graph[j]=[]

for i in range(M):
    U,V=map(int,input().strip().split())
    graph[U].append(V)
    graph[V].append(U)


K= int(input())
t = list(map(int,input().strip().split()))

isExist=True
for y in range(K-1):
    a= t[y]
    b= t[y+1]

    if b not in graph[a]:
        isExist= False

if isExist :
    print('YES')
else:
    print('NO')
