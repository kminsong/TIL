import sys

sys.stdin = open('list2_practice1_1.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    first_list = []
    final_list = []
    for i in range(n):
        total += arr[i][i]
        total += arr[i][n-i-1]
    if n%2 != 0:
        total -= arr[n//2][n//2]
    print(f'#{tc} {total}')
