# 2월22일 단순 그래프
N,M =map(int,input().strip().split())

graph = { }
for j in range(1,N+1):
    graph[j]=[]

isSimple=True
for i in range(M):
    U,V = map(int,input().strip().split())
    if V in graph[U] or U is graph[V]:
        isSimple =False
    if U == V :
        isSimple =False
    graph[U].append(V)
    graph[V].append(U)

if isSimple:
    print("YES")
else:
    print("NO")