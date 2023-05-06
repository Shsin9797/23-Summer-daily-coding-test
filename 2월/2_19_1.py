T= int(input()) # 테스트 케이스 개수

#UUUUmmm 의경우를 확인안했음. . U 가 시작하는게 아니라 U에서 m ㅇ로 전환되는부분 부터 확인해야함
#Umm문자열 확인함수 정의
def isUm(N,S,A,B):
    if N < 3:
        return False
    #잘라온 리스트에서 하나씩 가져온다
    for i in range(A-1,B):
        if ((B - 1) - i) < 2:
            return False
        if (S[i] == "U") and (S[i+1] =='m'): # U 가 m으로 변경 시 카운팅 시작
            if ((B - 1) - i) < 2:
                return False
            for t in range(i+1,B):
                if S[t] != 'm':
                    return False

            #for 문 다 돌았는데 다 m 이면
            return True


for i in range(T):
    N,M =map(int,input().strip().split()) #N:문자열길이 M:관찰횟수
    S = input()
    count=0
    #테스트 시작
    for j in range(M):
        A,B= map(int,input().strip().split())

        # A 부터 B 까지가 Umm 문자열인지 확인
        #Umm문자열 확인 함수 호출
        if isUm(N,S,A,B):
            count+=1

    #테스트 종료후 개수 출력
    print(count)
