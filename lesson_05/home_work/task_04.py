total = 0
count = 5

for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    total += number

average = total / count

print("The average is:", average)
