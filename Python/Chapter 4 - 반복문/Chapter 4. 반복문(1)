# 리스트
# 마찬가지로 0부터 인덱스 시작
# 리스트 안에 리스트, 인덱스 안에 인덱스도 가능
list_a = ["문자열",0, 2, True]
list_a[0]

list_b = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
lsit_b[0][1]

#요소 추가하기 - append
list_a.append(7)
list_a

# 요소 추가하기 - insert
list_a.insert(0, 10)
list_a

# 요소 삭제하기 - del
del list_a[0]
list_a

# 요소 삭제하기 - pop()
list_a.pop()
list_a
#별다른 입력이 없으면 제일 마지막 값 삭제
# remove()로 지우고 싶은 값을 지정하거나,
# clear()로 전부 지우기도 가능

# 반복문을 활용해 새 리스트를 만들 수도 있음.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
  output[number%3-1].append(number)

print(output)

# 반복문 활용2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(numbers) // 2 ):
  j = i*2 +1
  print(f"i = {i}, j = {j}")
  numbers[j] = numbers[j] ** 2

print(numbers)
