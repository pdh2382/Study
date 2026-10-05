# 신경망
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
