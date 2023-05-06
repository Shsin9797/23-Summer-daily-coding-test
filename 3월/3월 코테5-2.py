#나뭇잎 지우는 함수
def removeTree(Tree,idx,time):
    if len(Tree[idx])!=0:
        #다삭제하고 time+1
        lis= Tree[idx] #임시보관
        Tree[idx] =[]
        for i in lis:
            Tree[i].remove(idx)
        for i in lis:
            time = removeTree(Tree,i,time) # 시작점이 i 가 됨
        #다삭제하고나면
        time+=1
    else:
        time+=1

    return time


N = int(input()) # 정점개수
Tree=[]

for i in range(N+1):
    Tree.append([])

#간선 표시
for i in range(N-1):
    U,V=map(int,input().strip().split()) # 간선이 연결하는 정점
    Tree[U].append(V)
    Tree[V].append(U)

#가장 많은 곳부터 시작해서 하나씩 없애기
maxlen=0
idx=0
time=0
# 가장많이 연결된 애 찾기
for i in range(1,N+1):
    if maxlen < len(Tree[i]):
        maxlen = len(Tree[i])
        idx= i

#트리 함수 시작
a = removeTree(Tree,idx,time)

print(a)



