# 함수의 활용
# 재귀함수
# 팩토리얼 예시
n! = n * (n-1) * (n-2) * ... * 1 # 식의 반복문도 가능하지만
factorial(n) = n*factorial(n-1) 
factorial(0) = 1
# 위와 같이 표현도 가능함.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# 재귀함수는 함수 호출의 수가 기하급수적으로 많아질 수 있음.
# 그래서 메모화 기능을 사용함.
dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output
# 딕셔너리 안에 있는 것이면 재귀함수를 호출하지 않고 그냥 값 불러옴.

# 리스트 평탄화도 재귀함수로 가능.
def flatten(data):
  output=[]
  for i in data :
    if type(i) == list :
      output += flatten(i)
    else :
      output.append(i)
  return output

flatten([1, 2, [3, [4, 5]], [6, 7]])
# 재귀함수를 헷갈리지 않고 사용하려면, 큰 함수의 구조를 머릿속에 그려두는게 중요.
# 또한, 주석과 함수 이름 등을 잘 이용하면 이해하기 쉬운 코드를 짜는 데에 도움이 됨.
