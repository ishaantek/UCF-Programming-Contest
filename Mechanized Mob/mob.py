import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().rstrip('\n')) for _ in range(n)]

dir_map = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

robots = []
robot_index = [[-1]*m for _ in range(n)]
robot_count = 0
for r in range(n):
    for c in range(m):
        ch = grid[r][c]
        if ch in dir_map:
            robots.append((r, c, ch))
            robot_index[r][c] = robot_count
            robot_count += 1

adj = [[] for _ in range(robot_count)]    # adjacency list
indegree = [0]*robot_count

for i, (r, c, dch) in enumerate(robots):
    dr, dc = dir_map[dch]
    rr, cc = r+dr, c+dc
    blocked = -1
    while 0 <= rr < n and 0 <= cc < m:
        if robot_index[rr][cc] != -1:
            blocked = robot_index[rr][cc]
            break
        rr += dr
        cc += dc
    if blocked != -1:
        adj[blocked].append(i)
        indegree[i] += 1

from collections import deque

q = deque()
for i in range(robot_count):
    if indegree[i] == 0:
        q.append(i)

order = []
while q:
    u = q.popleft()
    order.append(u)
    for w in adj[u]:
        indegree[w] -= 1
        if indegree[w] == 0:
            q.append(w)

if len(order) != robot_count:
    print("Dang Roombas!")
else:
    for idx in order:
        r, c, _ = robots[idx]
        print(r+1, c+1)
