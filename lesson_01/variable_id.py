

my_dict = {"age": 35, "name": "Alex", "first_name": 45}
print(id(my_dict))

ids = {45, 67, 89, 45}
ids = [45, 67, 89, 45]
print(id(ids))

print(ids)

del ids

# print(ids)  # Deleted object