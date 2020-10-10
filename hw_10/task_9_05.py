from functools import reduce
list_number = [1, 2, 3, 4, 5, 6]
new_list = filter(lambda x: x % 3 == 0, list_number)
multiplication_of_numbers = reduce(lambda a, x: a * x, list(new_list))
print(multiplication_of_numbers)

