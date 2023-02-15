N=int(input()) # 노래개수
B = list(map(int,input().strip().split()))
M = int(input()) # 물어보는 개수
Q = list(map(int,input().strip().split())) # 질문들

#노래 길이 합 리스트
sumS =[]
for i in range(N):
    if i ==0:
        ss=B[i]
    else:
        ss = sumS[i-1]+B[i]
    sumS.append(ss)


#질문 수행
total=0
for j in range(M):
    que = Q[j]
    if que > sumS[-1]:
        que = que % sumS[-1]
    for song in sumS:
        if song >= que : # 같거나 작아지는순간
            total += (sumS.index(song)+1)
            break


#출력
print(total%1000000007)