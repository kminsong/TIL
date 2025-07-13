import sys
input = sys.stdin.readline
N=int(input())

dp ='I'+'OI'*(N)


M=int(input())
S=input()
start =0
cnt=0
while start<=M-N:
    if S[start:start + 2*N + 1] == dp:
        cnt+=1
        start+=2
    else:
        start+=1
print(cnt)