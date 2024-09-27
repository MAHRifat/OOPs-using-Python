# https://atcoder.jp/contests/arc087/tasks/arc087_a

N =input()
n=int(N)
L=[]
count=0
visited=[]
for i in range(0,n):
    i=input()
    m=int(i)
    L.append(m)

m = max(L)
for i in range(0,m+1):
    visited.append(False)

for i in L:
    if visited[i] == True:
        continue
    c=L.count(i)
    visited[i]=True
    if c > i:
        count = count + abs(c-i)
    elif c < i:
        count = count + c

print(count)