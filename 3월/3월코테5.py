#나뭇잎 지우는 함수
def removeTree(Tree,idx,time):
    if len(Tree[idx]) != 0:

        list= Tree[idx]
        time +=1
        Tree[idx] = []

        for i in list:

            Tree[i].remove(idx)

        # 가장 길이 긴 애 찾기
        maxl = 0
        idxl=0
        for i in list:
            if len(Tree[i]) > maxl:
                maxl =len(Tree[i])
                idxl=i

        if idxl !=0 :
            time = removeTree(Tree,idxl,time)




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

a = removeTree(Tree,idx,time)
print(a)



