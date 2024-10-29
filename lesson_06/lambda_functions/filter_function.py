numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

squared_numbers_list = list(map(lambda x : x ** 2, even_numbers))
print(squared_numbers_list)