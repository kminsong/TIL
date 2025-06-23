import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
move = {}
for _ in range(N + M):
    x, y = map(int, input().split())
    move[x] = y
arr = [0] * 101
visited = [0] * 101
q = deque()
q.append(1)
visited[1] = True
while q:
    current = q.popleft()

    for i in range(1, 7):
        next = current + i
        if 0 < next <= 100 and not visited[next]:
            if next in move:
                next = move[next]
            if not visited[next]:
                q.append(next)
                visited[next] = True
                arr[next] = arr[current] + 1
print(arr[100])
        


