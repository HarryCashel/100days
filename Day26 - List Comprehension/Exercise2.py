numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55]

squared = [n**2 for n in numbers]

print(squared)

even_nums = [n for n in numbers if n % 2 == 0]
print(even_nums)

list1 = [int(num.strip()) for num in open("file1.txt")]
print(list1)

list2 = [int(num.strip()) for num in open("file2.txt")]
print(list2)

result = [num for num in list1 if num in list2]
print(result)