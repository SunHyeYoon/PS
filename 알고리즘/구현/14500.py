import sys; input = sys.stdin.readline

def dfs(x, y, step, total):
    global answer

    # 탐색을 계속 진행해도 최댓값보다 작은 경우
    if total + max_val * (4 - step) <= answer:
        return

    if step == 4:
        answer = max(answer, total)
        return
    
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue
        # 'ㅏ', 'ㅓ', 'ㅗ', 'ㅜ' 모양 탐색
        if step == 2:
            visited[nx][ny] = True
            dfs(x, y, step + 1, total + board[nx][ny])  # 기존 좌표에서 시작
            visited[nx][ny] = False

        visited[nx][ny] = True
        dfs(nx, ny, step + 1, total + board[nx][ny])
        visited[nx][ny] = False


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_val = max(map(max, board))

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0

for i in range(n):
    for j in range(m): 
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(answer)
