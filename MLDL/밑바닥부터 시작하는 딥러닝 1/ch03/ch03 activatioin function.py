# 자주 쓰는 활성화함수 
# 계단함수
def step_function(x):
  y = x>0
  return y.astype(int)

#시그모이드 함수
def sigmoid(x):
  return 1 / (1+ np.exp(-x))

# Relu 함수
def relu(x):
  return np.maximum(0,x)

# 자기함수
def identity_function(x):
  return x

# 소프트맥스 함수
def softmax(a):
  c = np.max(a) # 지수함수 특성상 기하급수적으로 커지는 것을 막기 위한 장치.
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y
