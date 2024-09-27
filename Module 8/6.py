# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/V
N, M = map(int, input().split())
A = list(map(int, input().split()))

count = {}

for num in A:
    count[num] = count.get(num, 0) + 1

for num in range(1, M + 1):
    print(count.get(num, 0))
