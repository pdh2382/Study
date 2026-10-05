# 함수 고급
# 튜플
# 괄호로 묶어서 요소를 정의하는 자료형.
tuple_test = (10, 20, 30)

# 그런데, 괄호 없이도 선언 가능함.
tuple_test = 10, 20, 30

# 변수 변경도 굉장히 편함.

# 매개변수로 함수 전달
def call_10_times(func):
  for i in range(10):
    func()

def print_hello():
  print("hello")

call_10_times(print_hello) # print_hello같은 함수를 '콜백 함수'라고 부름.

# map() 함수
list_a = [1, 2, 3, 4, 5]
output_a = map(power, list_a)

# filter()함수
output_b = filter(under_3, list_a)
# power, under_3은 실제로 돌릴 예정이라면 따로 정의해야함.

# 람다
# 간단한 함수를 쉽게 선언하게 해주는 기법.
# lambda 매개변수: 리턴값
power = lambda x: x*x
under_3 = lambda x: x<3

# 파일처리
# 파일 열고 닫기
# 파일 객체 = open(문자열:파일경로, 문자열: 읽기 모드)
file = open("basic.txt", "w")
# a : 이어쓰기 모드(append)
# r : 읽기 모드(read)

# 닫을 때는 close()
file.close()

# 파일은 항상 닫아야 하는데, 실수로 안 닫을 수도 있음.
# 그럼 with 키워드 사용.
with open("basic.txt", "w") as file:
    file.write("Hello Python!")
