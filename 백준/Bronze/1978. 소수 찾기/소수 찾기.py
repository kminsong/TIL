n = int(input())
lst = list(map(int, input().split()))
count_numb = 0
for i in lst:
    b = 0
    if i == 1:
        b = -1
    else:
        for j in range(2, i):
            if i % j == 0:
                b = -1
                break
    if b == 0:
        count_numb+=1
print(count_numb)