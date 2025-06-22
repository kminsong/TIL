import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
ans = 0
left = 0
count = {}
type_count = 0
for i in range(N):
    if arr[i] in count:
        count[arr[i]] += 1
    else:
        count[arr[i]] = 1
        type_count += 1
    while type_count > 2:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
            type_count -= 1
        left += 1

    ans = max(ans, i - left + 1)

print(ans)