T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
 
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
 
    row, col = 0, 0
    idx = 0
 
    for i in range(1,N*N + 1):
      arr[row][col] = i
      row += dx[idx]
      col += dy[idx]
 
      if not(N > row >= 0) or not(N > col >= 0) or arr[row][col] != 0:
        row -= dx[idx]
        col -= dy[idx]
        idx += 1

        if idx == 4:
            idx = 0
        
        row += dx[idx]
        col += dy[idx]

    print('#{}'.format(tc))
    for i in arr:
        ans = ' '.join(map(str, i))
        print(ans)
