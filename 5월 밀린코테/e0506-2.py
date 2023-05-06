#2월 23일 [중] [그래프] 정점의 차수
N,M= map(int,input().strip().split())
graph={}
for j in range(1,N+1):
    graph[j]=[]



for i in range(M):
    U,V=map(int,input().strip().split())
    graph[U].append(V)
    graph[V].append(U)

sum=0

for t in range(1,N+1):
    sum+= len(graph[t])

print(sum)