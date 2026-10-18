N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
honor = [] # 명예의 전당 기록용
command_a = [] # 1시간 단위로 얼마나 이동시키는지로 입력 형태 변경
command_b = []
for i in range(N):
    while t[i] >0:
        command_a.append(v[i])
        t[i]-=1

for i in range(M):
    while t2[i] >0:
        command_b.append(v2[i])
        t2[i]-=1
    
time = len(command_a) # 총 시간 

# A, B 위치 기록
memo_a = 0
memo_b = 0
cnt = 0

for i in range(time):
    memo_a += command_a[i]
    memo_b += command_b[i]
    past_honor = honor

    if memo_a > memo_b :
        honor = ["A"]
    elif memo_a < memo_b :
        honor = ["B"]
    else : 
        honor = ["A", "B"]
    
    if past_honor != honor :
        cnt += 1

print(cnt)