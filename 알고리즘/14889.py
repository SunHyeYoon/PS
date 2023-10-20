# 조합 이용

from itertools import combinations

n = int(input())

stat = [list(map(int, input().split())) for _ in range(n)]

team = list(combinations(range(n), n//2))
mn = float('inf')

for i in range(len(team)//2):
    start = list(team[i])
    link = list(set(range(n)) - set(start))

    sum1 = sum(stat[x][y] + stat[y][x] for x, y in combinations(start, 2))
    sum2 = sum(stat[x][y] + stat[y][x] for x, y in combinations(link, 2))

    mn = min(mn, abs(sum1 - sum2))

print(mn)
