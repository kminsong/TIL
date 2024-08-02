import sys

sys.stdin = open('1209.txt')

# Testcase 수

# Testcase 만큼 반복
for k in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0

    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[i][j]
        if max_v <= s:
            max_v = s
    for j in range(100):
        s = 0
        for i in range(100):
            s += arr[i][j]
        if max_v <= s:
            max_v = s
    x = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                x += arr[i][j]
    if max_v <= x:
        max_v = x

    y = 0
    for i in range(100):
        for j in range(100):
            if 2-i == j:
                y += arr[i][j]
    if max_v <= y:
        max_v = y

        # y += arr[i][99-i]
    # if max_v <= y:
    #     max_v = y



    print(f'#{tc} {max_v}')
