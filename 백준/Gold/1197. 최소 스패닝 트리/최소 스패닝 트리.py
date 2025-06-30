import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V, E = map(int, input().split())
edge = []   # 간선 정보
parent = [] # union - find용 부모 노드

for _ in range(E):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))  # sort하려고 가중치를 앞에 둠

for i in range(V+1):    # 부모 노드를 자기 자신으로 초기화
    parent.append(i)

edge.sort() # 가중치 기준으로 간선 정렬
result = 0

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

# 간선 하나씩 확인해서 최소 스패닝 트리
for c, a, b in edge:
    if find_parent(a) != find_parent(b):    # 사이클 방지
        union_parent(a, b)      
        result += c

print(result)