#4월 3일 [하] [DP] 피보나치 수열

N= int(input())

A=1
B=2

print(A,B)
for i in range(N):
    if A<B:
        A=A+B
    else:
        B=A+B
    print(A,B)