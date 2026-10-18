dirs = input()

# Please write your code here.
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0

for i in range(len(dirs)):
    if dirs[i] == "L":
        dir = (dir + 3) % 4
    elif dirs[i] == "R":
        dir = (dir + 1) % 4
    else : 
        x = x + dx[dir]
        y = y + dy[dir]

print(x, y)