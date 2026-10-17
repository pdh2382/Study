N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
ismemo = [0]*N # 감염여부 기록용 (0 음성, 1 양성)
fcnt = [0]*N # 남은 전염횟수 기록용
ismemo[P-1] = 1
fcnt[P-1] = K

handshakes.sort(key = lambda x : x[0])
handshakes = [t[1:] for t in handshakes]

for i, j in handshakes:
    i_can_infect = (fcnt[i-1] > 0)
    j_can_infect = (fcnt[j-1] > 0)

    if i_can_infect: 
        fcnt[i-1] -= 1
        if ismemo[j-1] != 1: 
            ismemo[j-1] = 1
            fcnt[j-1] = K
    if j_can_infect: 
        fcnt[j-1] -= 1
        if ismemo[i-1] != 1: 
            ismemo[i-1] = 1
            fcnt[i-1] = K
    
for i in range(N):
    print(ismemo[i], end = '')

