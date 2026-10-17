n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
command_a = [] # A의 움직임을 [L, L, R, R, R]과 같이 표현함.
command_b = []
flag = True
memo_a = 0 # A의 현재 위치 표시
memo_b = 0 # B의 현재 위치 표시

for i in range(n):
    while t[i] > 0:
        command_a.append(d[i])
        t[i] -= 1

for i in range(m):
    while t_b[i] > 0:
        command_b.append(d_b[i])
        t_b[i] -= 1

time = max(len(command_a), len(command_b))
cnt = 0

for i in range(time):
    if i > (len(command_a)-1): # 만약 A의 이동이 끝났다면
        for j in range(i, time):
            # B만 이동
            if command_b[j] == 'R':
                memo_b += 1
            else :
                memo_b -= 1
            # 겹쳤는지 확인, cnt올리기
            if flag == False and memo_a == memo_b :
                cnt += 1
                flag = True
            elif flag == True and memo_a != memo_b :
                flag = False
        break
    elif i > (len(command_b)-1): # 만약 B의 이동이 끝났다면
        for j in range(i, time):
            # A의 이동
            if command_a[j] == 'R':
                memo_a += 1
            else :
                memo_a -= 1
            # 겹쳤는지 확인, cnt올리기
            if flag == False and memo_a == memo_b :
                cnt += 1
                flag = True
            elif flag == True and memo_a != memo_b :
                flag = False
        break
    else:
        if command_a[i] == 'R':
            memo_a += 1
        else :
            memo_a -= 1

        if command_b[i] == 'R':
            memo_b += 1
        else :
            memo_b -= 1

        if flag == False and memo_a == memo_b :
            cnt += 1
            flag = True
        elif flag == True and memo_a != memo_b :
            flag = False
        

print(cnt)
