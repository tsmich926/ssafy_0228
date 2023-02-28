# R,C = map(int,input().split())
# arr = [list(input()) for _ in range(R)]
# #가로탐색
# lst= []
# col = 0
# for row in range(R):
#     for col in range(C):
#     while 0<=row<R and 0<=col<C and arr[row][col] != '#':
#         if arr[row+1][col+1] != '#':
#             st = "" 
#             st += arr[row][col]
#         col += 1
#         lst.append(st)
# print(lst)
                                
#세로탐색


R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
col = 0
#가로 탐색
lst = []

for row in range(R):
    st = "" 
    while 0<=row<R and 0<=col<C and arr[row][col] != '#':
        st += arr[row][col]
        col += 1
    if len(st)>= 2:
        lst.append(st)
    print(lst)