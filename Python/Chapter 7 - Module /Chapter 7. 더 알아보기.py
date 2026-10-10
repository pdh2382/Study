# operator 모듈 - itemgetter()
# min, max함수에서 특정 키 기준으로 구할 때의 코드 복습.
books = [{
    "제목": "혼자 공부하는 파이썬"
    "가격": 18000
},{
    "제목": "혼자 공부하는 머신러닝"
    "가격": 26000
},{
    "제목": "혼자 공부하는 데이터분석"
    "가격": 24000
}]

print(min(books, key = lambda book: book["가격"]))
# 람다는 어려운 문법임. 따라서 다른 사람들이 이해하는 데에 어려울 수 있음.

def 가격추출함수(book):
    return book["가격"]
print(max(books, key=가격추출함수))
# 콜백함수를 이용하면, 그 함수가 뭔지 알아내기 위해 다시 위로 올라가야 함.

# itemgetter()함수 활용
# 특정 요소를 추출하는 함수를 만들어 줌.
from operator import itemgetter
...생략...

print(min(books, key=itemgetter("가격")))
# 위처럼 응용 가능. 

# 더 알아보기
# python prime module
# PrimePy
from primePy import primes
a = primes.check(5)
print(a)

# 100부터 1000 사이 소수 개수세기
b = primes.between(100, 1000)
print(len(b))

# 인공지능 개발 분야의 모듈 찾아보기
# scikit_learn, tensorflow, keras 등의 모듈이 있음.
# [핸즈온 머신러닝]으로 공부할 수 있을듯.
