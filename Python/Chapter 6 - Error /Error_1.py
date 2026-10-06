# 예외 (Error)
# 구문 오류 : 프로그램 실행 전에 발생하는 오류
print("# 프로그램이 시작되었습니다!")
print("# 예외를 강제로 발생시켜볼게요!) # 아예 실행도 안됨.

# 런타임 오류(예외) : 실행 중에 발생하는 오류
print("#프로그램이 시작되었습니다!") # 이 줄까지는 잘 실행됨.
list_a[1]

# 기본 예외 처리
user_input_a = input("정수 입력> ")

if user_input_a.isdigit() :
  number_input_a = int(user_input_a)

  print("원의 반지름: ", number_input_a)
  print("원의 둘레: ", 2 * 3.14 * number_input_a)
  print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
else :
  print("정수를 입력하지 않으셨습니다.")
# 모든 오류 케이스를 전부 분리하기는 어려움.

# try except 구문
try :
  number_input_a = int(input("정수 입력> "))

  print("원의 반지름: ", number_input_a)
  print("원의 둘레: ", 2 * 3.14 * number_input_a)
  print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
except :
  print("무언가 잘못되었습니다.")

# 반복문 적용
list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for i in list_input_a :
  try :
    float(i)
    list_number.append(i)
  except :
    pass # 예외가 발생하면 넘어가버림.

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{} 입니다.".format(list_number))

# try except else 구문
# 예외가 발생할 가능성이 있는 구문만 try에 집어넣어서 시도.
try :
  number_input_a = int(input("정수 입력> "))
except :
  print("무언가 잘못되었습니다.")
else :
  print("원의 반지름: ", number_input_a)
  print("원의 둘레: ", 2 * 3.14 * number_input_a)
  print("원의 넓이: ", 3.14 * number_input_a * number_input_a)

# 시도 가능한건 오직
# try + except
# try + except + else
# try + except + finally
# try + except + else + finally
# try + else

# finally 구문
# while에서 break로 탈출해도, return으로 탈출해도 무조건 실행됨.
print("프로그램이 시작되었습니다.")

while True :
  try :
    print("try 구문이 실행되었습니다.")
    break
    print("try 구문의 break 키워드 뒤입니다.")
  except :
    print("except 구문이 실행되었습니다.")
  finally :
    print("finally 구문이 실행되었습니다.")
  print("while 반복문의 마지막 줄입니다.")

print("프로그램이 종료되었습니다.")

# 파일과같이, 강조를 하는 용도로 사용하기도 함.

