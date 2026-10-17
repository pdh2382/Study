n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
memo_a = 0
memo_b = 0

command_a = []
command_b = []

for i in range(n):
    while t[i] > 0 :
        command_a.append(d[i])
        t[i] -= 1

for i in range(m):
    while t2[i] > 0:
        command_b.append(d2[i])
        t2[i] -= 1

time = len(command_a)

for k in range(time):
    if command_a[k] == 'R':
        memo_a += 1
    else :
        memo_a -= 1
    
    if command_b[k] == 'R':
        memo_b += 1
    else : 
        memo_b -= 1
    
    if memo_a == memo_b :
        print(k+1)
        break
    
    if k == (time - 1):
        print(-1)
    

