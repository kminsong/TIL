import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 0, max(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2
    h = 0
    for i in lst:
        if i > mid:
            h += i-mid
    if h >= M:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)