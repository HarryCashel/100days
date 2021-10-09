"""List Comprehension"""

# Syntax
# new_list = [new_item for item in list *optional conditional*]

num_list = [1, 2, 3]
new_list = [i + 1 for i in num_list]
print(new_list)

name = "Harry"
letter_list = [l for l in name]
print(letter_list)

doubled = [n*2 for n in range(1, 5)]
print(doubled)

names = ["Beth", "Alex", "Caroline", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
