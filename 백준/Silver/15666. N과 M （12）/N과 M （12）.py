import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
n = len(arr)
ans = []
def back(n, s, tlst):
    if n == M:
        ans.append(tlst)
        return
    prev = 0 
    for j in range(s, N):
        if prev != arr[j]:
            prev = arr[j]
            back(n+1, j, tlst + [arr[j]])


back(0, 0, [])
for lst in ans:
    print(*lst)