N, M = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 0, max(lst)
answer = 0
while start <= end:
    mid = (start + end) // 2
    height = 0
    for i in lst:
        if i > mid:
            height += i-mid
    if height >= M:
        answer = mid
        start = mid+1
    else:
        end = mid-1
print(answer)