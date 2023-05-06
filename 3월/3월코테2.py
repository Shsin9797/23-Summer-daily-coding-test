N=int(input())
X,Y,Z=1,2,3

for i in range(1,N):
    tem=X
    X=Y
    Y=Z
    Z=tem
print(X,Y,Z)