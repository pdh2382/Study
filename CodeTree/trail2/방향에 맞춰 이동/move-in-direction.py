n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
x, y = 0, 0

dir_num = []
for i in range(n):
    if dir[i] == "W":
        dir_num.append(0)
    elif dir[i] == "S":
        dir_num.append(1)
    elif dir[i] == "N":
        dir_num.append(2)
    else :
        dir_num.append(3)
 
for i in range(n):
    x = x + int(dist[i])*dx[dir_num[i]]
    y = y + int(dist[i])*dy[dir_num[i]]

print(x, y)
