import sys
input = sys.stdin.readline
N, M = map(int, input().split())
gender = list(input().split())
uvds = []
for _ in range(M):
    u, v, d = map(int, input().split())
    uvds.append((d, v, u))
uvds.sort()
answer = 0
check = 0

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:   # 더 작은 번호를 부모로
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N + 1)]

for uvd in uvds:
    distance, a, b = uvd
    if find_parent(a) != find_parent(b) and gender[a - 1] != gender[b - 1]:
        union_parent(a, b)
        answer += distance
        check += 1

if check == N - 1:
    print(answer)
else:
    print(-1)
