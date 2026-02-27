numbers = [1, -2, -3, 4, 5]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_numbers)
print(negative_numbers)
print(even_nums)
print(odd_nums)
