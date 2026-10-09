# 전개 연산자
# 리스트 앞에 * 을 붙이면 리스트 안의 요소를 전개시켜주는 역할을 함.
# 주로 함수의 매개변수 위치에 사용하거나 리스트 내부에 사용함.

# 리스트 내부
a = [1, 2, 3, 4]
b = [*a, *a]

# 비파괴적으로 구현할 때에도 도움이 됨.
a.append(5) # a가 [1, 2, 3, 4, 5]로 변경됨 (파괴적)

b = [1, 2, 3, 4]
c = [*b, 5] # b의 내용에 변경점이 없음. (비파괴적)

# 함수 매개변수 위치
a = [1, 2, 3, 4]
print(*a) # print(a[0], a[1], a[2], a[3])과 같음.

# 반복문 예제 - 1부터 더하기
limit = 10000
i = 1
sum_value = 0
while sum_value < limit :
  sum_value += i
  i += 1
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

# 반복문 예제 - 1부터 100까지 숫자 곱하기
max_value = 0
a = 0
b = 0

for i in range(1, 100 + 1):
  j = 100 - i

  if i*j > max_value:
    a = i
    b = j
    max_value = i*j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

# 구문 내에 여러 줄 문자열을 사용했을 때 문제점
number = int(input("정수 입력> "))

if number % 2 == 0:
  print('''\
  입력한 문자열은 {}입니다. 
  {}는(은) 짝수입니다.'''.format(number, number))
else :
  print('''\
  입력한 문자열은 {}입니다. 
  {}는(은) 홀수입니다.'''.format(number, number)) # 예상치 못한 들여쓰기가 들어감.

# 해결(1) : 괄호로 문자열 연결하기
test = (
  "이렇게 입력해도"
  "하나의 문자열로 나옴."
)

print(test)

# 응용
number = int(input("정수 입력> "))

if number % 2 == 0:
  print((
    "입력한 문자열은 {]입니다.\n"
    "{}는(은) 짝수입니다."
  ).format(number, number))
else :
  print((
    "입력한 문자열은 {]입니다.\n"
    "{}는(은) 홀수입니다."
  ).format(number, number))

# 이터레이터
# 내부에 있는 요소를 차례차례 꺼낼 수 있는 객체
numebers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print(r_num) # <list_reverseiterator object at 주소> 형태로 나옴.
print(next(r_num)) # numbers를 뒤집은 게 하나씩 나옴.
# 실제 리스트를 복제하고 뒤집는 것보다 
# 기존의 리스트를 이용해서 주소개념으로 꺼내는게 낫기 때문.

# 예제 - 2진수 변환, 0 개수 1개인것 찾기
output = [num 
          for num in range(1,100) 
          if len("{:b}".format(num)) - 1 == sum(map(int,[*"{:b}".format(num)]))

# 도전문제 - 숫자의 종류
dictionary = {}
list_a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
for i in list_a:
  if i in dictionary:
    dictionary[i] += 1
  else:
    dictionary[i] = 1

print((
    "{}에서\n"
    "사용된 숫자의 종류는 {}입니다.\n"
    "참고: {}"
).format(list_a, len(dictionary), dictionary))

# 도전문제 - 염기의 개수
list_input_a = input("염기 서열을 입력해주세요: ")
dictionary_a = {
  'a' : 0,
  't' : 0,
  'g' : 0,
  'c' : 0
}

for i in list_input_a:
  dictionary_a[i] += 1

for key, value in dictionary_a.items():
  print("{}의 개수: {}".format(key, value))

# 도전문제 - 리스트 평탄화
list_b = [1, 2, [3, 4], 5, [6, 7], [[8, 9], 10]]
def list_flatten(x):
  output = []
  for i in x:
    if type(i) == list:
      output.extend(list_flatten(i))
    else: 
      output.append(i)
  return output
print(list_flatten(list_b))
