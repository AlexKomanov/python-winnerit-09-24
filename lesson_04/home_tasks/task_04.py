# The initial list of numbers from 1 to 16
numbers = list(range(1, 17))

# List to store the removed elements
removed_elements = []

# Step 1: Remove the element at the last position
removed_elements.append(numbers.pop(-1))  # Last element

# Step 2: Remove the element at the 0th position
removed_elements.append(numbers.pop(0))  # First element (index 0)

# Step 3: Remove the element at the 12th position
removed_elements.append(numbers.pop(12))  # Element at index 12

# Step 4: Remove the element at the 7th position
removed_elements.append(numbers.pop(7))  # Element at index 7

# Output the modified list
print(numbers)

# List of removed items
print(removed_elements)

# Output the sum of the removed elements
print(sum(removed_elements))
