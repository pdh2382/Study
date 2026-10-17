n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
head = 0
cnt = 0
command_a = []
command_b = []
memo_a = 0
memo_b = 0

for i in range(n):
    while t[i] > 0:
        command_a.append(v[i])
        t[i] -= 1

for i in range(m):
    while t2[i] > 0:
        command_b.append(v2[i])
        t2[i] -= 1

time = len(command_a)

for i in range(time) :
    memo_a += command_a[i]
    memo_b += command_b[i]
    if head == 0:
        if memo_a > memo_b :
            head = 'A'
        elif memo_a < memo_b :
            head = 'B'
        else : 
            head = 0
    else :
        if  memo_a > memo_b:
            if head == 'B':
                head = 'A'
                cnt += 1
        elif memo_a < memo_b:
            if head == 'A':
                head = 'B'
                cnt += 1

print(cnt)
