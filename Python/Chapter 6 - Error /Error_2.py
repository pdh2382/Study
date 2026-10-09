# 예외 객체
# 예외와 관련된 정보를 품고 있는 객체
# Exception : 모든 종류의 예외를 포함하는 객체.
try :
  number_input_a = int(input("정수 입력> "))
  print("원의 반지름: ", number_input_a)
  print("원의 둘레: ", 2 * 3.14 * number_input_a)
  print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
except Exception as exception :
  print("type(exception) : ", type(exception))
  print("exception : ", exception)

#조건문 적용
lsit_number = [52, 273, 32, 72, 100]

try:
  number_input = int(input("정수 입력>"))

  print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception : # 해당 예외가 뜨면 실행할 코드
  print("정수를 입력해주세요!")
  print(type(exception), exception)
except IndexError as exception :
  print("리스트의 인덱스를 벗어났어요!")
  print(type(exception), exception)

# 이 또한 마찬가지로, 모든 예외를 조건에 포함시키기 어렵다는 한계를 가짐.
#모든 예외 처리
lsit_number = [52, 273, 32, 72, 100]

try:
  number_input = int(input("정수 입력>"))

  print("{}번째 요소: {}".format(number_input, list_number[number_input]))
  예외.발생해주세요() # 예외 라는 이름의 변수가 없어서 NameError발생.
except ValueError as exception :
  print("정수를 입력해주세요!")
  print(type(exception), exception)
except IndexError as exception :
  print("리스트의 인덱스를 벗어났어요!")
  print(type(exception), exception)
except Exception as exception : # 모든 예외 포함.
  print("예상치 못한 오류가 발생했습니다.")
  print(type(exception), exception)

# 예외 발생시키기 : raise
number = input("정수 입력> ")
number = int(number)

if number >0 :
  raise NotImplementedError
else :
  raise NotImplementedError
