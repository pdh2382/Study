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
    i_can_infect = (fcnt[i-1] > 0) # 처음에 이런 식으로 최초 감염여부를 저장을 안 해둬서, 
    j_can_infect = (fcnt[j-1] > 0)

    if i_can_infect: 
        fcnt[i-1] -= 1
        if ismemo[j-1] != 1:  # 여기서 바꾼 감염상태가 밑의 조건문에도 영향을 미쳤었음.
            ismemo[j-1] = 1
            fcnt[j-1] = K
    if j_can_infect: 
        fcnt[j-1] -= 1
        if ismemo[i-1] != 1: 
            ismemo[i-1] = 1
            fcnt[i-1] = K
    
for i in range(N):
    print(ismemo[i], end = '')

# 따라서 최초 감염상태를 따로 저장하고 그걸 활용해서 문제 해결.
