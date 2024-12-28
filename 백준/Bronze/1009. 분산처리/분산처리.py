# 입력 받기
t = int(input())  # 테스트 케이스 수
results = []

for _ in range(t):
    a, b = map(int, input().split())
    a %= 10 
    if a == 0:
        results.append(10)
    else:
        cycle = []
        value = a
        while value not in cycle:
            cycle.append(value)
            value = (value * a) % 10
        idx = (b - 1) % len(cycle)
        results.append(cycle[idx])

for res in results:
    print(res)
