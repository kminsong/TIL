import sys
import math
input = sys.stdin.readline
N, M = map(int, input().split())
for i in range(N, M+1):
    if i == 1:
        pass
    elif i == 2:
        print(2)
    else:
        b = 0
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0:
                b = -1
                break
        if b == 0:
            print(i)
