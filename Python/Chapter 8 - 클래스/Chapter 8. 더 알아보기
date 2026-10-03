# 가비지 컬렉터
# 앞으로 쓰이지 않을 것 같은 데이터는 삭제함.
# 대표적으로 변수에 저장되는지 여부.
class Test:
def __init__(self, name):
    self.name = name
    print("{}가 생성되었습니다.".format(self.name))
def __del__(self):
    print("{}가 파괴되었습니다.".format(self.name))

Test("A")
Test("B")
Test("C")
# 결과, 생성되는 대로 바로 파괴됨.
# 변수에 저장하지 않았기 때문.
a = Test("A")
b = Test("B")
c = Test("C")
# 이러면 프로그램이 종료될 때까지는 파괴하지 않음.

# 프라이빗 변수
# 클래스 내부에서만 사용(변경)할 수 있게 하는 변수.
import math

class Circle :
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)
print(circle.get_circumference())
print(circle.get_area())
circle.__radius = -2 # AttributeError 발생

# 게터와 세터
    def get_radius(self):
      return self.__radius
    def set_radius(self, value):
      self.__radius = value
# 위와 같은 코드로 간접적으로 __radius에 접근해 변경도 가능함.

def set_radius(self, value):
    if value <= 0:
        raise TypeError("길이는 양의 숫자여야 합니다.")
    self.__radius = value
# 위와 같은 코드로 예외처리까지 적용할 수도 있음.
# 그리고 이 모든걸 데코레이터를 활용해 간략히 표현도 가능.
import math

class Circle:
    # ...생략...
    # 게터와 세터 선언
    @property
    def radius(self):
        return self.radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

print("#데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2 # 데코레이터로 더 편하게 변경가능.
print("변경된 원의 반지름: ", circle.radius)
print()

# 상속
# 다른 누군가가 만들어둔 기본 형태에 내가 원하는 것만 추가하는 것.
# 기반이 되는 것을 '부모', 부모로 만든 것을 '자식'이라 함.
class Parent:
  def __init__(self):
    self.value = "테스트"
    print("Parent 클래스의 __init__ 메소드가 호출되었습니다.")
  def test(self):
    print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
  def __init__(self):
    super().__init__() # 부모의 __init__함수를 호출
    print("CHild 클래스의 __init__메소드가 호출되었습니다.")

child = Child()
child.test() # 이 시점에서 Parent와 Child의 __init__은 모두 호출됨.
print(child.value)
