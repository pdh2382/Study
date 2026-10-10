# 딕셔너리에서 특정 값을 기준으로 최대/최소를 구하고 싶을 경우
# min(), max()함수에 key를 입력해주면 됨.
books = [{
    "제목": "혼자 공부하는 파이썬"
    "가격": 18000
},{
    "제목": "혼자 공부하는 머신러닝"
    "가격": 26000
},{
    "제목": "혼자 공부하는 데이터분석"
    "가격": 24000
}]

print(min(books, key = lambda book: book["가격"]))
# 람다함수까지 같이 활용

# 기본 자료형과 객체 자료형의 저장 차이
# 기본 자료형은 스택에 직접 저장됨.
a = 5
b = 10

# 함수를 선언하면, 그 함수만의 함수 스택이 생김.
def primitive_change(b):
  b = 20

a = 10
print(a)
primitive_change(a) # 함수 스택에 따로 b라는 인덱스 + 20이라는 값이 생김.
print(a) # 똑같이 10이 나옴.(전역 스택에서 불러오기에.)

# 리스트의 경우에는 힙에 본 데이터를, 스택에 주소를 저장함.
# 그래서 append같은 함수를 쓰면 힙의 데이터가 변경돼서 함수 스택이든 전역 스택이든 다 영향미침.

# 도전문제 - 하노이 탑
count = 0
def hanoii(n, A, B, C):
  global count
  if n == 1:
    print("{} -> {}".format(A, B))
    count +=1
  if n >= 2:
    for i in range(n):
      hanoii(n-1, A, C, B)
      print("{} -> {}".format(A, B))
      count += 1
      hanoii(n-1, C, B, A)
  return count

n = int(input("원판의 개수를 입력해주세요:"))
hanoii(n, 'A탑', 'B탑', 'C탑')

def hanoii_count(n):
  print("이동 횟수는 {}회입니다.".format(2**n -1))

n = int(input("원판의 개수를 입력해주세요:"))
hanoii_count(n)
