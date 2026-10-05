# 불리언, 논리 연산자는 아니까 pass.
# 조건문에 불리언이 아닌 값이 오게 되면 자동으로 변환함.
# 이때, None, 0, 0.0, 빈 컨테이너는 False로 변환
# 나머지는 True로 변환함.
# 따라서, 이렇게 짝수 구분 식을 작성하면 안됨.
num = input()
last_num = num[-1]
if last_num == 0 or 2 or 4 or 6 or 8 :
  print("짝수입니다.")
# 0을 제외한 숫자들이 다 True가 되어서 전부 True판정을 해버림.

# 날짜 / 시간 이용하기
import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.year, "월")
print(now.year, "일")
print(now.year, "시")
print(now.year, "분")
print(now.year, "초")

# 또한, else와 elif로 추가 조건을 걸 수도 있음.
# 간단한 예제로 총정리.
a = input('입력: ')
if "안녕" in a :
  print("안녕하세요.")
elif "몇 시" in a: # elif로 추가 조건
  print("지금은 {}시입니다.".format(now.hour)) # format함수 활용
else :
  print(a)

# 조건문 구현시 골격만 잡아두고 넘어가는 경우도 있음.
# 이 경우, IndentationError를 막기 위해 pass를 채워놓는 편.
if 2 > 0 :
  pass
else :
  pass

#혹은 raise NotImplementedError를 넣어 오류를 발생시키기도 함.
if 2 > 0 :
  raise NotImplementedError
else :
  raise NotImplementedError
