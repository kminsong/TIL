import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
answer = []
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
def bfs(s):
    visited = [-1] * (N+1)
    global cnt, fin_cnt
    q = deque()
    q.append(s)
    visited[s] = 0
    total_visit = 0
    while q:
        t = q.popleft()
        for w in lst[t]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[t] + 1
                total_visit += visited[w]
    return total_visit

for i in range(1, N+1):
    answer.append((bfs(i), i))
answer.sort()
print(answer[0][-1])



