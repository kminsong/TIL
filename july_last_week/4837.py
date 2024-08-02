import sys

sys.stdin = open('4837.txt')
def sum_all(lst):       #sum을 대신할 sum_all 함수 정의
    sum_v = 0
    for i in lst:
        sum_v += i
    return sum_v
# Testcase 수
T = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]   # arr 정의
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    final_list = []     # 만들어진 부분집합들 하나의 리스트에 추가
    for i in range(1<<len(arr)):
        mid_list =[]    # 각각의 부분집합 리스트화
        for j in range(len(arr)):
            if i&(1<<j):
                mid_list.append(arr[j]) # 각각의 부분집합에 추가
        final_list.append(mid_list)     # 각각의 부분집합을 최종 리스트에 추가
    #print(final_list)  # final_list가 부분집합리스트를 갖은 채로 출력되는지 확인
    for i in final_list:    # final_list의 각 부분집합 하나씩
        if sum_all(i) == K and len(i) == N: # 그 합이 k인지, 길이가 i인지 확인
            count+=1
    print(f'#{tc} {count}')



