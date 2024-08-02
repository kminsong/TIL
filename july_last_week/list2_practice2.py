import sys

sys.stdin = open('list2_practice2.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
def sum_all(lst):
    sum_v = 0
    for i in lst:
        sum_v += i
    return sum_v
for tc in range(1, T+1):
    pass
    arr = list(map(int, input().split()))
    final_list = []
    tandf = 0
    for i in range(1<<10):
        mid_list = []
        for j in range(10):
            if i & (1<<j):
                mid_list.append(arr[j])
            #print(mid_list)    # mid_list 확인
        final_list.append((mid_list))
    #print(final_list)  # final_list 확인
    for i in final_list:    # 공집합 제거
        if i == []:
            final_list.remove(i)
    for i in final_list:
        if sum_all(i) == 0:
            tandf = 1
            break
    print(f'#{tc} {tandf}')