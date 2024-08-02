import sys

sys.stdin = open('list2_practice.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열 정의
    di = [0, -1, 0, 1]      # 상하좌우 i(행) 증감설정
    dj = [1, 0, -1, 0]      # 상하좌우 j(열) 증감설정
    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):      # arr[di][dj]가 4가지 경우 존재
                ni = i + di[k]
                nj = j + dj[k]
                if 0<= ni < N and 0 <=nj <N:    # 유효한 인덱스일 경우
                    total += abs(arr[i][j] - arr[ni][nj])
    print(f'#{tc} {total}')


