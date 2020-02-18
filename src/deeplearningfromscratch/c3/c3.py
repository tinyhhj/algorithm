'''
신경망
데이터로부터 가중치 매개변수의 적절한 값을 자동으로 학습하는 능력이 신경망의 중요한 성질입니다.
신경망의 구조
0.입력층
1.은닉층
2.출력층

퍼셉트론의 편향은 입력이 1이고 가중치가 b일 경우의 가중치로 변경이 가능합니다.
a = b(=w0)*x0 +w1*x1 + .. + wn*xn 으로 표현이 가능합니다.
y = h(a)
여기서 h(a)는 활성화 함수라고 하는데 입력의 총합(a)이 활성화(y)를 일으키는지 정하는 역할을 합니다.

퍼셉트론의 경우에 활성화 함수로 계단 함수를 사용하고 있으나 신경망으로 세계에서는 활성화 함수로 다른 함수를 사용하고 있습니다.

시그모이드 함수

'''

# 계단 함수
import numpy as np
import matplotlib.pylab as plt

def step_func(x1):
    return np.array( x1 >0, dtype=np.int)

x = np.arange(-5., 5.,0.1)
y = step_func(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1) # 범위
plt.show()

# sigmoid

def sigmoid(x):
    # broadcast 이용
    # scalar 와 np.array 연산 시 해당 크기만큼 scalar값이 확장되어 연산을 수행합니다.
    return 1 / (1 + np.exp(-x))

xx = np.arange(-5.,5.,0.1)
yy = sigmoid(xx)

plt.plot(xx,yy)
plt.ylim(-0.1,1.1)
plt.show()

# ReLU(Rectified Linear Unit)

def relu(x):
    return np.maximum(0,x)

# 다차원 배열
A = np.array([[1,2],[3,4]])
print(A)
print(np.ndim(A)) # 차원
print(A.shape) # 차원의 크기

B = np.array([[4,5],[7,8]])
print(np.dot(A,B)) # 행렬의 곱 np.dot

C = np.array([[[1],[3]],[[1],[3]],[[1],[3]]])
print(C.shape)

# 신경망 행렬 곱
# x * w = y

X = [1,2]
W = [[1,2,3],[4,5,6]]
Y = np.dot(X,W)
print(Y)

# 핵심은 신경망에서의 계산을 행렬 계산으로 정리할 수 있다는 것입니다.
# 0층 입력층
# 1층 은닉층
# 2층 은닉층
# 3층 출력층
X = np.array([0.5,1])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])
print(W1.shape)
print(X.shape)
print(B1.shape)

# 0->1층
A1 = np.dot(X,W1)+B1
Z1 = sigmoid(A1)
print(A1)
print(Z1)

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

# 1->2층
A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)
print(A2)
print(Z2)

# 2->3층
# 나머지 구현은 같으나, 활성화 함수만 다릅니다.
def identify_func(x):
    return x

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])
A3 = np.dot(Z2,W3)+B3
Z3 = identify_func(A3)
print(A3)
print(Z3)

# 중요: 출력층의 활성화 함수는 문제의 성질에 다르게 정합니다
# 회귀: 항등함수
# 분류: 시그모이드
# 다중분류: 소프트 맥스

# 소프트 맥스

a = np.array([0.3, 0.5, 0.7])
exp_a = np.exp(a)
sum_exp_a = np.sum(exp_a)
y = exp_a / sum_exp_a
print(y)

# softmax의 결과값의 경우 항상 출력 총합이 1 이므로 출력값을 '확률'로 해석할 수 있습니다.
def softmax(x):
    # exp는 오버플로우가 발생할 수 있으므로 max값을 빼줍니다.
    max = np.max(x)
    exp_x = np.exp(x-max)
    sum = np.sum(exp_x)
    # print(max, exp_x, sum)
    return exp_x / sum

# 기계학습을 학습과 추론 2단계로 나뉩니다
# 학습: 데이터를 사용해서 '가중치 매개변수'를 학습합니다.
# 추론: 앞에서 학습한 '가중치 매개변수'를 사용해서 입력데이터를 분류합니다.
import sys, os
sys.path.append(os.pardir)
from download_mnist import load_mnist

(x_train, t_train), (x_test,t_test) = load_mnist(flatten=True, normalize=True)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

# 출력층 뉴런 10개 -> 다중 분류 0-9(10개
# 은닉 1층 50개 뉴런 / 2층 100 개 뉴런
# 50 과 100 은 임의의 값
import pickle

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True)
    return x_test,t_test

def init_network():
    with open("sample_weight.pkl",'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1,W2,W3 = network['W1'], network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    a1 = np.dot(x,W1)+b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2)+b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3)+b3
    y = softmax(a3)

    print('a1.shape', a1.shape)
    print('z1.shape', z1.shape)
    print('a2.shape', a2.shape)
    print('z2.shape', z2.shape)
    print('a3.shape', a3.shape)
    print('y.shape', y.shape)
    return y

x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0
for i in range(0,len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    #y = predict(network, x[i])
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt+= np.sum(p == t[i:i+batch_size])

print("Accuracy: " + str(float(accuracy_cnt) / len(x)))







