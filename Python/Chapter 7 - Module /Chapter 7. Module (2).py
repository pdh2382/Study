# 외부 모듈 다뤄보기

# Beautiful Soup모듈
pip install beautifulsoup4

from urllib import request
from bs4 import BeautifulSoup # 패키지여서 대문자가 사용됨.

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
  print("도시:", location.select_one("city").string)
  print("날씨:", location.select_one("wf").string)
  print("최저기온:", location.select_one("tmn").string)
  print("최고기온:", location.select_one("tmx").string)

# Flask 모듈
pip install flask

from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터
def hello():
    return "<h1>Hello World!</h1>"
# 위 코드를 실행하면, Hello World라는 글자를 출력하는 웹 서버와 연결되는 URL을 출력해줌.
# 실행법도 특이한데, 
$env:FLASK_APP="파일 이름"
flask run
# 위 코드를 명령 프롬프트에서 입력해야함.

# 라이브러리 : 개발자가 모듈의 기능을 직접 호출하는 형태의 모듈
# 프레임워크 : 모듈이 개발자가 작성한 코드를 실행하는 형태의 모듈

# 데코레이터
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()
# 이를 잘 이용하면 매개변수 등을 전달해 가독성을 늘리는 등 유용하게 사용할 수 있음.
