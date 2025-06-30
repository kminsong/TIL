import sys
import heapq as hq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    min_heap = []   # 최솟값 용
    max_heap = []   # 최댓값 용, 음수로
    k = int(input())    
    hq.heapify(min_heap)    
    hq.heapify(max_heap)
    del_list = {}   # 어떤 숫자들이 있는지, 딕셔네리 형태로, key에 숫자, value에 해당 숫자의 갯수
    vaild = 0   # 현재 유효한 원소 수
    for _ in range(k):
        txt , num = input().strip().split()
        num = int(num)
        if txt == 'I':  # 삽입
            hq.heappush(min_heap, num)
            hq.heappush(max_heap, -num) # 최대는 음수로
            # 삽인한 숫자 del_list에 개수 기록
            if num in del_list: # del_list 딕셔네리에 이미 존재하면 갯수 추가
                del_list[num] += 1
            else:                  # 없으면 1
                del_list[num] = 1
            vaild += 1  # 유효한 원소 수 + 1
        elif txt == "D":    # 최대 최소 중 하나 삭제
            if num == -1:   # 최솟값 삭제
                while min_heap:
                    del_num = hq.heappop(min_heap)  # 가장 작은 값 꺼냄
                    if del_num in del_list and del_list[del_num] > 0:   # 실제 존재하면
                        del_list[del_num] -= 1  # 갯수 감소
                        vaild -= 1  # 유효한 원소 수 - 1
                        break
            
            elif num == 1:  # 최댓값 삭제
                while max_heap:
                    del_num = -hq.heappop(max_heap) # 가장 큰값
                    if del_num in del_list and del_list[del_num] > 0:
                        del_list[del_num] -= 1
                        vaild -= 1
                        break



    if vaild > 0:   # 힙에 원소가 존재할 때 
        # min_heap과 max_heap에서 삭제된 값이 있을 수 있으므로 체크
        while True:
            minanswer = hq.heappop(min_heap)
            if minanswer in del_list and del_list[minanswer] > 0:
                break
        while True:
            maxanswer = -hq.heappop(max_heap)
            if maxanswer in del_list and del_list[maxanswer] > 0:
                break
        print(maxanswer, minanswer)
    
    else:   # 힙이 비었으면
        print("EMPTY")