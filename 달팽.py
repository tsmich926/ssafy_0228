N = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 0
row = N//2
col = N//2
arr = [[0] * N for _ in range(N)]
for i in range(1, N * N + 1):
    # print(row,col)
    arr[row][col] = i
    newr = row + dr[d]
    newc = col + dc[d]
    if 0 > newr or newr >= N or newc < 0 or newc >= N or arr[newr][newc] != 0:  # 범위 밖
        d = (d + 1) % 4
    row = row + dr[d]
    col = col + dc[d]

for i in arr:
    print(*i)