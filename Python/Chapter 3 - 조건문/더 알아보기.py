# 도전문제
a = input('입력: ')
if "안녕" in a :
  print("안녕하세요.")
elif "몇 시" in a:
  print("지금은 {}시입니다.".format(now.hour))
else :
  print(a)

number = int(input("정수를 입력해주세요: "))
if number%2 ==0 :
  print("{}은 2로 나누어떨어지는 수입니다.".format(number))
else :
  print("{}은 2로 나누어떨어지는 수가 아닙니다.".format(number))
if number%3 ==0 :
  print("{}은 3로 나누어떨어지는 수입니다.".format(number))
else :
  print("{}은 3로 나누어떨어지는 수가 아닙니다.".format(number))
if number%4 ==0 :
  print("{}은 4로 나누어떨어지는 수입니다.".format(number))
else :
  print("{}은 4로 나누어떨어지는 수가 아닙니다.".format(number))
if number%5 ==0 :
  print("{}은 5로 나누어떨어지는 수입니다.".format(number))
else :
  print("{}은 5로 나누어떨어지는 수가 아닙니다.".format(number))

# 사람의 방식 구현
# 3의 배수
number = input("정수를 입력해주세요: ")
counter = 0
for i in range(len(number)) :
  counter += int(number[i])
if counter % 3 == 0 :
  print("3의 배수입니다!")
else : 
  print("3의 배수가 아닙니다.")

# 4의 배수
n = input("정수를 입력해주세요: ")
if int(n[-2:]) % 4 == 0:
  print("4의 배수입니다!")
else : 
  print("4의 배수가 아닙니다.")

# 5의 배수
n = input("정수를 입력해주세요: ")
if int(n[-1:]) == 0 or \
    int(n[-1:]) == 5:
  print("5의 배수입니다!")
else : 
  print("5의 배수가 아닙니다.")

# 6의 배수
n = input("정수를 입력해주세요: ")
for i in range(len(number)) :
  counter += int(number[i])
if int(n) % 2 == 0 and \
    counter % 3 == 0:
  print("6의 배수입니다!")
else : 
  print("6의 배수가 아닙니다.")

# 9의 배수
n = input("정수를 입력해주세요: ")
counter = 0
for i in range(len(number)) :
  counter += int(number[i])
if counter % 9 == 0 :
  print("9의 배수입니다!")
else : 
  print("9의 배수가 아닙니다.")

# 10의 배수
n = input("정수를 입력해주세요: ")
if int(n[-1:]) == 0:
  print("5의 배수입니다!")
else : 
  print("5의 배수가 아닙니다.")
