# 클래스의 추가 구문
# isinstance()구문 : 어떤 클래스의 인스턴스인지
class Student:
  def __init__(self):
    pass

student = Student()

print("isinstance(student, Student):",isinstance(student, Student)) 
print("type(student):",type(student))
# 둘다 인스턴스의 클래스를 확인해주지만, type은 상속관계를 파악하지 못함.

# 활용 예시
class Student:
  def study(self):
    print("공부를 합니다.")

class Teacher:
  def teach(self):
    print("학생들을 가르칩니다.")

classroom = [Student(), Teacher(), Student(), Student(), Teacher(), Student()]

for person in classroom:
  if isinstance(person, Student):
    person.study()
  elif isinstance(person, Teacher):
    person.teach()

# 파이썬에서는 클래스를 만들 때 자체적으로 제공해주는 메소드가 있음.
# __str__을 정의하면 str()함수를 불러올 때 자동으로 __str__이 호출됨.
class Student:
  def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science

  def get_sum(self):
    return self.korean + self.math +\
        self.english + self.science

  def get_avg(self) :
    return self.get_sum() / 4

  def __str__(self): # 이전 클래스(1)에서의 to_srting()과 동일한 역할을 함.
      return "{}\t{}\t{}".format(
          self.name,\
          self.get_sum(),\
          self.get_avg())
      
  
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤인성", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep = "\t")
for student in students :
  print(str(student))

# 이 외에도 eq, ne, gt, ge 등의 메소드를 제공함.
class Student:
  # 생략
  def __eq__(self, value):
    return self.get_sum() == value.get_sum()
  def __ne__(self, value):
    return self.get_sum() != value.get_sum()
  def __gt__(self, value):
    return self.get_sum() > value.get_sum()
  def __ge__(self, value):
    return self.get_sum() == value.get_sum()
  #생략
student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a < student_b = ", student_a < student_b)

# 이를 6장의 예외 처리와 함께 사용할 수 있음
# 클래스와 다른 타입을 비교하면 TypeError가 발생하게.
class Student:
  #생략
  def __eq__(self, value):
    if not isinstance(value, student): 
      raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
    return self.get_sum() == value.get_sum()
  #생략

student_a = Student("윤인성", 87, 98, 88, 95)
student_a == 10

# 클래스 변수
# 이전까지는 클래스 안에는 함수만 정의하고, 그로인해 인스턴스가 속성을 지니게 했으나,
# 클래스 자체가 속성을 가질 수도 있음
class Student:
  count = 0 # 클래스 변수

  def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science

    Student.count += 1
    print("{}번째 학생이 생성되었습니다.".format(Student.count))

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤인성", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print()
print("현재 생성된 학생 수는 총 {}명입니다.".format(Student.count)) # 클래스 변수는 클래스.변수명으로 호출함.

# 클래스 함수
class Student:
  count = 0
  students = []

  @classmethod
  def print(cls):
    print("---- 학생 목록 -----")
    print("이름\t총점\t평균")
    for student in cls.students:
      print(str(student))
    print("------ ------ ------")
  
  # 인스턴스 함수
  def __init__(self, name, korean, math, english, science): 
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science
    Student.count += 1
    Student.students.append(self) # 클래스 변수에 추가

  # 생략

Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤인성", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)

Student.print()
