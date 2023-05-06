#2월 27일 [중] [그래프] DFS

N,M= map(int,input().strip().split())

#빈그래프 세팅
graph=[]

for i in range(N):
    graph.append([])
    for j in range(N):
        graph[i].append(0)

# 그래프에 값 집어넣기

for j in range(M):
    U, V = map(int, input().strip().split())
    graph[U-1][V-1] +=1
    graph[V-1][U-1] +=1

# 탐색함수
def dfs(here):
    print(here,end=" ")
    # 다른정점들에서 here 과 연결된거 다 True 로 바꿈
    for i in range(N):
        graph[i][here-1] =0 # True 로 두면 1이랑 같은값되어서 안됬던거인듯..

    # graph 에서 1로 적힌거 탐색
    for p in range(N):
        if graph[here-1][p] == 1:
            dfs(p+1)

dfs(1)








'''
1차시도 .. 
# 그래프에 집어넣기
for m in range(M):
    U,V = map(int,input().strip().split())
    graph[U].append(V)
    graph[V].append(U)


print(graph)
# 재귀 탐색함수
def dfs(here):
    print(here, end=" ")
    for i in graph[here]:
        #방문 다 하고 True 로변경
        if i != True:

            idxI = graph[here].index(i)
            graph[here][idxI] = True # 탐색값
            idxHere= graph[i].index(here)
            graph[i][idxHere] =True #상대값
            dfs(i)


dfs(1)

'''