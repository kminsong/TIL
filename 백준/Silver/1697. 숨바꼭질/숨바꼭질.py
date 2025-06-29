from collections import deque

def BFS(v):
    q = deque()
    visited = [0] * 100001
    visited[v] = 1
    q.append(v)
    while q:
        x = q.popleft()

        if x == K:
            return visited[x]
        
        for y in (x - 1, x + 1, 2 * x):
            if 0 <= y <= 100000 and visited[y] == 0:
                visited[y] = visited[x] + 1
                q.append(y)

N, K = map(int, input().split())
print(BFS(N)-1)


