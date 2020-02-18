# 학습: 데이터로부터 가중치 매개변수의 최적값을 자동으로 획득하는 것을 말합니다.
# 학습 시에는 훈련 데이터와 테스트 데이터를 나누는데, 훈련데이터로 학습된 모델의 범용성을 테스트하기 위함입니다.
# 신경망 학습에서는 최적의 매개변수를 찾기위한 지표로 '손실 함수'를 사용하는데, 손실 함수란 성능의 나쁨을 나타내는 지표입니다.
# 즉 학습모델의 성능이 좋다는것은 성능의 나쁨(손실함수)을 최소로 하는것과 일맥상통합니다.

import numpy as np

def sum_squares_error(y,t):
    return 0.5 * np.sum((y-t)**2)

# 2가 확률이 0.6으로 제일 높습니다.
t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

print(sum_squares_error(np.array(y),np.array(t)))
# 7이 확률이 0.6으로 제일 높습니다.
t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]

# 손실함수의 결괏값이 낮을수록 정답에 가깝다고 예상할 수 있습니다.
print(sum_squares_error(np.array(y),np.array(t)))

# 또다른 손실할수로 '교차 엔트로피'함수를 많이 사용합니다.

def cross_entropy_error(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    delta = 1e-7
    # np.log(0)일 경우 -inf로 이후 연산이 불가능하므로 아주 작은 값을 더해줍니다.
    return -np.sum(t*np.log(y+delta)) / batch_size

# 2가 확률이 0.6으로 제일 높습니다.
t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
print(cross_entropy_error(np.array(y),np.array(t)))
# 7이 확률이 0.6으로 제일 높습니다.
t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
print(cross_entropy_error(np.array(y),np.array(t)))

import sys, os
sys.path.append(os.pardir)

from download_mnist import load_mnist

(x_train, t_train), (x_test,t_test) = load_mnist(normalize= True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

# 전체 데이터로 학습을 시키기에 너무 시간이 오래 걸릴때, 부분데이터만 추출하여 학습을 시킬수 있습니다.
# 이때 부분 데이터를 미니 배치라고 하며, 부분 학습을 미니배치 학습이라고 지칭합니다.
# 미니배치를 추출할때 랜덤 함수로 np.random.choice함수를 사용할 수 있습니다.

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(batch_mask)
print(x_batch[0])
print(t_batch.shape)

# 손실 함수를 설정하는 이유?
# 정확도라는 지표를 사용하는 경우에 100개중 10개 일경우 10%의 수치를 보입니다.
# 반복된 학습을 통해서 가중치 매개변수를 성능이 더 좋게끔 수정하려면 작은 매개변수의 변화에도 지표의 변화가 필요합니다.
# 하지만 정확도의 경우에 작은 변화에 지표의 변화가 일어나지 않거나, 10 11 12% 라는 연속적이지 않은 값으로 변경되기 때문에,
# 아주 작은 변화에 따른 성능의 차이를 확인할 수 없습니다. 반면 손실 함수의 경우에 활성화 함수로 시그모이드 함수를 채택하는 것처럼
# 아주 작은 변화에도 손실함수의 값에는 10.123123 이라는 연속적인 값으로 현재 성능을 제대로 판단할 수 있습니다.
# 따라서 조금씩 입력값을 변경시켜가면서 손실함수를 최솟값으로 만드는 매개변수를 찾는 일로 학습이 가능한 이유입니다.

# 수치 미분 (중심 차분, 중앙 차분)
def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

f = lambda x: x**2+x

# 2x+1 =5
print(numerical_diff(f,2))
# 2x+1 =7
print(numerical_diff(f,3))

def function_2d(f,x):
    return np.sum(x**2)




