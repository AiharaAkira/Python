#리스트
numbers = [2,3,5,7]
names = ["윤수", "혜린", "태호", "양훈"]
print(numbers)
print(names)

#인덱싱
print(names[0])
print(numbers[1] + numbers[3])
num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)
print(numbers[-1])
print(numbers[-2])
print(numbers[-4])

#리스트 슬라이싱
print(names[0:4])
print(numbers[:3])#x번부터 j개
print(numbers[0:])
numbers[0] = 7
print(numbers[0])
numbers[0] = numbers[0] + numbers[1]
print(numbers[0])