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

# Relu 함수
def relu(x):
  return np.maximum(0,x)

# 3층 신경망 만들어보기
# 1층의 가중치와 전달 구현
# 위 그림과 같이, xi노드에서 aj노드로 가는 신호의 가중치를 (i,j)성분으로 가지는 W를 가중치 행렬이라고 한다.
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X, W1) + B1 # 입력값 행렬 x 가중치 행렬 + 편향으로 나온 은닉층1의 값이 담긴 행렬

# 은닉층1의 값에 활성화함수 부여.
Z1 = sigmoid(A1)
print(Z1)

#위의 원리대로, 3층 신경망을 전부 구현할 수 있음.
def identity_function(x):
  return x

def init_network():
  network = {}
  network['W1'] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
  network['b1'] = np.array([0.1, 0.2, 0.3])
  network['W2'] = np.array([[0.1, 0.4],[0.2, 0.5],[0.3, 0.6]])
  network['b2'] = np.array([0.1, 0.2])
  network['W3'] = np.array([[0.1, 0.3],[0.2, 0.4]])
  network['b3'] = np.array([0.1, 0.2])

  return network

def forward(network, x): # 순전파여서 forward.
  W1, W2, W3 = network['W1'], network['W2'], network['W3']
  b1, b2, b3 = network['b1'], network['b2'], network['b3']

  a1 = np.dot(x, W1) + b1
  z1 = sigmoid(a1)
  a2 = np.dot(z1, W2) + b2
  z2 = sigmoid(a2)
  a3 = np.dot(z2, W3) + b3
  y = identity_function(a3)

  return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)

# 소프트맥스 함수 구현
def softmax(a):
  c = np.max(a) # 지수함수 특성상 기하급수적으로 커지는 것을 막기 위한 장치.
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a

  return y

  # 소프트맥스의 출력값은 확률로도 볼 수 있음.
