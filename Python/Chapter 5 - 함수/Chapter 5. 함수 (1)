#함수 선언
def print_n_times(value, n) :
  for i in range(n) :
    print(value)

print_n_times("안녕하세요", 5)

# 가변 매개변수 : 개수가 변할 수 있는 매개변수.
# 가변 매개변수는 제일 뒤에 와야 함.
def print_n_times(n, *value):
  for i in range(n) :
    for values in value :
      print(values)
    print()

print_n_times(3, "안녕하세요", "저는", "파이썬 공부중입니다.")

#함수마다 고유의 매개변수가 있음.
# 예를 들어, print함수의 기본 형태는 다음과 같음.
# print(value, sep=' ', end='\n', file=sys.stdout, flush=False)
# 여기서 매개변수=값 형태로 이미 정해진걸 "기본 매개변수"라고 함.
# 이 경우, sep과 end가 기본 매개변수로서 이미 들어가 있는 것이다.
def prin_n_times(n=2, *values) : # 기본 매개변수(n)와 가변 매개변수(values)를 함께 쓰는 경우
  for i in range(n) :
    for value in values :
      print(value)

print_n_times("안녕하세요", "저는", "박대현입니다.") #n자리에 "안녕하세요"가 들어가 오류 발생.

# 따라서 이런 경우에는 직접 그 매개변수를 명시하는, "키워드 매개변수"를 사용함.
def print_n_times(*values, n=2) :
  for i in range(n) :
    for value in values :
      print(value)

print_n_times("안녕하세요", "저는", "박대현입니다.", n=5) # 이름을 직접 지정해서 써주는 것.
# 따라서 함수 제작 시 기본 매개변수로 값을 입력하면 비필수,
# 비워두면 필수로 지정해서 입력해주면 됨.

# return : 함수가 끝나는 위치
def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")
# A 위치입니다. 까지만 출력됨.

# return + 값
def mul(*values):
  output = 1
  for i in values:
    output*=int(i)
  return output # output을 출력해줌.

print(mul(5,7,9,10))

# 아무것도 없이 return하면 None 출력.

#함수 내부에서 외부의 변수를 참조하지 못함.
# global을 써줘야 가능.
count = 0
def fibonacci(n):
  counter += 1
  if n == 1 :
    return 1
  if n == 2 :
    return 1
  else : return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
