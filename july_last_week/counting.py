data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0]*5              # data가 0~4까지의 정수

N = len(data)               # data의 크기
temp = [0]*N                # 정렬된 결과 저장

# 1단계 : data 원소 별 개수 세기
for x in data:      # data의 원소 x를 가져와서 counts[x]에 개수 기록
    counts[x] += 1  # 왜 이게 나오지?

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):   # 왜 5냐? : counts에서 가져오는데 counts에 4까지 나와야  되니깐 : counts[1]~ counts[4]까지
    counts[i] = counts[i-1] + counts[i]

# 3단계 : data의 맨 뒤부터 temp에 자리 잡기
for i in range(N-1, -1, -1):
    counts[data[i]] -= 1        # 누적 개수 1개 감소
    idx = counts[data[i]]
    #temp[counts[data[i]]]
    temp[idx] = data[i]

print(*temp)



# def counting_sort(data, temp, k):
#     #data [] : 입력 배열 0 to k
#     #temp [] : 정렬된 배열
#     #counts[] : 카운트 배열
#     counts = [0] * (k+1)
#     for i in range(len(data)):
#         counts[data[i]] += 1
#     for i in range(1, k+1):
#         counts[i] += counts[i-1]
    
#     for i in range(len(temp)-1, -1, -1):
#         counts[data[i]] -= 1
#         temp[counts[data[i]]] = data[i]
            