import sys
from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1 # 1은 사과

l = int(input())

rotate = []
for _ in range(l):
    rotate.append(sys.stdin.readline().split())

def OOB(x, y):
    return x < 0 or y < 0 or x >= n or y >= n or board[x][y] == 2
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
now = 1 # 현재 뱀의 방향
x, y = 0, 0    # 현재 위치
board[x][y] = 2 # 2는 뱀의 몸통
snake = deque()
snake.append((0, 0))

while True:
    if rotate and int(rotate[0][0]) == time:
        _, dir = rotate.pop(0)
        if dir == 'L':
            now = (now - 1) % 4
        else:
            now = (now + 1) % 4
    nx = x + dx[now]
    ny = y + dy[now]

    if not OOB(nx, ny):
        x, y = nx, ny  
        snake.appendleft((nx, ny)) 
        if board[nx][ny] == 0:  # 사과가 없으면
            tail_x, tail_y = snake.pop()
            board[tail_x][tail_y] = 0
        board[nx][ny] = 2
        time += 1
    else:
        break

print(time + 1)
