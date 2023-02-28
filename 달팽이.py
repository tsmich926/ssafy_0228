N = int(input()) # 홀수
arr = [[0]*N for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 0
#시작좌표
row = N//2
col = N//2
for t in range(1,N*N+1):
    arr[row][col] = t
    newr = row + dr[d]
    newc = col + dc[d]
    if newr < 0 or newr <= N or newc < 0 or newc<=N or arr[newr][newc] != 0: #범위를 벗어났거나 숫자가 이미 채워져있으면
        d = (d+1)%4

    row = row + dr[d]
    col = col + dc[d]

print(arr)
