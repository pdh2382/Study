N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
bad = [0]*N
for i in range(M):
    bad[student[i]-1] += 1
    if bad[student[i]-1] >= K:
        print(student[i])
        break
    if i == M-1 :
        print(-1)
        break
        
