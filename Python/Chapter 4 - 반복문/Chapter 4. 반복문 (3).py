# 범위 자료형과 while문
# 범위
range(A) # 0부터 A-1까지 정수.
range(A, B) # A부터 B-1까지 정수.
range(A, B, C) # A부터 B-1까지, C 간격으로.

# range 안에는 무조건 정수를 집어넣어야 함.
n = 10
range(0, n/2) # TypeError 발생.

# for문과 같이 연결
for i in range(4):
    print("{}번째 반복입니다.".format(i))

# 역반복문 : for문 반대로 하기
for i in range(4, 0-1, -1): # 그냥 -1로 써도 되는데, 그냥 강조용으로 0-1이라 씀.
    print("현재 반복 변수: {}".format(i))

# reversed()함수 이용하기
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))

# while문
# while 조건문 : 조건문이 참인 동안 실행을 반복함.
i = 0
whlie i<10 :
    print("{}번째 반복입니다.".format(i))
    i += 1
# 조건에 따라서 무한반복이 되어버릴 수도 있기 때문에, 조건을 잘 설정해야 함.

# list와 while
# 특정 값을 전부 제거하는 코드도 가능.
list_a = [1, 2, 1, 2]
value = 2

while value in list_test:
    list_a.remove(value)

# enumerate() 함수
list_b = [a, b, c]
enumerate(list_a) # <enumerate object at ~~~>와 같이, 이터레이터로 나옴.
lsit(enumerate(list_a)) # list로 강제 변환

for i, value in enumerate(list_b):
    print("{}번째 요소는 {]입니다.".format(i,value))

# items()함수
# (키, 값)형태로 추출해줌.
for key, element in dictionary :
    print("dictionary[{]] = {}".format(key, element))

# 리스트 내포
# 리스트 안에 반복문을 넣어서 바로 생성해내는 것.
array = [i*i for i in range(0, 20, 2)]
