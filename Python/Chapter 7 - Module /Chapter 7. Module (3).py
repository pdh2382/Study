# 모듈 만들기
# 그냥 변수, 함수를 잔뜩 넣은 파이썬 파일을 만들어주면 그게 모듈임.
# 밑의 함수를 test_module.py로 저장한다고 하면
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# 불러와서 다음과 같이 사용 가능.
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# __name__ == "__main__"
# 모듈 파일에서 __name__은 그 모듈의 이름
# 엔트리 포인트 파일에서 __name__은 __main__임.
# 이를 이용하면 그 파일을 바로 실행시킨 것인지(엔트리 포인트인지)
# 아니면 그 파일을 모듈로서 불러내서 실행시킨 것인지 구분이 가능함.
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

if __name__ == "__main__" : # 현재 파일이 엔트리 포인트일때만 실행
print("get_circumference(10) : ", get_circumference)
print("get_circle_area(10) : ", get_circle_area)

# 패키지 : 모듈이 모여서 구조를 이루면 패키지
# 패키지 만들기
# test_package 라는 폴더과 main.py(엔트리 포인트), 폴더 안에 module_a, module_b가 있다고 할 때, 

# module_a.py의 내용
variable_a = "a 모듈의 변수"

# module_b.py의 내용
variable_b = "b 모듈의 변수"

# 패키지 내부의 모듈을 불러옴(main.py에서 실행)
import test_package.module_a as a
import test_package.module_b as b

print(a.variable_a)
print(b.variable_b)

# 패키지 내에서 어떤 처리를 수행하거나 내부의 모듈들을 한번에 불러와야 할 때는
# __init__.py 파일을 만들어서 사용함.
# 아까의 test_package 폴더 안에 __init__.py 파일을 만들면
__all__ = ["module_a", "module_b"]
print("test_package를 읽어 들였습니다.")

from test_package import *
print(module_a.variable_a)
print(module_b.variable_b)
