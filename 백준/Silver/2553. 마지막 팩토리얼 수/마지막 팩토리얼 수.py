import sys
sys.setrecursionlimit(100000)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
num = str(factorial(n))
answer = 0
for i in num[::-1]:
    if i != '0':
        answer = int(i)
        break
print(answer)