# arr1 = [0] * 3
#
# arr2 = [[0] * 3 for _ in range(2)]
# print(arr1)
# print(*arr1)
# for i in range(2):
#     print(*arr2[i])
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end = ' ')
#     print()

# arr = [[1,2,3], [4,5,6]]
# print(len(arr)) # 행의 갯수 출력
# print(len(arr[0]))  # 첫 행의 길이(원소의 갯수) 출력

# arr= [[0]*3] * 2    # 이렇게 하면 안된다.
# print(arr)
# arr[0][0] = 1       # 이렇게 쓰지 말라고 알려주는 거다 , 위에 있는데로 for문을 써라
# print(arr)

# for i in range(n):
#     for j in range(m):
#         f(array[i][j])
#         s+= array[i][j]