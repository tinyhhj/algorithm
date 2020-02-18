# solution
# input : 압축된 string
# output: 거꾸로 뒤집은 압축된 string

def solution(string):
    # 기저조건
    # 하나의 색인경우
    # w,b인경우
    if(string[0] != 'x'):
        return string[0]

    # x로 시작하는 경우에는 어떻게 나눌것인가?
    first = solution(string[1:])
    second = solution(string[1+len(first):])
    third = solution(string[1+len(first)+ len(second):])
    fourth = solution(string[1+len(first)+len(second) + len(third):])
    return 'x'+third + fourth + first + second


if __name__ == '__main__':
    tc = input()
    for i in range(int(tc)):
        string = input()
        print(solution(string))