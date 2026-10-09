# 신경망
# 활성화 함수
# 단층 퍼셉트론에서 층을 깊게 하고, 비선형성을 주는 데에 목적이 있음.

import numpy as np
import matplotlib.pylab as plt
# 계단 함수
def step_function(x):
    if x > 0:
        return x
    else :
        return 0

# 넘파이 배열을 집어넣을 수 있게 세팅
def step_function(x):
    y = x > 0
    return y.astype(int)

x = np.array({-1.0, 1.0, 2.0})
step_function(x)

# 계단함수 그래프 그리기
x = np.arrange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1,1)
plt.show()

# sigmoid함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# sigmoid함수 그래프 그리기
x = np.arrange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1,1)
plt.show()
