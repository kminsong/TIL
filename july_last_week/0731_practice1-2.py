import sys

sys.stdin = open('0731_practice1-2.txt')

# Testcase 수
# T = int(input())
# Testcase 만큼 반복
# for tc in range(1, T+1):
#     pass
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# print(arr)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
total = 0
for i in range(N):
    for j in range(N):  # NxN 배열의 모든 원소에 대해
        s = 0           # 문제에서 원소와 인접원소의 차의.... 합 저장
        # i, j 원소의 4방향 원소에 대해
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni < N and 0<= nj < N:
                s += abs(arr[i][j] - arr[ni][nj])                                # 실존하는 인접원소 ni, nj
                #f(arr[ni][nj])
        print(s, end= ' ')
        total += s
    print()
print(total)