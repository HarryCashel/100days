"""Program to add even numbers from and including 1 - 100"""

sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
print(f"The sum of even numbers between 1 and 100 inclusive is: {sum_even}")

for i in range(101):
    if i % 2 != 0:
        sum_odd += i
print(f"The sum of odd numbers between 1 and 100 inclusive is: {sum_odd}")


def sum_numbers(start_number, end_number, odd_or_even):
    sum_num = 0
    if odd_or_even == "odd":
        for i in range(start_number, end_number):
            if i % 2 != 0:
                sum_num += i
    elif odd_or_even == "even":
        for i in range(start_number, end_number + 1):
            if i % 2 == 0:
                sum_num += i
    return sum_num


start_number = int(input("Enter the first number: "))
end_number = int(input("Enter the last number: "))
odd_or_even = input("Odd or even numbers? ")
print(sum_numbers(start_number, end_number, odd_or_even))

