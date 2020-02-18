'''
# perceptron
# input : 여러 신호( 전류나 강물처럼 흐름이 있는..)
# output: 1 or 0 (1: 신호가 흐른다, 0 : 흐르지 않는다)
# 임계값(theta): 입력신호마다(x1,x2,..xn) 가중치(w1,w2,..wn)을 곱해 임계치를 넘을경우 출력신호(1)을 내보낸다.
# 가중치는 각 신호가 결과에 주는 영향력을 나타내는 요소( 즉 가중치가 클수록 중요한 신호임을 뜻합니다.)

x1*w1 + x2*w2 + .. xn*wn <= theta (return 0)
x1*w1 + x2*w2 + .. xn*wn > theta (return 1)


논리회로 and 게이트
x1 x2 y
0  0  0
0  1  0
1  0  0
1  1  1

퍼셉트론을 이용해 논리 and게이트를 만들 때 w1,w2(각 입력의 가중치)와 임계값(theta)를 정해야 합니다.
  w1  w2  theta
(0.5,0.5,0.7)
(0.5,0.5,0.8)
...
and 게이트의 조건을 만족하는 매개변수 조합은 무수히 많습니다.

nand 게이트
x1 x2 y
0  0  1
0  1  1
1  0  1
1  1  0
and 게이트 조건을 만족하는 매개변수들의 부호를 변경하면 모두 만족합니다.

위와 같은 문제일 경우 문제를 해결하는 방식을 생각해보면
and 게이트의 진리표라는 '학습데이터'를 보면서 알맞은 매개변수의 값을 찾습니다.
기계학습 문제는 이 매개변수의 값을 컴퓨터가 자동으로 찾도록 하는것을 말합니다.
학습이란 적절한 매개변수 값을 정하는 행위이며, 사람은 퍼셉트론의 구조(모델)을 고민하고
컴퓨터에 학습할 데이터를 주는 역할을 합니다.

and , nand ,or 게이트 모두 같은 구조의 퍼셉트론이 역할을 수행할 수 있고, 각 게이트마다 다른점은 매개변수(가중치와 임계값)일 뿐입니다.
즉 매개변수에 따라서 다양하게 역할을 수행하도록 퍼셉트론을 변경할 수 있습니다.
'''

# and gate

def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    if x1*w1+x2*w2 <= theta:
        return 0
    else:
        return 1
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

'''
theta = -b
b를 편향이라고 부르며
x1*w1 + x2*w2 + .. xn*wn <= -b (return 0)
x1*w1 + x2*w2 + .. xn*wn > -b (return 1)
위 수식을
b +  x1*w1 + x2*w2 + .. xn*wn <= 0 (return 0)
b +  x1*w1 + x2*w2 + .. xn*wn > 0 (return 1)
로 변경이 가능합니다.

편향과 가중치와 차이점에 주의합니다
가중치: 각 입력신호가 결과에 주는 영향력(중요도)를 조절하는 매개변수
편향: 뉴런이 얼마나 쉽게 활성화 하느냐 조절하는 매개변수
'''
import numpy as np
x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7

print(np.sum(w*x)+ b)

def And(x1,x2):
    w = np.array([0.5,0.5])
    b = -0.7
    x = np.array([x1,x2])
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def Or(x1,x2):
    w = np.array([0.5,0.5])
    b = -0.1
    x = np.array([x1,x2])
    tmp = np.sum(w*x)+ b
    if tmp <= 0:
        return 0
    else:
        return 1
def Nand(x1,x2):
    if And(x1,x2) <= 0:
        return 1
    else:
        return 0



'''
퍼셉트론의 한계 
직선으로만 출력이 표현가능하기 때문에 xor같은 비선형 데이터를 표현할 수 없습니다.
퍼셉트론을 여러 층으로 쌓으면 xor와 같은 비선형 데이터를 표현할 수 있습니다.

'''
def Xor(x1,x2):
    s1 = Nand(x1,x2)
    s2 = Or(x1,x2)
    return And(s1,s2)

print(Xor(0,0))
print(Xor(0,1))
print(Xor(1,0))
print(Xor(1,1))


