numbers = [19, 13, 2, 5, 3, 11, 7, 17 ]

new_list = sorted(numbers, reverse=True)
print(new_list)
print(numbers)

numbers.sort(reverse=True)#솔트는 원래값에도 영향이 간다.
print(numbers)