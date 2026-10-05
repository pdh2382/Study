# MNIST 손글씨 파일에 적용시켜보기
import sys, os
sys.path.append(os.path.dirname(__file__), '..')) # 상위 디렉터리에 접근 가능하게 함.
from dataset.mnist import load_mnist # load_mnist()함수 불러오기

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten = True, normalize = False)
    return x_test, t_test

def init_network():
    with open(os.path.dirname(__file__) + "/samle_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network
