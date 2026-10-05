# 객체 지향 프로그래밍 : 객체를 우선으로 생각하여 프로그래밍한다.
# 객체 : 속성과 메소드를 갖는 것.

# 여태까지의 방식
students = [
    { "name": "윤인성", "korean" : 87, "math": 98, "english":88, "science": 95},
    { "name": "연하진", "korean" : 92, "math": 98, "english":96, "science": 98},
    { "name": "구지연", "korean" : 76, "math": 96, "english":94, "science": 90},
    { "name": "나선주", "korean" : 98, "math": 92, "english":96, "science": 92},
    { "name": "윤아린", "korean" : 95, "math": 98, "english":98, "science": 98},
    { "name": "윤명월", "korean" : 64, "math": 88, "english":92, "science": 92}
]

print(students)

# 객체를 만드는 함수 
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
        }

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤인성", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep = '\t')
for student in students:
  score_sum = student["korean"] + student["math"] +\
          student["english"] + student["science"]
  score_avg = score_sum / 4
  print(student["name"], score_sum, score_avg, sep = "\t")
# students 리스트 생성 시에 key를 잘못 입력하거나 하는 일이 생기지 않게 됨.
# 합계, 평균을 구하는 부분도 마찬가지로 객체로 뺄 수 있음.
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
        }

def student_get_sum(student):
  return student["korean"] + student["math"] +\
      student["english"] + student["science"]

def student_get_avg(student):
  return student_get_sum(student) / 4

def student_to_string(student):
  return "{}\t{}\t{}".format(
      student["name"],
      student_get_sum(student),
      student_get_avg(student))
  
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤인성", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep = "\t")
for student in students :
  print(student_to_string(student))

# 클래스
# 생성자(__init_)
class Student:
  def __init__(self, name, korean, math, english, science): # 소멸자는 __del__
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤인성", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

# 메소드
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

  def to_string(self):
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
  print(student.to_string())
