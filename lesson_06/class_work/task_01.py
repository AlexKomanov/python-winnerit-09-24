original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

reg_even_numbers = get_even_numbers(original_numbers)

print(f"Using Regular function: {reg_even_numbers}")

even_numbers_lambda = list(filter(lambda num: num % 2 == 0, original_numbers))
print(f"Using Lambda function: {even_numbers_lambda}")