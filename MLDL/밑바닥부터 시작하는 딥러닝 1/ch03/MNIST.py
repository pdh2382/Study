# MNIST 손글씨 파일에 적용시켜보기
import sys, os
sys.path.append(os.path.dirname(__file__), '..')) # 상위 디렉터리에 접근 가능하게 함.
from dataset.mnist import load_mnist # load_mnist()함수 불러오기
from activation_function import sigmoid

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten = True, normalize = False)
    return x_test, t_test

def init_network():
    with open(os.path.dirname(__file__) + "/samle_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3'] # 튜플을 사용한 것!
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(x, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(x, W3) + b3
    z3 = sigmoid(a3)

    return y
