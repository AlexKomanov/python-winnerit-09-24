# number = int(input("Write a number: "))
#
#
# print("Before if statement...")
#
# if number > 0:
#     print(f"A number {number} is greater than 0.")
#     print(f"A number {number} integrated...")
#     print(f"Creating a message...")
#     print(f"A number {number} is greater than 0.")
# print("After if statement...")


# indentation error
number = 5
#
# if number > 0:
# print(f"A number {number} integrated...")
#
# print("After if statement...")

# colon error
# if number > 0
#     print(f"A number {number} integrated...")


# empty block + pass

status = 400

if status == 300:
    print("Status 300")

if status == 400:
    pass

if status == 500:
    pass

print("After if statement...")