# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P

n =input()
n=int(n)
L=list(map(int,input().split()))
c=0
f=0

while True:
    for i,v in enumerate(L):
        if v%2!=0:
            f=1
            break
        elif v%2==0:
            L[i]=v/2
    
    if f == 1:
        break
    else:
        c=c+1

print(c)

