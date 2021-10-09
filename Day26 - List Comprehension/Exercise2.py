numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55]

squared = [n**2 for n in numbers]

print(squared)

even_nums = [n for n in numbers if n % 2 == 0]
print(even_nums)